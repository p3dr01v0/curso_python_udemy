from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

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


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('lavar roupa', datetime.now())
    casa.add('passar roupa')
    casa.add('lavar pratos')
    casa.add('lavar banheiro')
    print(casa)

    casa.procurar('lavar roupa').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    print('\n')
    mercado = Projeto('Compras no mercado')
    mercado.add('carne', datetime.now() +
                timedelta(days=3))
    mercado.add('frango')
    mercado.add('tomate')
    mercado.add('alface')
    print(mercado)

    mercado.procurar('carne').concluir()
    mercado.procurar('frango').concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


# def hora():
#     data = datetime.now() - timedelta(days=1)
#     return print(data)


if __name__ == '__main__':
    main()
    # print(datetime.now())
    # hora()
