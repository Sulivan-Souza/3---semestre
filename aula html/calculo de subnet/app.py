from flask import Flask, request, render_template
import ipaddress

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            endereco_ip = request.form["ip"]
            mascara = request.form["mascara"]

            rede = ipaddress.IPv4Network(f"{endereco_ip}/{mascara}", strict=False)
            endereco_de_rede = rede.network_address
            endereco_de_broadcast = rede.broadcast_address
            quantidade_de_hosts = len(list(rede.hosts()))
            faixa_de_ips_disponiveis = f"{rede.network_address + 1} - {rede.broadcast_address - 1}"

            resultado = {
                "endereco_de_rede": endereco_de_rede,
                "endereco_de_broadcast": endereco_de_broadcast,
                "quantidade_de_hosts": quantidade_de_hosts,
                "faixa_de_ips_disponiveis": faixa_de_ips_disponiveis,
            }
        except Exception as e:
            erro = str(e)

    return render_template("index.html", resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
