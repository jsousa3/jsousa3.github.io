
# Primeiro programa

No mundo da informática, quando se começa a trabalhar numa nova linguagem de programação, costuma-se fazer um programa que mostre a frase "Hello World".

Em Python, esse programa é este.

### Programa

<pre><code class="lang-python">{% include "./hello.py" %}</code></pre>

Para escrever e executar este programa faça:

1. Entre no IDLE.

2. Faça `Ctrl n` para criar um novo programa.

3. Escreva o programa

4. Faça `Ctrl s`, escolha uma pasta no seu computador e escreva `hello.py`, para gravar o programa dentro da pasta escolhida, no ficheiro `hello.py`. Note que as pastas no contexto Python se chamam diretorias.

5. Faça `F5` para executar o programa. Deverá ter obtido na janela de
*output* Python a frase `Hello World`.

## Como funciona

Neste programa, `print` é uma **função** e `'Hello World'` é um
**valor**.

Quando o programa é executado pelo interpretador Python, a linha
`print('Hello World')`, é lida do ficheiro `hello.py`, e é
interpretada. O nome `print`, seguindo de parentsis curvos com um
valor dentro, é interpretado como a chamada à função `print`. O valor
dentro de parentsis é criado em memória. A função `print` é executada
e é-lhe passado o valor `'Hello World'`. A função `print` mostra então
na janela de *output* o valor que recebeu.
