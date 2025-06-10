def calcular_media(n1, n2, n3):
    return(n1 + n2 + n3)/3

def verificar_situacao(nota1, nota2, nota3): 
    if nota >= 7:
        print(nota,"Aluno aprovado")
    elif nota >= 5 and nota < 7:
        print(nota," Aluno de recuperação")
    elif nota < 5:
        print(nota," Aluno reprovado")
                    

def mostrar_relatorio():
    print("RELATÓRIO")
    for aluno in alunos:
        print("nome - ",f"{testes['nome']}")          
        print("media - ",f"{testes['media']}")
        print("situação - ",f"{testes['situação']}") 



alunos = []
while True:
    print("menu")
    print("")
    print("[1] - Cadastrar nome e a nota do aluno ")
    print("[2] - Alunos cadastrados ")
    print("[3] - Verificar Situação")
    print("[4] - Relatório")
    print("[5] - Sair")
    opcao = int(input("escolhe uma das opções"))
    if opcao == 1:
        nome = input("Digite o nome do aluno")
        aluno = {
            "nome": nome
            }
        if nome in alunos:
            print("Este nome já está na lista")
        else:
            alunos.append(nome)
            print("Seu nome foi adicionado com sucesso")
            
