import gerador.palavra
import base.memoria


def main():
    quantidade = int(input("Digite a quantidade de palavras que voce deseja sortear \n"))
    print(gerador.palavra.sortear(quantidade))


if __name__ == '__main__':
    main()