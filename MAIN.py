import funções
import os
os.system('cls')

while True:
    funções.menu_principal()
    escolha = int(input('Digite o que você deseja fazer (1-9): '))
    if escolha<1 or escolha>9:
        print('Escolha inválida! Digite um número de 1-9.')
    if escolha == 1:
        funções.criar_treino()
    if escolha == 2:
        funções.excluir_treino()
    if escolha == 3:
        funções.visualizar_treino()
    if escolha == 4:
        funções.editar_treino()
    if escolha == 5:
        funções.filtrar_treino()
    if escolha == 6:
        funções.adicionar_meta()
    if escolha == 7:
        funções.sugestao_treino()
    if escolha == 8:
        funções.analise_treino()
    if escolha == 9:
        break



