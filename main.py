#----------------------Exercício 01-------------------------#
print('-' * 45)
print('\t----Tabuada----')
numero = int(input('Informe o número para ver a tabuada: '))

print('\nTabuada de',numero,':')

for i in range(1,11):
  print(f"{numero} X {i} = {numero * i}")
print('\n')
#----------------------Exercício 02-------------------------#
print('-' * 45)
print('\t----Cálculo do novo salário----')
salario_atual = float(input('Informe o salário atual: ').replace(',','.'))

if (salario_atual<500):
  salario_novo = salario_atual+(salario_atual*0.15)
  print('Salário com reajuste = {:.2f}'.format(salario_novo))

if ((salario_atual>=500) and (salario_atual <=1000)):
  salario_novo = salario_atual+(salario_atual*0.10)
  print('Salário com reajuste = {:.2f} '.format(salario_novo))

if (salario_atual>1000):
  salario_novo = salario_atual+(salario_atual*0.5)
  print('Salário com reajuste = {:.2f} '.format(salario_novo))
print('\n')
#----------------------Exercício 03-------------------------#
print('-' * 45)
print('\t--Números entre 5 e 100 que são divisíveis por 7--')
for num in range(5,100):
  if(num % 7 == 0 and num % 5 != 0):
    print(num)
print('\n')
#----------------------Exercício 04-------------------------#
print('-' * 50)
print('\t----Soma de 1 até o valor digitado----')
soma_numeros = 0
nuemro = int(input("Por favor, insira um número: "))
for i in range(1, numero + 1, 1):
   soma_numeros += i
print("A Soma é = {}".format(soma_numeros))
print("\n")
#----------------------Exercício 05-------------------------#
print('-' * 50)
print('\t---A Dança dos números----')
x = int(input("Informe um número para brincar: "))
if x < 0:
  print("É um número negativo!")
elif x == 0:
  print("É um número neutro!")
elif x > 0:
  print("É um número positivo!")
print("\n")
#----------------------Exercício 06-------------------------#
print('-' * 50)
print('\t----Contagem dos dígitos----')
digitos = int(input("Digite um número para contar seus dígitos: "))
contador = 0
while digitos != 0:
  digitos  //= 10
  contador += 1
print("Total de dígitos = {} ".format(contador))
print("\n")