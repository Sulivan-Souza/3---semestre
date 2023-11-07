from flask import Flask, request, render_template
import ipcalc  # Importe a biblioteca ipcalc

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            endereco_ip = request.form["ip"]
            mascara = request.form["mascara"]

            rede = ipcalc.IP(endereco_ip, mascara)
            endereco_de_rede = rede.network()
            endereco_de_broadcast = rede.broadcast()
            quantidade_de_hosts = rede.size() - 2  # Excluindo o endereço de rede e broadcast
            faixa_de_ips_disponiveis = f"{rede[1]} - {rede[-2]}"

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
