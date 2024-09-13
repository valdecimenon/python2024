#notas.py


print('#### Controle de Notas Escolares #####')

#lista vazia

nome = input('Nome do aluno:')
notas = []
quant = int(input('Digite a quantidade de notas:')) #ex: 4

for x in range(quant):  #range = 0,1,2,3
    notas.append(int(input(f'Digite a {x+1}a nota: ')))
    
print(notas)

media = sum(notas) / len(notas)  #4

#operador ternário
print('Passou' if media >= 7 else 'Reprovou')
print(f'A média foi {media:.1f}')
print('A maior nota é %.1f' % max(notas))
print('A menor nota é %.1f' % min(notas))

arquivo = 'D:/curso python agosto/Aula 02/notas.csv'
#abre arquivo para gravação
arq = open(arquivo, 'w')  #'w'rite,'a'ppend, 'r'ead

#Cabeçalho da tabela
print('NOME','NOTA1','NOTA2','NOTA3','NOTA4','MEDIA',sep=';',file=arq)
print(f'{nome};', end='', file=arq)

#Dados da tabela
for x in range(quant):
    print(f'{notas[x]:.1f};', end='', file=arq)

print(f'{media}', file=arq)

#fecha o arquivo
arq.close()



