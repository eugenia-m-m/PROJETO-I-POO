import json
from animal import Animal

class SistemaAdocao:
    __arquivo = "animais.json"   # Arquivo para salvar animais
    list_animais = []            # Lista para armazenar animais
    @classmethod
    def carregar(cls): # Lê os animais salvos no JSON
        with open(cls.__arquivo, "r", encoding="UTF-8") as arquivo:
            cls.list_animais = json.load(arquivo)   # Atualiza a lista
            return cls.list_animais
        return False

    @classmethod
    def salvar(cls, dados): # Salva todos os animais atuais no JSON
        with open(cls.__arquivo, "w", encoding="UTF-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            return True
        return False

    @classmethod
    def cadastrar_Animal(cls, id, nome, especie, sexo, idade, raca, disponibilidade):
        for animal in cls.list_animais:
            if animal["ID"] == id:
                return "⚠️ ID do animal já cadastrado."
        
        animal = {
            "ID": id, 
            "Nome": nome, 
            "Especie": especie, 
            "Sexo": sexo, 
            "Idade": idade, 
            "Raca": raca, 
            "Disponibilidade": disponibilidade
        }
        cls.list_animais.append(animal)
        cls.salvar(cls.list_animais)
        return "✅ Animal cadastrado com sucesso."

    @classmethod
    def listar_Animais(cls):
        if not cls.list_animais:
            return "Nenhum animal cadastrado."
        
        resultado = "\n📋 --- Animais cadastrados ---\n"
        for animal in cls.list_animais:
            resultado += f"ID: {animal['id']}\n"
            resultado += f"Nome: {animal['nome']}\n"
            resultado += f"Espécie: {animal['especie']}\n"
            resultado += f"Sexo: {animal['sexo']}\n"
            resultado += f"Idade: {animal['idade']}\n"
            resultado += f"Raça: {animal['raca']}\n"
            resultado += f"Disponibilidade: {animal['disponibilidade']}\n"
            resultado += "-" * 30 + "\n"
        return resultado

    @classmethod
    def editar_Animal(cls, id_animal, novo_nome):
        for animal in cls.list_animais:
            if animal["ID"] == id_animal:
                animal["Nome"] = novo_nome

                cls.salvar(cls.list_animais)
                return "✅ Animal atualizado com sucesso."
        return "⚠️ Animal não encontrado."

    @classmethod
    def remover_Animal(cls, id_animal):
        for animal in cls.list_animais:
            if animal["ID"] == id_animal:
                cls.list_animais.remove(animal)
                cls.salvar(cls.list_animais)
                return "🗑️ Animal removido com sucesso."
        return "⚠️ Animal não encontrado."
