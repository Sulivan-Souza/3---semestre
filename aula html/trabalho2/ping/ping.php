<?php
if (isset($_POST['submit'])) {
    $ipAddress = $_POST['ip-address'];
    
    // Verifica se o sistema suporta a opção -c no ping
    $isCOptionSupported = false;
    exec('ping -c 1 127.0.0.1', $output, $returnCode);
    if ($returnCode === 0) {
        $isCOptionSupported = true;
    }

    // Executa o comando ping com ou sem a opção -c com base no suporte
    if ($isCOptionSupported) {
        $pingResult = shell_exec("ping -c 4 $ipAddress");
    } else {
        $pingResult = shell_exec("ping $ipAddress");
    }

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

    if ($pingResult) {
        echo '<div id="ping-results"><pre>' . $pingResult . '</pre></div>';
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
