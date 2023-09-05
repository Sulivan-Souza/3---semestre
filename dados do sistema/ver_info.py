import os
import platform
import psutil
import datetime

def check_required_libraries():
    libraries = ['psutil']

    for lib in libraries:
        try:
            import psutil
        except ImportError:
            print(f"Error: The '{lib}' library is missing. Installing it...")
            os.system(f"pip3 install {lib}")

def get_system_info():
    check_required_libraries()

    try:
        system = platform.system()

        if system == 'Linux':
            ip_address = os.popen("hostname -I | awk '{print $1}'").read().strip()
            mac_address_output = os.popen("cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address").read().strip()
            mac_address = ':'.join(mac_address_output[i:i+2] for i in range(0, len(mac_address_output), 2))
            df_output = os.popen("df -h / | awk 'NR==2{print $5}'").read().strip()
        elif system == 'Windows':
            ip_address = os.popen("ipconfig | findstr IPv4 | findstr -v IPv4\\s\\+:\\s\\+0.0.0.0").read().split()[-1]
            mac_address_output = os.popen("getmac /NH /FO CSV").read().strip()
            mac_address = mac_address_output.splitlines()[0].split(',')[0].replace('-', '').replace('"', '').strip()
            mac_address = ':'.join(mac_address[i:i+2] for i in range(0, len(mac_address), 2))
            df_output = os.popen("wmic logicaldisk where caption='C:' get FreeSpace,Size /format:list").read().strip()
            free_space, total_size = [int(val.split('=')[1]) for val in df_output.split('\n') if val.startswith("FreeSpace") or val.startswith("Size")]
            df_output = f"{(free_space / total_size) * 100:.2f}%"
        else:
            ip_address = "N/A"
            mac_address = "N/A"
            df_output = "N/A"

        hostname = os.popen("hostname").read().strip()

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
            os.system("read -p 'Pressione Enter para continuar...'")

        if platform.system() == "Windows":
            input("Pressione Enter para continuar...")
