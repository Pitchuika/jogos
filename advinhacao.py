import random


print("********************************")
print("Bem vindo no jogo de advinhação")
print("********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("definir nivel:"))

if (nivel == 1):
    total_de_tentativas=20
elif(nivel == 2):
    total_de_tentativas=10
else:
    total_de_tentativas=5
for rodada in range (1, total_de_tentativas +1):
    print("tentativa {} de {}".format (rodada,total_de_tentativas))
    chute_str = input(" digite o seu número entre 1 e 100:")
    print("vc digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 ):
        print(" vc deve digitar um múmero entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("vc errou! O seu chute foi maior q o numero secreto.")
        elif(menor):
            print("vc errou! o seu numero foi menor que o numero secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print ("fim de jogo")