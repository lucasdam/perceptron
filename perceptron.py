# OPERADOR 'OU'
#x1 = [0, 1, 0, 1]
#x2 = [0, 1, 1, 0]
#classe = [-1, 1, 1, 1]

# OPERADOR 'E'
#x1 = [1, 0, 1, 0]
#x2 = [1, 1, 0, 0]
#classe = [1, -1, -1, -1]

x1 = [1, 9.4, 2.5, 8, 0.5, 7.9, 7, 2.8, 1.2, 7.8]
x2 = [1, 6.4, 2.1, 7.7, 2.2, 8.4, 7, 0.8, 3, 6.1]
classe = [1, -1, 1, -1, 1, -1, -1, 1, 1, -1]
pesos =  [1,  1,  1]
VIES = 1
COEFICIENTE = 0.3


def perceptron(indice):
    print('\nÍndice:    ', indice)
    print('x1:        ', x1[indice])
    print('x2:        ', x2[indice])
    print('Classe:    ', classe[indice])
    
    somatorio = calcular_somatorio(indice)
    print('Somatório: ', round(somatorio, 3))
    
    saida = funcao_ativacao(somatorio)
    print('Saída:     ', saida)

    if saida == classe[indice]:
        print('* Valor obtido é IGUAL ao valor esperado *')
        return True
    else:
        print('* Valor obtido é DIFERENTE do valor esperado *')
        recalcular_pesos(indice, saida)
        organizar_base(indice)
        return False


def calcular_somatorio(indice):
    return x1[indice] * pesos[0] + x2[indice] * pesos[1] + VIES * pesos[2]


def funcao_ativacao(somatorio):
    return 1 if somatorio >= 0 else -1


def recalcular_pesos(indice, saida):
    print('\n* Recalculando os Pesos *')

    pesos[0] = pesos[0] + (COEFICIENTE * (classe[indice] - saida) * x1[indice])
    pesos[1] = pesos[1] + (COEFICIENTE * (classe[indice] - saida) * x2[indice])
    pesos[2] = pesos[2] + (COEFICIENTE * (classe[indice] - saida) * VIES      )

    print('Pesos Atuais: ', [round(x, 3) for x in pesos], '\n')


def organizar_base(indice):
    print('* Ordenando as Listas *')
    
    a = x1[indice]
    b = x2[indice]
    c = classe[indice]

    del x1[indice]
    del x2[indice]
    del classe[indice]

    x1.insert(0, a)
    x2.insert(0, b)
    classe.insert(0, c)

    print('Lista x1: ', x1)
    print('Lista x2: ', x2, '\n')
    print('=======================================================')


def main():
    print('\n===============================================================')
    print('Primeira Entrada: ', x1)
    print('Segunda Entrada:  ', x2)
    print('Classe: ', classe)
    print('Pesos Iniciais: ', pesos)
    print('Viés: ', VIES)
    print('Coeficiente de Entrada: ', COEFICIENTE)
    print('===============================================================\n')

    indice = 0
    while indice < len(x1):
        if perceptron(indice):
            indice += 1
        else:
            indice = 0

    print('\n\nPesos Finais: ', [round(x, 3) for x in pesos], '\n')


if __name__ == "__main__":
    main()