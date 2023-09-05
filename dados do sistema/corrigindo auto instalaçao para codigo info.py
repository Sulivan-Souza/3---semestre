import os
import platform
import datetime
import subprocess
import psutil
import sys

def check_required_libraries():
    libraries = ['psutil']

    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"Error: The '{lib}' library is missing. Installing it...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

def get_system_info():
    check_required_libraries()

    try:
        system = platform.system()

        if system == 'Linux':
            ip_address = subprocess.getoutput("hostname -I | awk '{print $1}'").strip()
            mac_address_output = subprocess.getoutput("cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address").strip()
            mac_address = ':'.join(mac_address_output[i:i+2] for i in range(0, len(mac_address_output), 2))
            df_output = subprocess.getoutput("df -h / | awk 'NR==2{print $5}'").strip()
        elif system == 'Windows':
            ip_address = subprocess.getoutput("ipconfig | findstr IPv4 | findstr -v IPv4\\s\\+:\\s\\+0.0.0.0").split()[-1]
            mac_address_output = subprocess.getoutput("getmac /NH /FO CSV").strip()
            mac_address = mac_address_output.splitlines()[0].split(',')[0].replace('-', '').replace('"', '').strip()
            mac_address = ':'.join(mac_address[i:i+2] for i in range(0, len(mac_address), 2))
            df_output = subprocess.getoutput("wmic logicaldisk where caption='C:' get FreeSpace,Size /format:list").strip()
            free_space, total_size = [int(val.split('=')[1]) for val in df_output.split('\n') if val.startswith("FreeSpace") or val.startswith("Size")]
            df_output = f"{(free_space / total_size) * 100:.2f}%"
        else:
            ip_address = "N/A"
            mac_address = "N/A"
            df_output = "N/A"

        hostname = subprocess.getoutput("hostname").strip()

        memory_usage = f"{psutil.virtual_memory().percent:.2f}%"
        cpu_usage = f"{psutil.cpu_percent(interval=1):.2f}%"

        return ip_address, mac_address, hostname, df_output, memory_usage, cpu_usage
    except Exception as e:
        print("Error:", e)
        return None, None, None, None, None, None
    
current_datetime = datetime.datetime.now().strftime("Data: %Y-%m-%d Hora: %H-%M-%S")

if __name__ == "__main__":
    ip_address, mac_address, hostname, free_disk_space, memory_usage, cpu_usage = get_system_info()

    if ip_address is not None and mac_address is not None and hostname is not None and free_disk_space is not None and memory_usage is not None and cpu_usage is not None:
        info_text = f"{current_datetime}\n"
        info_text += f"Hostname: {hostname}\n"
        info_text += f"IP address: {ip_address}\n"
        info_text += f"MAC address: {mac_address}\n"
        info_text += f"Espaço Livre em Disco: {free_disk_space}\n"
        info_text += f"Uso de Memória: {memory_usage}\n"
        info_text += f"Uso de CPU: {cpu_usage}\n"
        
        print(info_text)

        with open("info_system.txt", "a") as file:
            file.write(info_text)
        print("As informações foram salvas no arquivo 'info_system.txt'.") 
        print("No mesmo diretório onde este codigo está localizado.\n")

        if platform.system() == "Linux":
            input("Pressione Enter para continuar...")

        if platform.system() == "Windows":
            input("Pressione Enter para continuar...")
