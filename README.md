# p3: Processador Parlamentar Português

Ferramentas de análise aos dados abertos do Parlamento português,
sobretudo focadas na criação de formatos facilmente utilizáveis a
partir dos formatos oficiais.

## Porquê?

Os formatos oficiais podem ser usados de forma directa por
programadores, mas muitas vezes seria útil poder carregar os dados de
votações de forma mais simples. Um exemplo é a facilidade com que se
podem utilizar dados em formato CVS numa folha de cálculo.

## Objectivos e princípios

Os formatos oficiais contêm toda a informação que é produzida, sendo
que na conversão é sempre necessário proceder a escolhas do que é
incluído, bem como limpeza e tratamento dos dados. O objectivo
principal é ser fiel aos dados oficiais, transformando-os em formatos
alternativos - nomeadamenet tabulares - que simplifiquem a sua
utilização.

A separação do processo de extracção/transformação dos dados das
análises visuais que são possíveis temc omo objectivo produzir dados
de referência que possam ser usados por múltiplas soluções, sendo que
as melhorias neste processo inicial beneficiam todos os utilizadores.

A autonomização do processo permite também simplificar a utilização de
mecanismos de CI/CD, de forma a automatizar a actualização dos dados.

## Contexto

O processo de obtenção e limpeza dos dados, com todas as nuances e
ajustes necessários, foi [desenvolvido no âmbito do trabalho inicial
de análsie ás votações
parlamentares](https://fsmunoz.github.io/parlamento/html/actual.html),
tendo sido continaumente melhorado para incluir actividades,
iniciativas, Orçamentos de Estado. Este repositório é fundamentalmente
a reutilização desse código para a sua utilização de forma autónoma.


## Como citar.

O código pode ser reutilizado nos termos da licença. A utilização dos
dados resultantes do processamento podem ser citados da seguinte forma:

```
p3: dados da actividade parlamentar, Frederico Muñoz.
```

A citação dos dados utilizados não é apenas uma questão de indicação
da fonte: apesar dos dados base serem os oficiais, são efectuadas
transformações, selecções, e ajustes vários. Todos estes passos tornam
a informação mais simples de utilizar, mas resultam num conjunto de
dados com diferenças do inicial, que é importante identificar para
possibilitar a validação dos mesmos.
