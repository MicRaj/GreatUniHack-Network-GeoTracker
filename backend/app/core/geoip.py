from sqlmodel import Session, text

# connect to database


# Convert IP into all possible combinations of subnet it could be
def generate_subnets(ip_address):
    """Generates all possible subnets for a given IP address.

    Args:
        ip_address: The IP address as a string.

    Returns:
        A list of subnet strings in CIDR notation.
    """

    ip_value = ip_address.split('.')
    ip_value = int(ip_value[0]) << 24 | int(ip_value[1]) << 16 | int(ip_value[2]) << 8 | int(ip_value[3])
    subnets = []

    for prefix_len in range(32, 0, -1):
        subnet_mask = 0xFFFFFFFF << (32 - prefix_len)
        subnet_address = ip_value & subnet_mask
        subnet = f"{subnet_address >> 24 & 0xFF}.{subnet_address >> 16 & 0xFF}.{subnet_address >> 8 & 0xFF}.{subnet_address & 0xFF}/{prefix_len}"
        subnets.append(subnet)

    return subnets

def get_geo_info(ip: str, db: Session):
    a = db.exec(text("SELECT * FROM geoip WHERE network IN (\""+'\",\"'.join(generate_subnets(ip))+"\");"))
    fetched = a.fetchone()

    if fetched is None:
        dict_duct_tape = {
            "network": None,
            "post_code": None,
            "latitude": None,
            "longitude": None,
            "accuracy_radius": None,
            "registered_country": None,
            "represented_country": None,
            "place": None
        }
    else:
        # TODO: Fix this as is very botched
        dict_duct_tape = {
            "network": fetched[0],
            "post_code": fetched[1],
            "latitude": fetched[2],
            "longitude": fetched[3],
            "accuracy_radius": fetched[4],
            "registered_country": fetched[5],
            "represented_country": fetched[6],
            "place": fetched[7]
        }

    return dict_duct_tape