def escala(composicao):
    tons_principais_a_menor = {'A', 'D', 'E'}
    tons_principais_c_maior = {'C', 'F', 'G'}

    contagem_a_menor = 0
    contagem_c_maior = 0

    medidas = composicao.split('|')


    for medida in medidas:
        tom_acentuado = medida[0]

        if tom_acentuado in tons_principais_a_menor:
            contagem_a_menor += 1
        elif tom_acentuado in tons_principais_c_maior:
            contagem_c_maior += 1


    if contagem_a_menor > contagem_c_maior:
        return 'A-mol'
    elif contagem_c_maior > contagem_a_menor:
        return 'C-dur'
    else:
        ultimo_tom = composicao[-1]
        if ultimo_tom in tons_principais_a_menor:
            return 'A-mol'
        elif ultimo_tom in tons_principais_c_maior:
            return 'C-dur'


composicao = input().strip()


resultado = escala(composicao)
print(resultado)
