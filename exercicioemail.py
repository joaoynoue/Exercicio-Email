#Uma pessoa digitará o nome completo e você deve criar o e-mail institucional dessa pessoa com
#o primeiro nome e o último sobrenome dessa pessoa.
def funcaoemail ():
    nome = str(input("Digite Seu Nome Completo: "))

    nome = nome.split()

    print(f'Email Gerado: {nome[0]}{nome[1]}@gmail.com.br')

funcaoemail()