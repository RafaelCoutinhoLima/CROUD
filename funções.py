lista_datas = []
lista_tipos = []
lista_duração = []
lista_movimentos = []

def menu_principal():    
        print("---WOD Tracker---")
        print("1. Criar treino")
        print("2. Excluir treino")
        print("3. Visualizar treinos")
        print("4. Editar treino")
        print("5. Filtrar treinos")
        print("6. Adicionar metas")
        print("7. Sugestões de treino aleatórias")
        print("8. Análise de treino")
        print("9. Sair")

def criar_treino():
        data = input('Digite a data data do treino (DD/MM/AA): ')
        tipo = input('Digite o tipo do treino (AMRAP, EMOM, For Time): ')
        duração = input('Digite a duração do treino em minutos (Ex: 30 minutos): ')
        movimentos = input('Digite os exercícios realizados no treino: ')

        lista_datas.append(data)
        lista_tipos.append(tipo)
        lista_duração.append(duração)
        lista_movimentos.append(movimentos)

        with open('treinos.txt', 'a', encoding='utf-8') as arquivo:
                for i in range(len(lista_datas)):
                        linha = f'Data: {lista_datas[i]} Tipo: {lista_tipos[i]} Duração: {lista_duração[i]} Exercícios: {lista_movimentos[i]}\n'
                        arquivo.write(linha)
        arquivo.close()
        print(f'Treino do dia {lista_datas[i]} adicionado com sucesso!')

def excluir_treino():
        if not lista_datas:
                print('Não existem treinos cadastrados.')
                return
        visualizar_treino()
        escolha = int(input('Digite o número do treino que você quer excluir: '))
        if escolha > 0 and escolha < len(lista_datas):
                indice = escolha - 1
                lista_datas.pop(indice)
                lista_tipos.pop(indice)
                lista_duração.pop(indice)
                lista_movimentos.pop(indice)
        print(f'Treino do dia {lista_datas[indice] - 1} excluído com sucesso!')

        
def visualizar_treino():
        with open('treinos.txt', 'r', encoding='utf-8') as arquivo:     
                treinos = arquivo.readlines()

                if not treinos:
                        print('Não existem treinos cadastrados.')
                        return
                for i in range(len(treinos)):
                        print(f'{i+1}.{treinos[i]}')
                arquivo.close()
    
def editar_treino():
        return
def filtrar_treino():
        return
def adicionar_meta():
        return
def sugestao_treino():
        return
def analise_treino():
        return
