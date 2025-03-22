#Tabuada de um número
#Peça um número ao usuário e mostre a tabuada desse número de 1 a 10.

number = int((input("Digite o número e aparecerá a tabuada do número digitado:")))

print("Tabuada do", number)

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")
