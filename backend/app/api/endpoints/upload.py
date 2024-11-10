from scapy.all import *
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()


class PCAPEntry():

    def getProtocolFromNumber(id):
        if id == 6:
            return "TCP"
        elif id == 17:
            return "UDP"
        else:
            return "N/A"

    def __init__(self, entry):
        if (entry.haslayer("IP")):
            self.m_timestamp = entry.time
            self.m_IPDest = entry["IP"].dst
            self.m_IPSrc = entry["IP"].src
            self.m_protocol = PCAPEntry.getProtocolFromNumber(
                entry["IP"].proto)
        else:
            self.m_timestamp = entry.time
            self.m_IPDest = "N/A"
            self.m_IPSrc = "N/A"
            self.m_protocol = "N/A"


def makePCAPEntryList(filePath):
    pcap = rdpcap(filePath)
    entries = []
    entriesCount = 0
    entriesRead = 0

    for entry in pcap:
        entriesCount += 1
        temp = PCAPEntry(entry)
        if (temp.m_IPDest != "N/A"):
            entries.append(temp)
            entriesRead += 1

    return entries, entriesCount, entriesRead


@router.post("/upload")
async def upload_pcap(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    entries, entriesCount, entriesRead = makePCAPEntryList(file.filename)

    print(
        f"Number of entries = {entriesCount}\nEntries read = {entriesRead}\n")

    for entry in entries:
        print(entry.m_IPSrc, entry.m_IPDest, entry.m_protocol)

    return {"detected": entriesCount,
            "read": entriesRead}
