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

    // Converte caracteres não UTF-8 e preserva novas linhas
    $pingResult = utf8_encode($pingResult);
    $pingResult = nl2br($pingResult);

    /* Remove acentos e substitui por caracteres sem acentos */
    $pingResult = strtr($pingResult, 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ', 'aaaaeeiooouucAAAAEEIOOOUUC');

    echo '<!DOCTYPE html>';
    echo '<html>';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<title>Teste de Ping - Resultado</title>';
    echo '<style>
        /* Estilos CSS para a página */
        body {
            font-family: Arial, sans-serif;
            background-image: url(\'tracert1.jpg\'); /* Substitua com a URL da sua imagem de fundo */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            max-width: 500px;
            background-color: rgba(255, 255, 255, 0.9); /* Adiciona transparência ao fundo */
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
            text-align: center;
            padding: 20px;
            margin: 0 auto;
        }

        h1 {
            font-size: 30px;
            color: #333;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        label {
            font-size: 20px;
            margin-bottom: 10px;
            color: #333;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            font-size: 18px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-bottom: 15px;
        }

        input[type="submit"] {
            width: 100%;
            padding: 15px;
            font-size: 18px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        /* Estilos para o rodapé */
        footer {
            width: 100%;
            position: absolute;
            bottom: 0;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 10px 0;
            font-size: 16px;
            color: #333;
            border-top: 1px solid #ccc;
            left: 0;
            right: 0;

        }
    </style>';
    echo '</head>';
    echo '<body>';
    echo '<div class="container">';
    echo '<h1>Teste de Ping - Resultado</h1>';

    if ($pingResult) {
        echo '<div id="ping-results">' . $pingResult . '</div>';
    } else {
        echo '<div id="ping-results">Erro ao testar o ping.</div>';
    }

    echo '<form method="post" action="index.html">';
    echo '<input type="submit" name="submit" value="Realizar outro teste">';
    echo '</form>';

    // Nome do autor no rodapé da página PHP
    echo '<footer>Sulivan Souza @ 2023 sulivan.souza@fatec.sp.gov.br</footer>';
    
    echo '</div>';
    echo '</body>';
    echo '</html>';
} else {
    header('Location: index.html');
}
?>
