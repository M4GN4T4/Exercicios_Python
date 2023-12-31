from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        cabeçalho("PESSOAS CADASTRADAS")
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome:"))
        idade = leiaint("Idade:")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[0;31mERRO: Digite uma opção válida!\033[m")
        sleep(2)