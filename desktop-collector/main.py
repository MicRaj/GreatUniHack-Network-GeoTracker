import subprocess
import os
from pprint import pprint
import re
from time import sleep
from glob import glob
import requests

p = None


def list_interfaces():
    command_output = subprocess.run(
        ["C:\Program Files\Wireshark\dumpcap.exe", "-D"], capture_output=True)
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

    p = subprocess.Popen(["C:\Program Files\Wireshark\dumpcap.exe", "-i", interface_number, "-b",
                         "interval:60", "-b", "files:2", "-b", "printname:./mostrecent.txt", "-s", "50", "-w", output])
    sleep(10)


def upload(filename):
    url = "http://localhost:8000/upload/upload"
    file = {'file': open(filename.strip(), 'rb')}
    response = requests.post(url, files=file)
    print(f"PCAP Upload response: {response.text}")


def checkLastLineofFile(file):
    with open(file, "rb") as f:
        try:  # catch OSError in case of a one line file
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return last_line


def main_loop():
    prev_recent = checkLastLineofFile("mostrecent.txt")

    try:
        while p.poll() is None:
            new_recent = checkLastLineofFile("mostrecent.txt")
            if new_recent != prev_recent:
                prev_recent = new_recent
                print("New file detected")
                print(f"Uploading file: {new_recent}")
                upload(new_recent)
            sleep(60)
    except KeyboardInterrupt:
        print("Stopping: Keyboard Interrupt")
        pass
    p.kill()


def clean_previous_files():
    if os.path.exists("mostrecent.txt"):
        os.remove("mostrecent.txt")
    for file in glob("capture*.pcap"):
        os.remove(file)


def killPrevious():
    try:
        print("Killing previous instances of dumpcap (if you see that it can't find the process, it's good)")
        subprocess.run(["taskkill", "/IM", "dumpcap.exe", "/F"])
    except:
        pass


if __name__ == "__main__":
    killPrevious()
    clean_previous_files()
    try:  # catch KeyboardInterrupt
        capture(interface="Wi-Fi", output="capture.pcap")
    except ValueError:
        try:
            capture(interface="WiFi", output="capture.pcap")
        except ValueError:
            print("Interface not found")
            exit()
    main_loop()
