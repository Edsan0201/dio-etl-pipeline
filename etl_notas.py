#Extraindo dados da tabela notas.csv

import csv
tabela =  open('notas.csv')
notas = csv.reader (tabela)

# Transformação de dados

tabela = list ()

for nota in notas:

    if nota [4] == 'media':
       nota.append('status')
       tabela.append(nota)

    elif nota [4] == '5':
        nota.append ('Xiii... Nao sou capaz de opinar...')
        tabela.append (nota)
    
    elif nota [4] < '5':
        nota.append ('Que pena! Estuda mais um pouco, vai...')
        tabela.append (nota)

    elif nota [4] > '5':
        nota.append ('Ai sim! Muito bem!')
        tabela.append (nota)

  
# Carregando novas informações

nova_tabela =  open('status.csv', 'w', newline='')
status = csv.writer(nova_tabela, delimiter=',')
status.writerows(tabela)

