import dists
from priority_queue import PriorityQueue
from city import City


# goal sempre será 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até
    goal segundo o algoritmo A*
    """

    # Cria uma fila prioritária onde os primeiros elementos sempre serão as possibilidades de rota mais curtas.
    queue = PriorityQueue(priority_asc=False)

    # Instancia o ponto de partida utilizando a estrutura City.
    start_city = City(start)

    # Adiciona o ponto de partida à fila prioritária.
    # Como o grau de prioridade não foi informado, será considerado O.
    queue.push(start_city.get_estimated_total_cost(), start_city)

    # Obtém-se a cidade com maior prioridade de ser expandida, que nesse momento ainda é o ponto inicial.
    city = queue.pop()

    # Enquanto a cidade prioritária não for o destino, continuaremos no laço.
    while city.is_name(goal) is False:
        # Expande as próximas cidades a partir da cidade atual.
        for next_city in dists.dists[city.name]:
            # Cria um novo ponto a partir do nome da próxima cidade, do custo de locomoção e da rota feita até aqui.
            new_city = City(name=next_city[0], cost=next_city[1], route_made=city.route_made)
            # Adiciona o ponto à fila prioritária dando o custo estimado até o destino como grau de prioridade.
            queue.push(new_city.get_estimated_total_cost(), new_city)

        # Atualiza a cidade a ser analisada pela próxima iteração.
        city = queue.pop()

    # Retorna uma lista contendo a melhor rota
    return [p.name for p in city.route_made]


origin = 'Lugoj'
better_route = a_star(origin)
print(f'The best route from {origin} to Bucharest is: {" -> ".join(better_route)}.')

