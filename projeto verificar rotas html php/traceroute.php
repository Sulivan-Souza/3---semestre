<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $destination = $_POST["destination"];
    if (!empty($destination)) {
        $traceroute_output = shell_exec("traceroute " . escapeshellarg($destination));
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Rastreamento de Rota - Resultados</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
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
</body>
</html>
