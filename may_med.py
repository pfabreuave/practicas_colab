"""
Escreva um programa para calcular a média de 3 alunos e imprimir “Parabéns 
<nome do aluno>!” para os alunos que tiveram a nota maior que a média
● Ler os nomes e as notas de 3 alunos 
● Calcular a média da turma 
● Listar os alunos que tiveram nota acima da média

"""

# variáveis
media = 0
alunos = int(input("quantos alunos são: "  ))
nota = 2
# Criar e inicializar lista
aluno_nota = [([0]*nota) for alunos in range(alunos) ]
# Ciclo para capturar os dados necessários
for i in range(alunos):
  aluno_nota[i][0] = (input("\ndigite nome do aluno " + str(i + 1) + " " ))   
  aluno_nota[i][1] = (float(input("\ndigite a nota do aluno " + str(i + 1) + " " )))
  media = aluno_nota[i][1] + media
# Ciclo para processar os dados capturados e dar resultados 
print("\n\nA MÉDIA DO GRUPO FOI: ", (media / alunos))
for i in range(alunos):
    if aluno_nota[i][1] > (media / alunos):
        print("\nparaben " + aluno_nota[i][0] + " você supera a média com " + str(aluno_nota[i][1]) + " puntos" )