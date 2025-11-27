fila = []
while True:
    print("menu")
    print(" 1-  adicionar tarefas ")
    print(" 2-  adicionar tarefas ")
    print(" 3-  adicionar tarefas ")
    op= int(input("escolha uma opção:"))
    if op==1:
        nome= input("digite um nome")
        fila.append(nome)
        print("nome adicionado")
    elif op==2:
        print("mostrando fila:", fila)
    elif op==3:
        print("saindo")
        break
    else:
        print("opcap invalida")