<!DOCTYPE html>
<html>
<head>
    <title>Estações do ano</title>
</head>
<body>
    <div class="container">
        <h1>Estações do ano</h1>
        <form action="estacoes.php" method="post">
            <label for="mes">Selecione o mês:</label>
            <select name="mes" id="mes">
                <option value="1">Janeiro</option>
                <option value="2">Fevereiro</option>
                <option value="3">Março</option>
                <option value="4">Abril</option>
                <option value="5">Maio</option>
                <option value="6">Junho</option>
                <option value="7">Julho</option>
                <option value="8">Agosto</option>
                <option value="9">Setembro</option>
                <option value="10">Outubro</option>
                <option value="11">Novembro</option>
                <option value="12" selected>Dezembro</option>
            </select>
            <input type="submit" value="Enviar">
        </form>
        <?php
            if (isset($_POST["mes"])) {
                $mes = $_POST["mes"];
                $estacao = "";
                switch ($mes) {
                    case 1:
                    case 2:
                    case 12: 
                        $estacao = "Inverno";
                        $imagem = "inverno.jpg";
                        break;
                    case 3:
                    case 4:
                    case 5:
                        $estacao = "Primavera";
                        $imagem = "primavera.jpg";
                        break;
                    case 6:
                    case 7:
                    case 8:
                        $estacao = "Verão";
                        $imagem = "verao.jpg";
                        break;
                    case 9:
                    case 10:
                    case 11:
                        $estacao = "Outono";
                        $imagem = "outono.jpg";
                        break;
                    default:
                        echo "Mês inválido";
                        break;
                }
                if (file_exists($imagem)) {
                    echo '<img src="' . $imagem . '" alt="Imagem da estação ' . $estacao . '">';
                    echo '<p>A estação é: <strong>' . strtoupper($estacao) . '</strong></p>';
                } else {
                    echo "Imagem não encontrada para esta estação.";
                }
            }
        ?>
    </div>
</body>
</html>
