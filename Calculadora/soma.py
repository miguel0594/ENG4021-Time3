def somaf(n1: float, n2: float) -> float:
    '''
    Função que retorna a soma de dois números (inteiros ou reais).

    :param n1: número 1 (int ou float)
    :param n2: número 2 (int ou float)
    :return: soma de n1 e n2 (float)

    Exemplo:
    >>> somaf(2, 3)
    5
    >>> somaf(2.5, 3.7)
    6.2
    '''
    return n1 + n2


def main():
    assert somaf(2, 3) == 5, "Erro: 2 + 3 deveria ser 5"
    assert somaf(2.5, 3.7) == 6.2, "Erro: 2.5 + 3.7 deveria ser 6.2"
    assert somaf(-1.5, 4.5) == 3.0, "Erro: -1.5 + 4.5 deveria ser 3.0"
    assert somaf(0, 5) == 5, "Erro: 0 + 5 deveria ser 5"
    assert somaf(5, 0) == 5, "Erro: 5 + 0 deveria ser 5"
    assert somaf(1.1, 1.1) == 2.2, "Erro: 1.1 + 1.1 deveria ser 2.2"
    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()
