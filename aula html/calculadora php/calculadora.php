<!-- Calculadora.php -->


<!DOCTYPE html>
<html>
<head>
    <title>Calculadora</title>
</head>
<body>
    <h1>Calculadora</h1>
    <form method="post" action="">
        <label for="numero1">Número 1:</label>
        <input type="text" name="numero1" id="numero1" required><br><br>
        
        <label for="numero2">Número 2:</label>
        <input type="text" name="numero2" id="numero2" required><br><br>
        
        <label for="operacao">Operação:</label>
        <select name="operacao" id="operacao">
            <option value="soma">Soma</option>
            <option value="subtracao">Subtração</option>
            <option value="multiplicacao">Multiplicação</option>
            <option value="divisao">Divisão</option>
        </select><br><br>
        
        <input type="submit" name="calcular" value="Calcular">
    </form>
 
    <?php
    if(isset($_POST['calcular'])) {
        // Obtém os números inseridos pelo usuário
        $numero1 = $_POST['numero1'];
        $numero2 = $_POST['numero2'];
        $operacao = $_POST['operacao'];
        
        // Inicializa a variável que armazenará o resultado
        $resultado = 0;
 
        // Realiza a operação escolhida
        switch ($operacao) {
            case 'soma':
                $resultado = $numero1 + $numero2;
                break;
            case 'subtracao':
                $resultado = $numero1 - $numero2;
                break;
            case 'multiplicacao':
                $resultado = $numero1 * $numero2;
                break;
            case 'divisao':
                if ($numero2 != 0) {
                    $resultado = $numero1 / $numero2;
                } else {
                    echo "<p>Impossível dividir por 0.</p>";
                }
                break;
            
            default:
                echo "<p>Operação inválida.</p>";
                break;
        }
 
        // Exibe o resultado
        echo "<p>O resultado da $operacao de $numero1 e $numero2 é: $resultado</p>";
    }
    ?>
</body>
</html>