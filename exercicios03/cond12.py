a = int(input("Digite um número inteiro:"))

if a % 2 == 0 and a < 100:
    print("O número é par e menor que 100")
elif a%2==0 and a >= 100:
    print("O número é par e maior ou igual a 100")

if a % 2 == 1 and a < 100:
    print("O número é ímpar e menor que 100")
elif a % 2 == 1 and a > 100:
    print("O número é ímpar e maior que 100")