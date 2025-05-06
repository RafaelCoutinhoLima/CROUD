def menu_principal():    
        print("---WOD Tracker---")
        print("1. Criar treino")
        print("2. Excluir treino")
        print("3. Vizualizar treinos")
        print("4. Editar treino")
        print("5. Filtrar treinos")
        print("6. Adicionar metas")
        print("7. Sugestões de treino aleatórias")
        print("8. Análise de treino")
        print("9. Sair")

def criar_treino():
        lista_datas = []
        lista_tipos = []
        lista_duração = []
        lista_movimentos = []

        data = input('Digite a data data do treino (DD/MM/AA): ')
        tipo = input('Digite o tipo do treino (AMRAP, EMOM, For Time): ')
        duração = input('Digite a duração do treino em minutos (Ex: 30 minutos): ')
        movimentos = input('Digite os exercícios realizados no treino: ')

        lista_datas.append(data)
        lista_tipos.append(tipo)
        lista_duração.append(duração)
        lista_movimentos.append(movimentos)

        with open('treinos.txt', 'w', encoding='utf-8') as arquivo:
                for i in range(len(lista_datas)):
                        linha = f'Data: {lista_datas[i]} Tipo: {lista_tipos[i]} Duração: {lista_duração[i]} Exercícios: {lista_movimentos[i]}'
                        arquivo.write(linha)
                        arquivo.close()



