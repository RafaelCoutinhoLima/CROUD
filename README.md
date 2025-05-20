# 🏋️‍♂️ WOD Tracker

WOD Tracker é uma aplicação em Python para registrar, visualizar e analisar treinos do tipo Workout of the Day. Ideal para praticantes de CrossFit ou treinos funcionais.

## ✅ Funcionalidades
- Criar, visualizar, editar e excluir treinos
- Filtrar treinos por data, tipo ou duração
- Registrar e visualizar metas
- Gerar sugestões aleatórias de treinos
- Analisar desempenho com base nos treinos realizados

## ▶️ Como usar
1. Certifique-se de ter o **Python 3.10** ou superior instalado.
2. Instale as dependências (se houver um arquivo requirements.txt):

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script principal:

    ```bash
    python nome_do_arquivo.py
    ```

4. Siga as instruções do menu para navegar entre as opções.

## 💡 Exemplo de uso
text
Copiar
Editar
---WOD Tracker---

 1. Criar treino
 2. Excluir treino
 3. Visualizar treinos
 4. Editar treino
 5. Filtrar treinos
 6. Adicionar metas
 7. Ler metas
 8. Sugestões de treino aleatórias
 9. Análise de desempenho
10. Sair

Digite o que você deseja fazer (1-10): 1

Digite a data do treino (DD/MM/AA): 20/05/25  
Digite o tipo do treino (AMRAP, EMOM, For Time): EMOM  
Digite a duração do treino em minutos (Ex: 30 minutos): 20 minutos  
Digite os exercícios realizados no treino: Burpee, Push-up, Air Squat  

Treino do dia 20/05/25 adicionado com sucesso!


💼 Estrutura de Arquivos
WOD-Tracker/
-main.py               # Script principal com o menu e chamadas de funções

-funções.py            # Lógica das funcionalidades do programa

-treinos.txt           # Armazena os treinos cadastrados

-metas.txt             # Armazena as metas inseridas

-README.md             # Documentação do projeto

📄 Licença
Este projeto é disponibilizado exclusivamente para fins de aprendizado, uso técnico ou acadêmico.
Não deve ser utilizado em ambientes comerciais sem permissão do autor.
