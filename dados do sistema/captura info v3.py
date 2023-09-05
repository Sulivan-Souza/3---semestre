import os
import platform
import psutil
import datetime
import subprocess

def check_required_libraries():
    libraries = ['psutil']

    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            print(f"Erro: A biblioteca '{lib}' está faltando. Tentando instalá-la...")
            subprocess.run(["pip3", "install", lib])

def get_ip_address():
    if platform.system() == 'Linux':
        return os.popen("hostname -I | awk '{print $1}'").read().strip()
    elif platform.system() == 'Windows':
        return os.popen("ipconfig | findstr IPv4 | findstr -v IPv4\\s\\+:\\s\\+0.0.0.0").read().split()[-1]
    else:
        return "N/A"

def get_mac_address():
    if platform.system() == 'Linux':
        mac_address_output = os.popen("cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address").read().strip()
        return ':'.join(mac_address_output[i:i+2] for i in range(0, len(mac_address_output), 2))
    elif platform.system() == 'Windows':
        mac_address_output = os.popen("getmac /NH /FO CSV").read().strip()
        mac_address = mac_address_output.splitlines()[0].split(',')[0].replace('-', '').replace('"', '').strip()
        return ':'.join(mac_address[i:i+2] for i in range(0, len(mac_address), 2))
    else:
        return "N/A"

def get_disk_space():
    if platform.system() == 'Linux':
        df_output = os.popen("df -h / | awk 'NR==2{print $5}'").read().strip()
        return df_output
    elif platform.system() == 'Windows':
        df_output = os.popen("wmic logicaldisk where caption='C:' get FreeSpace,Size /format:list").read().strip()
        free_space, total_size = [int(val.split('=')[1]) for val in df_output.split('\n') if val.startswith("FreeSpace") or val.startswith("Size")]
        return f"{(free_space / total_size) * 100:.2f}%"
    else:
        return "N/A"

def get_system_info():
    check_required_libraries()

    try:
        ip_address = get_ip_address()
        mac_address = get_mac_address()
        disk_space = get_disk_space()
        hostname = os.popen("hostname").read().strip()

        memory_usage = f"{psutil.virtual_memory().percent:.2f}%"
        cpu_usage = f"{psutil.cpu_percent(interval=1):.2f}%"

        return ip_address, mac_address, hostname, disk_space, memory_usage, cpu_usage
    except Exception as e:
        print("Erro:", e)
        return None, None, None, None, None, None
    
current_datetime = datetime.datetime.now().strftime("Data: %Y-%m-%d Hora: %H-%M-%S")

if __name__ == "__main__":
    ip_address, mac_address, hostname, disk_space, memory_usage, cpu_usage = get_system_info()

    if ip_address is not None and mac_address is not None and hostname is not None and disk_space is not None and memory_usage is not None and cpu_usage is not None:
        info_text = f"{current_datetime}\n"
        info_text += f"Hostname: {hostname}\n"
        info_text += f"Endereço IP: {ip_address}\n"
        info_text += f"Endereço MAC: {mac_address}\n"
        info_text += f"Espaço Livre em Disco: {disk_space}\n"
        info_text += f"Uso de Memória: {memory_usage}\n"
        info_text += f"Uso de CPU: {cpu_usage}\n"
        
        print(info_text)

        with open("info_system.txt", "a") as file:
            file.write(info_text)
        print("As informações foram salvas no arquivo 'info_system.txt'.") 
        print("No mesmo diretório onde este código está localizado.\n")

        input("Pressione Enter para continuar...")
 