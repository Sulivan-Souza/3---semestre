<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $destination = $_POST["destination"];
    if (!empty($destination)) {
        $traceroute_output = shell_exec("tracert " . escapeshellarg($destination));
        $traceroute_output = utf8_encode($traceroute_output); // Converter para UTF-8
        $traceroute_output = str_replace(array('á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'î', 'ô', 'û'), array('a', 'e', 'i', 'o', 'u', 'a', 'o', 'a', 'e', 'i', 'o', 'u'), $traceroute_output); // Remover acentos
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Rastreamento de Rota - Resultados</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('tracert1.jpg') no-repeat center center fixed;
            background-size: cover;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column; /* Alteração para empilhar os elementos verticalmente */
            justify-content: center; /* Centralizar verticalmente */
            align-items: center;
            height: 100vh;
        }
        .container {
            max-width: 800px;
            padding: 30px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 20px; /* Espaçamento inferior da caixa */
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #f7f7f7;
            padding: 10px;
            border-radius: 5px;
            overflow: auto;
            max-height: 400px;
            font-size: 14px;
            line-height: 1.4;
            text-align: left;
        }
        p {
            color: #666;
            margin: 10px 0;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .author-info {
            color: #fcf9f9;
            font-style: italic;
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Resultados do Rastreamento de Rota</h1>
        <?php
        if (isset($traceroute_output)) {
            echo "<pre>$traceroute_output</pre>";
        } else {
            echo "<p>Por favor, insira um destino válido.</p>";
        }
        ?>
        <p><a href="index.html">Voltar</a></p>
    </div>
    <p class="author-info">Sulivan Souza | 2023 | sulivan.souza@fatec.sp.gov.br</p>
</body>
</html>

