from datetime import datetime


class Projeto:
    # construtor, passamos os parametros da classe aki, por assim dizer
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # mais um metodo magico, este nos permiti deixar o elemento 'iteravel' assim quando formos chama-lo não precisamos
    # mais usar o ponto. antes: "casa.tarefas" agora : "casa", claro precisamos especificar o elemneto na função
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        # funcao para adicionar uma tarefa ao projeto
        self.tarefas.append(Tarefa(descricao))

    def pendente(self):
        # estamos analisando todas as tarefas do projeto e vendo qual tarefa não tem o self.feito = True, caso
        # a tarefa não tenha ela vai ser retornada, essa verificação ocorre para todas as tarefas presente no projeto
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel index error]
        # função para procurarmos uma tarefa em especifico
        # o '[0] esta pegando o primeiro elemento que ele encontra com a descricao fornecida
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    # função "magica" que retorna a saida da classe como uma string
    def __str__(self):
        return f'Projeto: {self.nome}, {len(self.pendente())} tarefas pendentes'


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        # atributo para verificação da conclusão da tarefa
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        # função para validar a tarefa como feita
        self.feito = True

    def __str__(self):
        return self.descricao + ('(Concluida)' if self.feito else '')


def main():
    # passamos o nome do projeto
    casa = Projeto('Tarefas de casa')
    # fazemos uso da função de adicionar tarefas o que esta entre parenteses é o parametro 'descrção'
    casa.add('lavar roupa')
    casa.add('passar roupa')
    casa.add('lavar pratos')
    casa.add('lavar banheiro')
    print(casa)

    # estamos localizando o a descricao(tarefa) 'lavar roupa' e chamando a função concluir da classe 'Tarefa' nela
    # assim sendo considerada como concluida
    casa.procurar('lavar roupa').concluir()
    # estamos imprimindo todas as tarefas presente em casa.tarefas(self.tarefas) da classe 'Tarefa'
    for tarefa in casa:
        print(tarefa)
    print(casa)

    print('\n')
    mercado = Projeto('Compras no mercado')
    mercado.add('carne')
    mercado.add('frango')
    mercado.add('tomate')
    mercado.add('alface')
    print(mercado)

    mercado.procurar('carne').concluir()
    mercado.procurar('frango').concluir()
    for tarefa in mercado:
        print(tarefa)
    print(mercado)


if __name__ == '__main__':
    main()
