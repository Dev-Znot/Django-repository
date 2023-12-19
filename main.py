tarefas = []

def Adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f'Tarefa adicionada: {tarefa}')

def Remover_tarefa(tarefa):
    try:
        tarefas.remove(tarefa)
        print(f'Tarefa removida: {tarefa}')
    except ValueError:
        print(f'Tarefa não encontrada: {tarefa}')

def Exibir_tarefas():
    if not tarefas:
        print('Não a tarefas.')
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')

while True:
    print('\n Escolha uma opção:')
    print('[1] Adicionar tarefa')
    print('[2] Remover tarefa')
    print('[3] Exibir tarefas')
    print('[4] Fechar menu')
    
    escolha_menu = int(input('Escolha uma opção:'))

    if escolha_menu == 1:
        tarefa = input('Digite a tarefa:')
        Adicionar_tarefa(tarefa)
    elif escolha_menu == 2:
        tarefa = input('Digite a tarefa a ser removida:')
        Remover_tarefa(tarefa)
    elif escolha_menu == 3:
        Exibir_tarefas()
    elif escolha_menu == 4:
        print('Saindo do aplicativo')
        break
    else:
        print('Opção invalida. Tente novamente.')

