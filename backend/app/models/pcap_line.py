from sqlmodel import Field, SQLModel

class PCAPEntry(SQLModel, table=True):
    id: int | None = Field(index=True, default=None, primary_key=True)
    timestamp: float = Field(index=True)
    ip_dest: str 
    ip_src: str
    protocol: str

    @staticmethod
    def get_protocol_from_number(id):
        if id == 6:
            return "TCP"
        elif id == 17:
            return "UDP"
        else:
            return "N/A"

    @classmethod
    def from_packet(cls, entry):
        if entry.haslayer("IP"):
            return cls(
                    id=None,
                    timestamp=entry.time,
                    ip_dest=entry["IP"].dst,
                    ip_src=entry["IP"].src,
                    protocol=cls.get_protocol_from_number(entry["IP"].proto),
                )
        return cls(
                    id=None,
            timestamp=entry.time,
            ip_dest="N/A",
            ip_src="N/A",
            protocol="N/A",
        )