
from .schemas import NetworkDataCreate, NetworkData
from .database import get_db

# Create a new network data entry with a custom time
def create_network_data(data: NetworkDataCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO network_data (time, source_ip, destination_ip, protocol)
        VALUES (?, ?, ?, ?)
    ''', (data.time, data.source_ip, data.destination_ip, data.protocol))
    conn.commit()
    conn.close()

# Get all network data entries with pagination
def get_network_data(skip: int = 0, limit: int = 100):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM network_data LIMIT ? OFFSET ?', (limit, skip))
    rows = cursor.fetchall()
    conn.close()
    return [NetworkData(id=row['id'], time=row['time'], source_ip=row['source_ip'],
                        destination_ip=row['destination_ip'], protocol=row['protocol']) for row in rows]
