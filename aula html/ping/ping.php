<?php
if (isset($_POST['submit'])) {
    $ipAddress = $_POST['ip-address'];
    
    // Validar o endereço IP inserido pelo usuário
    if (!filter_var($ipAddress, FILTER_VALIDATE_IP)) {
        echo "Endereço IP inválido.";
        exit;
    }
    
    // Executa o comando ping de maneira segura usando escapeshellarg
    $ipAddress = escapeshellarg($ipAddress);
    exec("ping -c 4 $ipAddress 2>&1", $pingResult, $returnCode);

    echo '<!DOCTYPE html>';
    echo '<html>';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Teste de Ping</title>';
    echo '<link rel="stylesheet" type="text/css" href="styles.css">';
    echo '</head>';
    echo '<body>';
    echo '<div class="container">';
    echo '<h1>Teste de Ping</h1>';
    echo '<form method="post" action="ping.php">';
    echo '<label for="ip-address">Digite o endereço IP:</label>';
    echo '<input type="text" id="ip-address" name="ip-address" required>';
    echo '<input type="submit" name="submit" value="Testar Ping">';
    echo '</form>';

    if ($returnCode === 0) {
        // Exibir a saída do ping com HTML escapado para evitar XSS
        echo '<div id="ping-results"><pre>' . htmlspecialchars(implode("\n", $pingResult)) . '</pre></div>';
    } else {
        echo '<div id="ping-results">Erro ao testar o ping.</div>';
    }

    echo '</div>';
    echo '</body>';
    echo '</html>';
} else {
    header('Location: ping.html');
}
?>
