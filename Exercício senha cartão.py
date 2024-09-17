senha = 7676

pin = int(input("Digite sua senha: "))
tent = 1
while pin != senha and tent <3:
    pin = int(input(f"Senha errada,\n"
                    f" você ainda tem {3-tent} tentativas \n "
                    f"Digite sua senha novamente: "))
    tent+=1

if tent == 3 and pin != senha:
    print("Você tentou 3 vezes e errou, o login foi bloqueado!")
else:
    print("Login efetuado com sucesso")