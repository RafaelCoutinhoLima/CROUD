lista_datas = []
lista_tipos = []
lista_duração = []
lista_movimentos = []

def carregar_treinos():
    global lista_datas, lista_tipos, lista_duração, lista_movimentos
    lista_datas.clear()
    lista_tipos.clear()
    lista_duração.clear()
    lista_movimentos.clear()
    
    try:
        with open('treinos.txt', 'r', encoding='utf-8') as arquivo:
            treinos = arquivo.readlines()
            for linha in treinos:
                try:
                    data = linha.split(' | Tipo: ')[0].replace('Data: ', '').strip()
                    resto = linha.split(' | Tipo: ')[1]
                    tipo = resto.split(' | Duração: ')[0].strip()
                    resto = resto.split(' | Duração: ')[1]
                    duração = resto.split(' | Exercícios: ')[0].strip()
                    movimentos = resto.split(' | Exercícios: ')[1].strip()
                    
                    lista_datas.append(data)
                    lista_tipos.append(tipo)
                    lista_duração.append(duração)
                    lista_movimentos.append(movimentos)
                except IndexError:
                    continue
    except FileNotFoundError:
        pass
def menu_principal():    
        print("\n---WOD Tracker---\n")
        print(" 1. Criar treino")
        print(" 2. Excluir treino")
        print(" 3. Visualizar treinos")
        print(" 4. Editar treino")
        print(" 5. Filtrar treinos")
        print(" 6. Adicionar metas")
        print(" 7. Ler metas")
        print(" 8. Sugestões de treino aleatórias")
        print(" 9. Análise de desempenho")
        print("10. Sair")
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
                linha = f'Data: {data} | Tipo: {tipo} | Duração: {duração} | Exercícios: {movimentos}\n'
                arquivo.write(linha)
        print(f'Treino do dia {data} adicionado com sucesso!')
