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

## Contento

O processo de obtenção e limpeza dos dados, com todas as nuances e
ajustes necessários, foi [desenvolvido no âmbito do trabalho inicial
de análsie ás votações
parlamentares](https://fsmunoz.github.io/parlamento/html/actual.html),
tendo sido continaumente melhorado para incluir actividades,
iniciativas, Orçamentos de Estado. Este repositório é fundamentalmente
a reutilização desse código para a sua utilização de forma autónoma.
