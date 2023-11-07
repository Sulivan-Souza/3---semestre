from flask import Flask, request, render_template, escape
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping')
def ping():
    ip_address = request.args.get('ip')

    # Validar o endereço IP inserido pelo usuário
    if not ip_address or not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip_address):
        return 'Endereço IP inválido.', 400

    try:
        result = subprocess.check_output(['ping', '-c', '4', ip_address], universal_newlines=True)
        return f'<pre>{escape(result)}</pre>'
    except subprocess.CalledProcessError as e:
        return 'Erro ao testar o ping.', 500

if __name__ == '__main__':
    app.run(debug=True)
