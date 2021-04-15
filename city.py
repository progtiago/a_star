import dists


class City:
    """
    Representa um ponto do mapa
    """

    def __init__(self, name, cost=0, route_made=[]):
        """
        :param name: nome da cidade
        :param cost: custo do percurso partindo da cidade anterior.
        :param route_made: lista com todas as cidades percorridas desde a cidade de partida.
        """
        self.name = name
        self.cost = cost
        self.route_made = route_made + [self]

    def get_estimated_total_cost(self):
        """
        :return: a estimativa de custo entre essa cidade e Bucharest.
        A fórmula para esse cálculo é f(n) = g(n) + h(n) onde:
            g(n) = distância percorrida desde a cidade de partida.
            h(n) = distância em linha reta entre a cidade atual e Bucharest.
        """
        return sum(point.cost for point in self.route_made) + \
               dists.straight_line_dists_from_bucharest[self.name]

    def is_name(self, name):
        """
        Verifica se o nome da cidade é o mesmo que o informado via parâmetro.
        :param name: nome da cidade a ser verificado
        :return: boolean
        """
        return self.name == name
