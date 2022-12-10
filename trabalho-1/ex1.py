#FUNÇÕES

class Calculadora:
  def __init__(self,n1,n2):
    self.n1=n1
    self.n2=n2


  def soma(self):
    sm = self.n1 + self.n2
    print(f'O resultado da sua soma é: {sm}')

  def subtracao(self):
    sm = self.n1 - self.n2
    print(f'O resultado da sua subtração é: {sm}')

  def multiplicacao(self):
    sm = self.n1 * self.n2
    print(f'O resultado da sua multiplicação é: {sm}')

  def divisao(self):
    sm = self.n1/self.n2
    print(f'O resultado da sua divisão é: {sm}')

  def exp(self):
    sm = self.n1**self.n2
    print(f'O resultado da sua exponenciação é: {sm}')

  def mod(self):
    sm = self.n1 % self.n2
    print(f'O resultado do modulo é: {sm}')


def borda(s1,s2,s3,s4,s5,s6,s7): #FUNÇÃO GENERICA SO PARA APLICAR UMA BORDA NAS OPERAÇÕES
  tam = len(s3)
  if tam:
    print('+','-' * tam, '+')
    print('|', s1, '        |')
    print('|', s2, '   |')
    print('|', s3, '|')
    print('|', s4, '      |')
    print('|', s5, '|')
    print('|', s6, '       |')
    print('|', s7, '         |')
    print('+', '-' * tam, '+')


# PROGRAMA PRINCIPAL

while True:
  print('+',2*'-', 'Calculadora',2*'-','+') 
  borda('SOMA (+) ','SUBTRAÇÃO (-) ','MULTIPLICAÇÃO (*)', 'DIVISÃO (/)', 'EXPONENCIAÇÃO (^)',  'MÓDULO (%)', 'SAIR (.)')
   

  s1 = input('Por favor selecione a opção desejada \n >> ') 
  if s1 == '+':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.soma()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break


  if s1 == '-':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.subtracao()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break

  if s1 == '*':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.multiplicacao()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break
  if s1 == '/':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.divisao()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break
  if s1 == '^':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.exp()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break
  if s1 == '%':
    s2 = Calculadora(n1 = int(input('DIGITE UM NÚMERO:')), n2 = int(input('DIGITE OUTRO NÚMERO:')))
    s2.mod()
    op = input('Deseja voltar ao menu principal? \n 1 - SIM \n 2 - NÃO \n >> ')
    if op == '1':
      continue
    elif op == '2':
      print('Obrigado por utilizar nosso programa!')
      break

  if s1 == '.':
    print('Obrigado por utilizar nosso programa!')
    break