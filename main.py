# Projecto de um meno para venda de Gelados na UMETRO
cont=1
while cont<=2*cont:
    print("\n")
    print ("*************************************************")
    print ("*\t\t\t\t\t\t*\n*\t\tMENU DE GELADOS\t\t\t*\n*\t\t\t\t\t\t*\t\t")
    print ("*************************************************")
    print("--------------------------------------------------")
    print("|Índice\t\t|Preço\t\t|Sabor\t\t|")
    print("|1\t\t|500 KZ\t\t|Chocolate\t|")
    print("|2\t\t|500 KZ\t\t|Maracujá\t|")
    print("|3\t\t|250 KZ\t\t|Banana\t\t|")
    print("|4\t\t|300 KZ\t\t|Abacate\t|")
    print("|0 Sair\t\t|\t\t|\t\t|")
    print("--------------------------------------------------")
    sabor=(input("\tEscolha o seu sabor por favor: "))

    if sabor=='0':
        
        print("\nVolte Sempre.....")
        print("   <    >   \n")
        exit()
    elif sabor=='1' or sabor=='2' or sabor=='3' or sabor=='4':
        try:
            quantidade=int(input("\tDigite a quantidade: "))
        except ValueError as erro:
            print("\nApenas é valido numeros inteiro....\n")
            continue

        if quantidade>0:

            try:
                valorApagar=int(input("\tDigite a a sua nota (KZ): "))
            except ValueError as erro:
                print("\nApenas é valido numeros inteiro....\n")
                continue 
        
            if sabor=='1':

                if valorApagar>=quantidade*500: 
                    print("--------------------------------------------------")
                    print("|SABOR\t\t|QUANTIDADE\t|VALOR PAGO\t|")
                    print("|Chocolate\t|{}X\t\t|{} KZ\t|".format(quantidade,valorApagar))
                
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|TOTAL\t\t|TROCO\t\t|")
                    print("|\t\t|{} KZ\t|{} KZ\t|".format(500*quantidade,valorApagar-(500*quantidade)))
                else:
                    print("\nO valor que você pagou é insuficiente.....\n")

            elif sabor=='2':

                if valorApagar>=quantidade*500: 
                    print("--------------------------------------------------")
                    print("|SABOR\t\t|QUANTIDADE\t|VALOR PAGO\t|")
                    print("|Maracujá\t|{}X\t\t|{} KZ\t|".format(quantidade,valorApagar))
                
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|TOTAL\t\t|TROCO\t\t|")
                    print("|\t\t|{} KZ\t|{} KZ\t|".format(500*quantidade,valorApagar-(500*quantidade)))
                else:
                    print("\nO valor que você pagou é insuficiente.....\n")

            elif sabor=='3':

                if valorApagar>=quantidade*250: 
                    print("--------------------------------------------------")
                    print("|SABOR\t\t|QUANTIDADE\t|VALOR PAGO\t|")
                    print("|Banana\t|{}X\t\t|{} KZ\t|".format(quantidade,valorApagar))

                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|TOTAL\t\t|TROCO\t\t|")
                    print("|\t\t|{} KZ\t|{} KZ\t|".format(500*quantidade,valorApagar-(500*quantidade)))
                else:
                    print("\nO valor que você pagou é insuficiente.....\n")

            elif sabor=='4':
                if valorApagar>=quantidade*300: 
                    print("--------------------------------------------------")
                    print("|SABOR\t\t|QUANTIDADE\t|VALOR PAGO\t|")
                    print("|Abacate\t|{}X\t\t|{} KZ\t|".format(quantidade,valorApagar))

                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|\t\t|\t\t|")
                    print("|\t\t|TOTAL\t\t|TROCO\t\t|")
                    print("|\t\t|{} KZ\t|{} KZ\t|".format(500*quantidade,valorApagar-(500*quantidade)))
                else:
                    print("\nO valor que você pagou é insuficiente.....\n")

            print("--------------------------------------------------")
        elif quantidade==0:
            print("\nVolte Sempre.....")
            print("   <    >   \n")
            exit()
        else:
                print("\nÉ valodo apenas numero numero inteiro e maiores que 0 (Zero)\n")    
            
    else:
        print("\n")
        print("Escolha um valor que esteja no Índice\nPor favor....")
        print("\n")
cont +=1



    









