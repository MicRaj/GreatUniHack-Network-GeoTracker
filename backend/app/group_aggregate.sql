WITH TotalData AS (
  SELECT
    ip_dest AS ip,
    SUM(length) AS total_bytes_sent,
    SUM(CASE WHEN ip_src = ip_dest THEN length ELSE 0 END) AS total_bytes_received
  FROM
    pcapentry
  WHERE
    timestamp BETWEEN 1730666069 AND 1730666080
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
    timestamp BETWEEN 1730666069 AND 1730666080
  GROUP BY
    ip_dest, protocol
)
SELECT
  td.ip,
  td.total_bytes_sent,
  td.total_bytes_received,
  pd.protocol,
  pd.protocol_bytes
FROM
  TotalData td
JOIN
  ProtocolData pd ON td.ip = pd.ip;