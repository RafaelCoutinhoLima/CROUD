import funções
import os
os.system('cls')

funções.carregar_treinos()
while True:
    try:
        funções.menu_principal()
        escolha = int(input('Digite o que você deseja fazer (1-9): '))
        
        if escolha < 1 or escolha > 9:
            print('Escolha inválida! Digite um número de 1 a 9.')
            continue
        
        if escolha == 1:
            funções.criar_treino()
        elif escolha == 2:
            funções.excluir_treino()
        elif escolha == 3:
            funções.visualizar_treino()
        elif escolha == 4:
            funções.editar_treino()
        elif escolha == 5:
            funções.filtrar_treino()
        elif escolha == 6:
            funções.adicionar_meta()
        elif escolha == 7:
            funções.sugestao_treino()
        elif escolha == 8:
            funções.analise_de_desempenho()
        elif escolha == 9:
            break
    except ValueError:
        print('Digite um número válido (1-9): ')



