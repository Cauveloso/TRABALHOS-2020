#CRIANDO VARIAVEIS GLOBAIS
nome = []
preco = []
estoque = []

# Na primeira funcionalidade deve ser registrado o NOME, PREÇO e QUANTIDADE EM ESTOQUE do produto utilizando listas.
def add_produtos():
    produto = input("Digite um produto: ")
    preco_produto = float(input("Digite o preço: "))
    estoque_produto = int(input("Digite o estoque: "))
    
    # Adicionar os elementos às listas corretas
    nome.append(produto)
    preco.append(preco_produto)
    estoque.append(estoque_produto)
    print("PRODUTO CADASTRADO COM SUCESSO!\n")

#Na segunda funcionalidade os produtos devem ser listados da seguinte forma:
########################
#PRODUTO: Nome do produto
#QUANTIDADE: XX
#PREÇO: R$ XX.XX
########################

def listar_produtos():
  if len(nome) == 0:
    print("Nenhum produto cadastrado no sistema.")
  else:
    for i in range(len(nome)):
      print("##############################")
      print("PRODUTO:", nome[i])
      print("QUANTIDADE:", estoque[i])
      print("PREÇO: R$", preco[i])
      print("##############################\n")

def remover_produtos():
    if len(nome) == 0:
        print("Nenhum produto cadastrado no sistema.")
    else:
        print(nome)
        indice_produto = int(input("Digite o índice do produto a ser removido: "))
        if indice_produto < 0 or indice_produto >= len(nome):
            print("Índice inválido.")
        else:
            produto_removido = nome.pop(indice_produto)
            preco.pop(indice_produto)
            estoque.pop(indice_produto)
            print("Produto",produto_removido, "removido com sucesso!\n")
            print("LISTA ATUALIZADA: \n")
            listar_produtos()


#Na funcionalidade de venda fica a critério da equipe decidir como armazenar os itens, lembrando que nessa funcionalidade deve ser fornecido ao usuário um menu oferecendo as opções de adicionar um item ou finalizar o pedido. Ao finalizar o pedido, exibir a lista de produtos no carrinho e o valor total da compra. Perguntar a forma de pagamento, dinheiro ou cartão. Caso seja em dinheiro, o programa deve receber o valor pago e retornar o troco, informando o valor e a quantidade de notas de 1, 5, 10, 20, 50 ou 100 o caixa deve passar, caso necessario. 

def realizar_compra():
    carrinho = []
    valor_total = 0

    while True:
        print("\n============= MENU DE VENDA ================")
        print("A - Adicionar um produto ao carrinho")
        print("F - Finalizar pedido")
        opcao = input("Escolha uma opção: ")

        if opcao == "A":
            listar_produtos()
            indice_produto = int(input("Digite o índice do produto a ser adicionado: "))

            if indice_produto < 0 or indice_produto >= len(nome):
                print("Índice inválido.")
            else:
                produto_selecionado = nome[indice_produto]
                preco_produto = preco[indice_produto]
                quantidade = int(input("Digite a quantidade a ser adicionada: "))

                if quantidade <= estoque[indice_produto]:
                    carrinho.append((produto_selecionado, preco_produto, quantidade))
                    valor_total += preco_produto * quantidade
                    estoque[indice_produto] -= quantidade
                    print("Produto", produto_selecionado, "adicionado ao carrinho.")
                    print("Valor total do carrinho: R$", valor_total)
                else:
                    print("Quantidade indisponível em estoque.")
              
        elif opcao == "F":
            print("\n===== Carrinho de Compras =====")
            for produto in carrinho:
                print("Produtos: ",produto)
                print("Valor total da compra: R$", valor_total)

          #PAGAMENTO
            forma_pagamento = input("\nForma de pagamento (dinheiro ou cartão): ")
            if forma_pagamento == "dinheiro":
                valor_pago = float(input("Valor pago: "))
                troco = valor_pago - valor_total
                print("Troco: R$", troco)

                # Cálculo da quantidade de notas
                notas = [100, 50, 20, 10, 5, 1]
                quantidade_notas = []

                for nota in notas:
                    quantidade = int(troco // nota)
                    quantidade_notas.append(quantidade)
                    troco -= quantidade * nota

                print("Quantidade de notas:")
                for i in range(len(notas)):
                    print(notas[i], ":", quantidade_notas[i])
            else:
                print("FIM DA COMPRA. Voce pagou", valor_total,"no cartão.\n")
            break
    

      
while True:
  print("============= MENU ================")
  print("1 - Adicionar um produto ao sistema")
  print("2 - Listar produtos do sistema")
  print("3 - Remover produto do sistema")
  print("4 - Realizar uma venda")
  print("5 - SAIR\n")
  menu = input("ESCOLHA UMA FUNÇÃO DO NOSSO MENU ACIMA: ")
  if menu == "1":
    add_produtos()
  elif menu == "2":
    listar_produtos()
  elif menu == "3":
    remover_produtos()
  elif menu == "4":
    realizar_compra()
  elif menu == "5":
    break
  else:
    print("Função Não Cadastrada!")
    break