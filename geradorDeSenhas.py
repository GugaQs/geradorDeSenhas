import random 

nome= input("Qual o seu nome?\n")

bemVindo = "Olá " + nome + ", bem vindo ao gerador de senhas\n"
print(bemVindo)
 

maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculo = "abcdefghijklmnopqrstuvwxyz"
simbolos = "!@#$%&*+-~^"
numeros = "1234567890"

s1 = maiuscula + minusculo + simbolos + numeros
largura = 15
senha = "".join(random.sample(s1, largura))
print("Senha gerada: " + senha)