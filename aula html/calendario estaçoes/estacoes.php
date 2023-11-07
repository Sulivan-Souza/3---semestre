<!-- Calendario que mostra as estacoes do ano quando selecionado o mes pelo usuario-->
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
            $mes = $_POST["mes"];
            switch ($mes) {
                case 1:
                case 2:
                case 12:
                    echo "<img src='inverno.jpg'>";
                    break;
                case 3:
                case 4:
                case 5:
                    echo "<img src='primavera.jpg'>";
                    break;
                case 6:
                case 7:
                case 8:
                    echo "<img src='verao.jpg'>";
                    break;
                case 9:
                case 10:
                case 11:
                    echo "<img src='outono.jpg'>";
                    break;
            }
        ?>
    </div>
</html>





