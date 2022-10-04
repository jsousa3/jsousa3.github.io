
## *Hello string type*

Suponhamos que não sabiamos qual o tipo do valor `'Hello
World'`. Existe uma forma de obter essa informação. Usa-se a função
`type`.

**Programa** No ficheiro `string_type.py`

<pre><code class="lang-python">{% include "./string_type.py" %}</code></pre>

**Output**

<pre><code class="lang-python">&#60;class 'str'&#62;</code></pre>

**Como funciona**

O valor `Hello Word` é fornecido à função `type` que retorna uma
*string* que representa o tipo do valor. A *string* retornada pela
função `type` é fornecida à função `print`, que faz o seu *output*.

**Observação**

Os sinais `<` e `>`, obtidos no *output*, são apenas notação usada por
conveniência. A *string* `class` diz respeito a um conceito de
programação orientada por objetos, que a linguagem Python suporta, mas
que está fora do âmbito deste cápitulo. A string `str` essa sim, é,
como já sabiamos, o nome do tipo do valor `'Hello World'`.