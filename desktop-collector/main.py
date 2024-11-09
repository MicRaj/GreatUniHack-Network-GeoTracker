import subprocess
from pprint import pprint
import re
from time import sleep


p = None

def list_interfaces():
    command_output = subprocess.run(["C:\Program Files\Wireshark\dumpcap.exe", "-D"], capture_output=True)
    stdout = command_output.stdout.decode()
    interfaces = {}

    interface_parsed = re.findall(r"([0-9]*)\. .* \((.*)\)", stdout)
    return interface_parsed

def find_interface(iname: str):
    interfaces = list_interfaces()
    for i in interfaces:
        if i[1] == iname:
            return i[0]
    return None

def capture(interface: str, output: str):
    global p
    interface_number = find_interface(interface)
    if interface_number is None:
        raise ValueError("Interface not found")
    p = subprocess.Popen(["C:\Program Files\Wireshark\dumpcap.exe", "-i", interface_number, "-b", "interval:60", "-b", "files:25", "-b", "printname:./mostrecent.txt", "-s", "50", "-w", output])
    sleep(10)

def upload(file):
    pass

def main_loop():
    prev_recent = open("mostrecent.txt", "r").read()

    try:
        while p.poll() is None:
            new_recent = open("mostrecent.txt", "r").read()
            if new_recent != prev_recent:
                prev_recent = new_recent
                print("New file detected")
                print("Uploading...")
                upload(new_recent)
            sleep(60)            
    except:
        pass
    p.kill()

def clean_previous_files():
    subprocess.run(["rm", "-f", "./mostrecent.txt"])
    subprocess.run(["rm", "-f", "./capture*.pcap"])


if __name__ == "__main__":
    clean_previous_files()
    capture(interface="WiFi", output="capture.pcap")
    main_loop()