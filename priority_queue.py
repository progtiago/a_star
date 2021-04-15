class PriorityQueue:

    def __init__(self, priority_asc=True):
        """
        :param priority_asc: define a regra de priorização.
            Caso True(default), quanto maior o valor de prioridade, mais prioritário será o elemento;
            Caso False, quanto menor o valor de prioridade, mais prioritário será o elemento.
        """
        self.queue = []
        self.priority_asc = priority_asc

    def __str__(self):
        return '\n'.join([f'priority: {i[0]} - data: {i[1]}' for i in self.queue])

    def push(self, priority, data):
        """
        Adiciona um elemento à queue
        :param priority: grau de prioridade do elemento na queue.
        :param data: elemento a ser adicionado
        """
        self.queue.append((priority, data))
        self.queue.sort(key=lambda element: element[0], reverse=self.priority_asc is True)

    def pop(self, show_priority=False):
        """
        Retorna o elemento prioritário removendo-o da queue
        :param show_priority:
            Caso True retornará uma Tupla contendo duas posições (0: prioridade, 1: valor);
            Caso False retornará apenas o valor.
        :return: o elemento prioritário
        """
        try:
            element = self.queue[0]
            del self.queue[0]
            return element if show_priority is True else element[1]
        except IndexError:
            return None

