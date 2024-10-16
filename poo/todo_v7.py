from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    # sobrecarga de operador
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(
            tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    def pendente(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel index error
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'Projeto: {self.nome}, {len(self.pendente())} tarefas pendentes'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append(' (Concluida)')
            if self.vencimento:
                if datetime.now() >= self.vencimento:
                    status.append('(Vencida)')
                elif datetime.now() < self.vencimento:
                    dias = (self.vencimento - datetime.now()).days
                    status.append(f'(Vence em {dias} dias)')
        else:
            status.append(' (Pendente)')
        return f'{self.descricao}' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('lavar roupa', datetime.now())
    casa.add('passar roupa')
    casa.add('lavar pratos')
    casa.add('lavar banheiro')
    # modificamos mais uma vez a chamada, agora fazendo uma sobrecarga de operadores podemos chamar da seuginte forma
    # metodo antigo
    # casa.add(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    # casa.add(casa.procurar('Trocar lencois').concluir())
    # novo metodo
    casa += TarefaRecorrente('Trocar lencois', datetime.now(), 7)
    casa.procurar('Trocar lencois').concluir()
    print(casa)

    casa.procurar('lavar roupa').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    print('\n')
    mercado = Projeto('Compras no mercado')
    mercado.add('carne', datetime.now() +
                timedelta(days=3, minutes=12, seconds=10))
    mercado.add('frango')
    mercado.add('tomate')
    mercado.add('alface')
    print(mercado)

    mercado.procurar('carne').concluir()
    mercado.procurar('frango').concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
