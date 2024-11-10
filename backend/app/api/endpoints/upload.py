from scapy.all import rdpcap
from fastapi import APIRouter, File, UploadFile
import shutil

import json

from sqlmodel import Session, select, text

from app.models.pcap_line import PCAPEntry
from app.core.database import SessionDep

router = APIRouter()


def makePCAPEntryList(filePath, db: Session):
    pcap = rdpcap(filePath)
    entries = []
    entriesCount = 0
    entriesRead = 0

    for entry in pcap:
        entriesCount += 1
        temp = PCAPEntry.from_packet(entry)
        if (temp.ip_dest != "N/A"):
            entries.append(temp)
            entriesRead += 1

    db.add_all(entries)
    db.commit()
    return entriesCount, entriesRead


@router.post("/upload")
async def upload_pcap(db: SessionDep, file: UploadFile = File(...) ):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    entriesCount, entriesRead = makePCAPEntryList(file.filename, db)

    print(
        f"Number of entries = {entriesCount}\nEntries read = {entriesRead}\n")

    return {"detected": entriesCount,
            "read": entriesRead}

@router.get("/getStats")
async def get_stats(startTimestamp: int, endTimestamp: int, db: SessionDep):
    # query = select(PCAPEntry).where(PCAPEntry.timestamp >= startTimestamp).where(PCAPEntry.timestamp <= endTimestamp).group_by(PCAPEntry.protocol)
    # entries = db.execute(text("SELECT protocol, COUNT(*), SUM(length) FROM pcapentry GROUP BY protocol;")).all()
    entries = db.execute(text("SELECT protocol, COUNT(*) FROM pcapentry GROUP BY protocol;")).all()

    ret = []

    for entry in entries:
        temp = {
            "protocol": entry[0],
            "count" : entry[1],
            # "size": entry[2]
        }
        ret.append(temp)

    return ret