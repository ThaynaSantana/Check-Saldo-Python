# criar um verificador de saldos automatico, onde ele
# ler dois arquivos txt um sistema.txt e banco.txt
# e faz o calculo das diferenças e apresenta ao usuario

# Variaveis
banco_saldos = []
sistema_saldos = []
diferencas = []
i=1
j=1
# lendo o arquivo banco.txt
with open('banco.txt') as banco:
  banco_txt = banco.read()

# removendo a quebra de linha \n e assim separando os valores
banco_txt = banco_txt.split('\n')
# armazenando num array
banco_saldos = [int(saldo) for saldo in banco_txt]
print('Lendo saldos do banco.txt ...')

with open('sistema.txt') as sistema:
  sistema_txt = sistema.read()
  
sistema_txt = sistema_txt.split('\n')
sistema_saldos = [int(saldo) for saldo in sistema_txt]

print('Lendo saldos do sistema.txt ...')

if(len(banco_saldos) == len(sistema_saldos)):
  print('[SIM - 1 ou NAO - 0]')
  opc = int(input('Fazer o calculo das diferenças entre banco e sistema?: '))
  if(opc == 1):
    # fazendo calculo
    for i in range(len(banco_saldos)):
      diferencas.append(banco_saldos[i] - sistema_saldos[i])
      i+=1
    # imprimindo na tela
    for dif in diferencas:
      print(f'SALDO #{j} - VALOR DIF R${dif}')
      j+=1
  else:
    print('Cancelado.')
else:
  print('A quantidade de saldos do banco.txt é divergente com a quantidade de saldos do sistema.txt! corrija-o!')
  
# conversor de saldos
# converte os saldos que estao na formataçao incorreta 1.000,50
# para formatação que o sistema aceita 1000.50

# criar um extrator de saldos de arquivo pdf e arquivo xls
# localiza onde esta os saldos, armazena e exportar