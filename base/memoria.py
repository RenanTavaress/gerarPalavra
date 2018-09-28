import gerador.palavra

def escreverTxt():
    gerador.palavra.sortear
    for renan in teste:

        arq = open('/home/renan/programaAvanca3/base/basePalavras.txt', 'w')
        arq.writelines(teste)
        arq.close()
    