def excluir_treino():
        with open('treinos.txt', 'r', encoding='utf-8') as arquivo:
            treinos = arquivo.readlines()
        
        if not treinos:
            print('Não existem treinos cadastrados.')
            return
        
        visualizar_treino()
        escolha = int(input('Digite o número do treino que você quer excluir: '))
        if 1 <= escolha <= len(treinos):
                indice = escolha - 1
                linha_excluida = treinos[indice]
                try:
                    data_excluida = linha_excluida.split(' Tipo: ')[0].replace('Data: ', '').strip()
                except IndexError:
                    data_excluida = "desconhecida"
                
                treinos.pop(indice)
                if len(lista_datas) > indice:
                    lista_datas.pop(indice)
                    lista_tipos.pop(indice)
                    lista_duração.pop(indice)
                    lista_movimentos.pop(indice)

                with open('treinos.txt', 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(treinos)
                
                print(f'Treino do dia {data_excluida} excluído com sucesso!')
def visualizar_treino():
        with open('treinos.txt', 'r', encoding='utf-8') as arquivo:     
                treinos = arquivo.readlines()
                if not treinos:
                        print('Não existem treinos cadastrados.')
                        return
                for i in range(len(treinos)):
                        print(f'{i+1}. {treinos[i]}')
def editar_treino():
    with open('treinos.txt', 'r', encoding='utf-8') as arquivo:
        treinos = arquivo.readlines()
    
    if not treinos:
        print('Não existem treinos cadastrados.')
        return
    
    visualizar_treino()
    try:
        escolha = int(input('Digite o número do treino que você quer editar: '))
        if 1 <= escolha <= len(treinos):
            indice = escolha - 1
            linha_antiga = treinos[indice]
            try:
                data_antiga = linha_antiga.split(' Tipo: ')[0].replace('Data: ', '').strip()
                resto = linha_antiga.split(' Tipo: ')[1]
                tipo_antigo = resto.split(' Duração: ')[0].strip()
                resto = resto.split(' Duração: ')[1]
                duração_antiga = resto.split(' Exercícios: ')[0].strip()
                movimentos_antigos = resto.split(' Exercícios: ')[1].strip()
            except IndexError:
                data_antiga = tipo_antigo = duração_antiga = movimentos_antigos = "desconhecido"
            
            nova_data = input(f'Digite a nova data (anterior: {data_antiga}) ou pressione Enter para manter: ').strip()
            novo_tipo = input(f'Digite o novo tipo de treino (AMRAP, EMOM, For Time) ou pressione Enter para manter: ').strip()
            nova_duração = input(f'Digite a nova duração do treino (Ex: 30 minutos) ou pressione Enter para manter: ').strip()
            novos_movimentos = input(f'Digite os novos movimentos do treino (anterior: {movimentos_antigos}) ou pressione Enter para manter: ').strip()
            
            nova_data = nova_data or (data_antiga if data_antiga != "desconhecido" else "")
            novo_tipo = novo_tipo or (tipo_antigo if tipo_antigo != "desconhecido" else "")
            nova_duração = nova_duração or (duração_antiga if duração_antiga != "desconhecido" else "")
            novos_movimentos = novos_movimentos or (movimentos_antigos if movimentos_antigos != "desconhecido" else "")
            
            nova_linha = f'Data: {nova_data} | Tipo: {novo_tipo} | Duração: {nova_duração} | Exercícios: {novos_movimentos}\n'
            treinos[indice] = nova_linha
            
            if len(lista_datas) > indice:
                lista_datas[indice] = nova_data
                lista_tipos[indice] = novo_tipo
                lista_duração[indice] = nova_duração
                lista_movimentos[indice] = novos_movimentos
            else:
                lista_datas.append(nova_data)
                lista_tipos.append(novo_tipo)
                lista_duração.append(nova_duração)
                lista_movimentos.append(novos_movimentos)
            
            with open('treinos.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(treinos)
            
            print(f'Treino do dia {nova_data or data_antiga} editado com sucesso!')
        else:
            print('Número de treino inválido.')
    except ValueError:
        print('Por favor, digite um número válido.')
def filtrar_treino():
    if not lista_datas:
        print("Nenhum treino carregado. Use a opção de visualizar ou criar treinos primeiro.")
        return

    print("\n--- Filtrar Treinos ---")
    print("1. Por data")
    print("2. Por tipo")
    print("3. Por duração")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data = input("Digite a data (DD/MM/AA): ").strip()
        encontrados = [
            (i, lista_datas[i], lista_tipos[i], lista_duração[i], lista_movimentos[i])
            for i in range(len(lista_datas)) if lista_datas[i] == data
        ]
    elif opcao == "2":
        tipo = input("Digite o tipo (AMRAP, EMOM, For Time): ").strip().lower()
        encontrados = [
            (i, lista_datas[i], lista_tipos[i], lista_duração[i], lista_movimentos[i])
            for i in range(len(lista_tipos)) if lista_tipos[i].lower() == tipo
        ]
    elif opcao == "3":
        duracao = input("Digite a duração exata (ex: 30 minutos): ").strip()
        encontrados = [
            (i, lista_datas[i], lista_tipos[i], lista_duração[i], lista_movimentos[i])
            for i in range(len(lista_duração)) if lista_duração[i] == duracao
        ]
    else:
        print("Opção inválida.")
        return

    if encontrados:
        print("\nTreinos encontrados:")
        for i, data, tipo, duracao, movimentos in encontrados:
            print(f"{i+1}. Data: {data} | Tipo: {tipo} | Duração: {duracao} | Exercícios: {movimentos}")
    else:
        print("Nenhum treino encontrado com esse critério.")
        return
def adicionar_meta():
    metas = input('Digite a meta: ')
    data = (input('Digite a data da meta: '))

    with open('metas.txt', 'a', encoding='utf-8') as arquivo:
        linha = f'Data: {data} | Meta: {metas}'
        arquivo.write(linha)
    print(f'Meta para {data} adicionada com sucesso!')
def visualizar_metas(): 
    try:
        with open('metas.txt', 'r', encoding='utf-8') as arquivo:
            metas = arquivo.readlines()
            if not metas:
                        print('Não existem metas cadastradas.')
                        return
            for i in range(len(metas)):
                    print(f'\n{i+1}. {metas[i]}')

    except FileNotFoundError:
        print('Arquivo inexistente!')    
def sugestao_treino():
        import random
        tipos = ["AMRAP", "EMOM", "For Time"]
        movimentos=["Push-up", "Pull-up", "Burpee", "Thruster", "Clean", "Snatch", "Air squat", "Deadlift"]
        tipo=random.choice(tipos)
        tempo_duração=random.randint(10,60)
        sugestão_movimento=random.sample(movimentos,4)
        print(f'\n{20*'-'}Treino aleatório gerado.{20*'-'}\n')
        print(f'Tipo: {tipo}')
        print(f'Duração: {tempo_duração} minutos.') 
        print('Movimentos:',end=' ')
        print(*sugestão_movimento,sep=', ')       
def analise_de_desempenho():
        return
