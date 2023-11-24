tasks_list = []

while True:
    print("""\nMENU DE OPÇÕES\n
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
            
        case 2:
            task_id = int(input("Informe o ID da tarefa: "))

            #verificar se tarefa existe            
            is_in_list = False
            i = 0

            while (is_in_list == False) and (i < len(tasks_list)):
                if (task_id == list(tasks_list[i].values())[0]):
                    is_in_list = True
                    #existindo, sinalizar que foi concluída
                    tasks_list[i]['check'] = True

                    #removendo item da lista e adicionando-o ao início
                    removed_task = tasks_list.pop(i)
                    tasks_list.insert(0, removed_task)
                i += 1
            
            if (is_in_list):
                print("Tarefa alterada com sucesso!")
            else:
                print("Essa tarefa não existe.")          
            
        case 3:
            task_id = int(input("Informe o ID da tarefa: "))

            #verificar se tarefa existe            
            is_in_list = False
            i = 0

            while (is_in_list == False) and (i < len(tasks_list)):
                if (task_id == list(tasks_list[i].values())[0]):
                    description = input("Informe a nova descrição da tarefa: ").capitalize().strip()
                    tasks_list[i]['description'] = description
                    is_in_list = True
                i += 1
            
            if (is_in_list):
                print("Tarefa editada com sucesso!")
            else:
                print("Essa tarefa não existe.")  
            
        case 4:
            for task in tasks_list:
                task = (f"{task['id']}. {task['description']} {('[x]' if task['check'] else '[]')}") 
                
                print(task)
            
        case 0:
            print('Fim do programa!')
            break
            
        case _:
            print('Insira um número entre 0 e 4.')