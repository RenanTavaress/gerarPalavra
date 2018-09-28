import random



def sortear(quantidade):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vogais = ["a", "e", "i", "o", "u"]

    teste = []
    contQuantidade =1


    while(True):
        letra1 = random.choice(alfabeto)
        letra2 = random.choice(alfabeto)
        letra3 = random.choice(alfabeto)
        letra4 = random.choice(alfabeto)

        if((not(letra1 in vogais) and (letra2 in vogais)) and  (not(letra3 in vogais) and (letra4 in vogais))):
            palavraSorteada = letra1 + letra2 + letra3 + letra4
            teste.append(palavraSorteada)
        
            if(contQuantidade < quantidade):
                contQuantidade = contQuantidade +1
            else:  
                print(teste)  
                break
            

    


#sortear(quantidade)