import sqlite3

# connect to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

ip = "148.252.141.213"

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

# print(generate_subnets(ip))
# print("SELECT * FROM geoip WHERE network IN (\""+'\",\"'.join(generate_subnets(ip))+"\");")
a = c.execute("SELECT * FROM geoip WHERE network IN (\""+'\",\"'.join(generate_subnets(ip))+"\");")
print(a.fetchall())