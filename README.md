# A*

Resolução do problema proposto por Stuart Russel e Perter Norvig na terceira edição do livro Inteligência Artifical utilizando o algoritmo A\*.

*Essa implementação faz parte da lista de exercícios proposta pelo curso de Pós Graduação em Inteligência Artificial da UFPR.*

## O problema

Abaixo temos uma representação gráfica do mapa da Romênia com suas cidades representadas pelos pontos. Os pontos estão ligadas por linhas que representam as estradas disponíveis com suas respectivas distâncias.

<img width="779" alt="image" src="https://user-images.githubusercontent.com/595044/114813780-329a8580-9d89-11eb-836a-b2fe2552b20f.png">

Dadas as cidades A e B, como escolher o menor deslocamento possível?


## A solução

A busca A\* (lê-se A estrela) é um tipo de busca heurística que tenta localizar o menor caminho a partir da combinação de g(n), o custo para alcançar o nó, e h(n), o custo para ir do nó atual ao objetivo:

*f(n) = g(n) + h(n)*

Nesse caso o valor de h(n) é estimado e corresponde a distância em linha reta (hdlr) entre o nó e Bucharest. Os valores de hdlr estão presentes na tabela abaixo:

**Para exemplificar, consideremos o exercício proposto onde queremos partir de Lugoj com destino a Bucharest.**

Partindo do nosso ponto inicial teremos duas ramificações possíveis:

1. Mehadia
2. Timisoara

Para calcular f(n) do ponto Mehadia teremos:

*f(mehadia) = 70 + 241 = 311*, onde 70 é distância gasta entre o ponto inicial e Mehadia e 241 é a distância aproximada entre Mehadia e Bucharest.

Para calcular f(n) do ponto Timisoara teremos:

*f(timisoara) = 111 + 329 = 440*, onde 111 é distância gasta entre o ponto inicial e Timisoara e 329 é a  distância aproximada entre Timisoara e Bucharest.

O algoritmo A\* faz uso de uma fila de prioridades. Uma vez inseridas as duas alternativas de rota na fila de prioridades, teremos como rota prioritária a de menor custo f(n), logo, Mehadia. Analisaremos as ramificações de Mehadia, da mesma forma como fizemos com o ponto inicial, e seguiremos até chegarmos no ponto final com o menor custo possível.

A imagem abaixo simula o passo a passo utilizado pelo algoritmo A\* para achar a melhor rota.



