tasks_list = []

while True:
    print("""Digite um número de 0 a 4
    1. Registrar uma nova tarefa
    2. Marcar uma tarefa como realizada
    3. Editar uma tarefa
    4. Listar as tarefas já registradas
    0. Sair do programa
    """)
    
    user_option = int(input("Sua opção: "))
    print()
    
    match user_option:
        case 1:
            description = input("Informe a descrição da tarefa: ")
            
            task_id = len(tasks_list) + 1

            tasks_list.append({'id': task_id, 
                                'description': description.capitalize().strip(),
                              'check': False})
            
            print('Tarefa registrada com sucesso!')
            print(tasks_list) #apagar
            
        case 2:
            task_id = input("Informe o ID da tarefa: ")

            #verificar se tarefa existe            
            is_in_list = False

            for task in tasks_list:
                if (task in task.values()):
                    #existindo, sinalizar que foi concluída
                    task['check'] = True
                    is_in_list = True

                    break
            
            if (is_in_list):
                print("Tarefa alterada com sucesso!")
            else:
                print("Esta tarefa não existe.")          
            
        case 3:
            print('ola')
            
        case 4:
            for task in tasks_list:
                #('impar', 'par')[x%2==0]
                task = (f"{task['id']}. {task['description']} {(['x'] if task['check'] else '[]')}") 
                
                print(task)
            
        case 0:
            print('Fim do programa!')
            break
            
        case _:
            print('Insira um número entre 0 e 4.')