import json

class Adotante:
    arquivo = "adotantes.json"   # Arquivo para salvar adotantes
    cadastro_adotantes = []      # Lista para armazenar adotantes

    def __init__(self, id, nome, idade, rg, cpf, comprovante, endereco): # Atributos básicos do adotante
        self.id = id
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.cpf = cpf
        self.comprovante = comprovante
        self.endereco = endereco
    
    @classmethod
    def carregar(cls): # Lê os adotantes salvos no JSON
        with open(cls.arquivo, "r", encoding="UTF-8") as arquivo:
            dado = json.load(arquivo)
            return dado
        return False

    @classmethod
    def salvar(cls, dados): # Salva todos os adotantes atuais no JSON
        with open(cls.arquivo, "w", encoding="UTF-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            return True
        return False
    
    @classmethod
    def cadastrar_Adotante(cls, id, nome, idade, rg, cpf, comprovante, endereco):
        adotante = {
                "ID": id, 
                "Nome":nome, 
                "Idade": idade,
                "RG": rg,
                "CPF": cpf,
                "comprovante":comprovante,
                "endereco": endereco
        }
        cls.cadastro_adotantes.append(adotante)
        cls.salvar(cls.cadastro_adotantes)
        return "✅ Adotante cadastrado com sucesso."
    
    @classmethod
    def editar_adotante(cls, id_adotante, novo_nome): # Procura adotante pelo ID e altera o nome
        for adotante in cls.cadastro_adotantes:
            if adotante["ID"] == id_adotante:  
                adotante["Nome"] = novo_nome  
                cls.salvar(cls.cadastro_adotantes)
                return "✅ Adotante atualizado com sucesso."
        return "⚠️ Adotante não encontrado."

    @classmethod
    def remover_adotante(cls, id_adotante):  # Remove adotante pelo ID
        for adotante in cls.cadastro_adotantes:
            if adotante["ID"] == id_adotante: 
                cls.cadastro_adotantes.remove(adotante)
                cls.salvar(cls.cadastro_adotantes)
                return "🗑️ Adotante removido com sucesso."
        return "⚠️ Adotante não encontrado."


