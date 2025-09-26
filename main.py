from Sistema_adocao import SistemaAdocao  
from adotante import Adotante

def menu():
    SistemaAdocao.carregar()  # Carrega animais do JSON
    Adotante.carregar()       # Carrega adotantes do JSON

    while True:
        print(""" 
        ------------- MENU -------------
            
            1 - CADASTRAR ANIMAL 📃
            2 - LISTAR ANIMAIS 🐶🐱🐦
            3 - EDITAR ANIMAL ✏️
            4 - REMOVER ANIMAL 🗑️
            5 - CADASTRAR ADOTANTE 📃
            6 - EDITAR ADOTANTE ✏️
            7 - REMOVER ADOTANTE 🗑️
            0 - SAIR ❌
    """)
        op = input("Escolha uma opção: ")

        if op == '1':
            id = input("ID: ")
            nome = input("Nome: ")
            especie = input("Espécie: ")
            sexo = input("Sexo: ")
            idade = input("Idade: ")
            raca = input("Raça: ")
            disponibilidade = input("Disponível (Sim/Não): ")
            print(SistemaAdocao.cadastrar_Animal(id, nome, especie, sexo, idade, raca, disponibilidade))

        elif op == '2':
            print(SistemaAdocao.listar_Animais())

        elif op == '3':
            id = input("Digite o ID do animal a editar: ")
            novo_nome = input("Digite o novo nome: ")
            print(SistemaAdocao.editar_Animal(id, novo_nome))

        elif op == '4':
            id = input("Digite o ID do animal a remover: ")
            print(SistemaAdocao.remover_Animal(id))

        elif op == '5':
            id = input("ID: ")
            nome = input("Nome: ")
            idade = input("Idade: ")
            rg = input("RG: ")
            cpf = input("CPF: ")
            comprovante = input("Comprovante: ")
            endereco = input("Endereço: ")
            print(Adotante.cadastrar_Adotante(id, nome, idade, rg, cpf, comprovante, endereco))
            
        elif op == '6':
            id = input("Digite o ID do adotante a editar: ")
            novo_nome = input("Digite o novo nome: ")
            print(Adotante.editar_adotante(id, novo_nome))

        elif op == '7':
            id = input("Digite o ID do adotante a remover: ")
            print(Adotante.remover_adotante(id))

        elif op == '0':
            print("Volte sempre!👋")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente!")

if __name__ == "__main__":
    menu()

