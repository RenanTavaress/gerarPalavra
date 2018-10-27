import gerador.Palavra
import base.memoria


def main():
    quantidade = int(input("Digite a quantidade de palavras que voce deseja sortear \n"))
    vogal = input("Digite a vogal\n")
    consoante = input("consoa")
    print(gerador.Palavra.sortear(quantidade,vogal,consoante))


if __name__ == '__main__':
    main()