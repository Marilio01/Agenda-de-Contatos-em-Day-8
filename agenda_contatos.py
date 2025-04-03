# Agenda de Contatos

# Passo 1: Inicializa uma agenda de contatos vazia
contacts = {}

# Passo 2: Exibe o menu
def show_menu():
  print("\n--- Menu da Agenda de Contatos ---")
  print("1. Adicionar um novo contato")
  print("2. Visualizar todos os contatos")
  print("3. Buscar um contato")
  print("4. Editar contato")
  print("5. Excluir contato")
  print("6. Sair")

# Passo 3: Adiciona um contato
def add_contact():
  name = input("Digite o nome do contato: ")
  phone = input("Digite o número do contato: ")
  email = input("Digite o email do contato: ")
  contacts[name] = {"phone": phone, "email": email}
  print(f"Contato {name} adicionado à sua agenda com sucesso!")

# Passo 4: Visualiza todos os contatos
def view_contacts():
  if contacts:
    print("\n--- Lista de Contatos ---")
    for name, details in contacts.items():
      print(f"Nome: {name}")
      print(f"Telefone: {details['phone']}")
      print(f"Email: {details['email']}")
  else:
    print("Sua agenda de contatos está vazia.")

# Passo 5: Busca um contato
def search_contact():
  name = input("Digite o nome do contato que deseja buscar: ")
  if name in contacts:
    details = contacts[name]
    print(f"Nome: {name}")
    print(f"Telefone: {details['phone']}")
    print(f"Email: {details['email']}")
  else:
    print(f"Contato {name} não encontrado na sua agenda.")

# Passo 6: Edita um contato
def edit_contact():
  name = input("Digite o nome do contato que deseja editar: ")
  if name in contacts:
    phone = input("Digite o novo número de telefone (pressione enter para pular): ")
    email = input("Digite o novo email (pressione enter para pular): ")

    # Lógica aprimorada para editar apenas os campos alterados
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email


    print(f"Contato {name} atualizado com sucesso!")
  else:
    print(f"Contato {name} não encontrado na sua agenda.")

# Passo 7: Exclui um contato
def delete_contact():
  name = input("Digite o nome do contato que deseja excluir: ")
  if name in contacts:
    del contacts[name]
    print(f"Contato {name} excluído com sucesso!")
  else:
    print(f"Contato {name} não encontrado na sua agenda.")

# Passo 8: Loop principal do programa
while True:
  show_menu()
  choice = input("Digite sua escolha (1-6): ")

  if choice == "1":
    add_contact()
  elif choice == "2":
    view_contacts()
  elif choice == "3":
    search_contact()
  elif choice == "4":
    edit_contact()
  elif choice == "5":
    delete_contact()
  elif choice == "6":
    print("Obrigado por usar a Agenda de Contatos. Até logo!")
    break
  else:
    print("Escolha inválida. Por favor, digite um número entre 1 e 6.")


