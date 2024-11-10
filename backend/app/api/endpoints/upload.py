from scapy.all import rdpcap
from fastapi import APIRouter, File, UploadFile
import shutil

from sqlmodel import Session

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
