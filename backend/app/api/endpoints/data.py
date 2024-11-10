from fastapi import APIRouter
from sqlalchemy import text
from app.core.database import SessionDep
from ipaddress import IPv4Address
from app.core.geoip import get_geo_info

router = APIRouter()

@router.get("/data")
def data(starttime: int, endtime: int, db: SessionDep):
    out = db.exec(text(f"""
WITH TotalData AS (
  SELECT
    ip_dest AS ip,
    SUM(length) AS total_bytes_sent,
    SUM(CASE WHEN ip_src = ip_dest THEN length ELSE 0 END) AS total_bytes_received
  FROM
    pcapentry
  WHERE
    timestamp BETWEEN {starttime} AND {endtime}
  GROUP BY
    ip_dest
),
ProtocolData AS (
  SELECT
    ip_dest AS ip,
    protocol,
    SUM(length) AS protocol_bytes
  FROM
    pcapentry
  WHERE
    timestamp BETWEEN {starttime} AND {endtime}
  GROUP BY
    ip_dest, protocol
)
SELECT
  td.ip,
  td.total_bytes_sent as total_transferred,
  pd.protocol,
  pd.protocol_bytes
FROM
  TotalData td
JOIN
  ProtocolData pd ON td.ip = pd.ip;
"""))
    fetched = out.fetchall()

    # Horrible, but there's no one to stop me >:)
    combined = []

    for single in fetched:
        if IPv4Address(single[0]).is_global:
            geo = get_geo_info(single[0], db)
            combined.append({**{
                "ip": single[0],
                "total_bytes_transferred": single[1],
                "protocol": single[2],
                "protocol_bytes": single[3]
            }, **geo})

    return combined

@router.get("/range")
def range(db: SessionDep):
    out = db.exec(text(f"""
SELECT MIN(timestamp) as start, MAX(timestamp) as end FROM pcapentry;
"""))
    fetched = out.fetchone()

    return {"start": fetched[0], "end": fetched[1]}