texto = input()
feliz = ":-)"
contagem_feliz = texto.count(feliz)
triste = ":-("
contagem_triste = texto.count(triste)

if contagem_feliz == contagem_triste and contagem_feliz > 0 and contagem_triste > 0:
    print("unsure")
elif contagem_feliz == 0 and contagem_triste == 0:
    print("none")
elif contagem_feliz > contagem_triste:
    print("happy")
else:
    print("sad")
