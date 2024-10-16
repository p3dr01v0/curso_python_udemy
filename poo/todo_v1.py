from datetime import datetime


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
    # como a tarefa é um parametro da classe e vamos ter mais que uma tarefa, fazemos da forma abixo
    casa = []
    casa.append(Tarefa('lavar roupas'))
    casa.append(Tarefa('lavar banheiro'))
    casa.append(Tarefa('lavar janelas'))

    # estamos executando a função concluir somente para a tarefa 'lavar janelas', fazemos isso com um for
    # que verfica todas as descricoes da lista 'casa' caso alguma seja igual a especificada o codigo é rodado
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'lavar janelas']
    for tarefa in casa:
        print(tarefa)


if __name__ == '__main__':
    main()
