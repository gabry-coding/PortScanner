
import socket

from ultils import ectract_jsonData

class PScan:

    PORTA_DATA_FILE = "/.common_ports.json"
   
    def__init__(self):
    self.open.ports =[]
    self.ports_info = {}

def get_ports_info():
            data = extract_json_data(PORTS_DATA_FILE)
            ports_info ={int (k): v for (k, v) in data.items()}
            return ports_info
@staticmethod
def get_host_ip_addr(target)
    try:
    ip_addr = socket.gethostbyname(target)
    exepct socket.gaierror as e:
    print(f"C'e stato un errore..."{è}")
    else:
        return ip_addr

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    conn_status= sock.connect_ex((ip, port))
    if conn_status == 0:
        OPEN_PORTS.append(port)
    sock.close()

    if__name__ == "main__":
    print("Programma")
    target = input("Inserire target")
    ip_addr = get_hosts_ip_addr(target)
    ports_info = get_ports_info()


   for ports in ports_info.keys():
        try:
        print(f"scanning:{ip_addr}:{port}")
        sca_port(ip_addr, port)
        except KeyboardInterrupt:
        print("\nExiting...")
        break 

print("Open Pprts"):
for port in OPEN_PORTS:
    print(str(port), ports_info[info])