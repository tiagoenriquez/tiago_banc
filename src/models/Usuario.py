from src.models.Model import Model


class Usuario(Model):
    def __init__(self, nome: str, cpf: str, perfil: str, senha: str, id: int | None = None) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.perfil = perfil
        self.senha = senha
    
    # def fields(self) -> list[str]:
    #     return ["nome", "cpf", "perfil", "senha"]
    
    # def to_inserted_array(self) -> list:
    #     return [self.nome, self.cpf, self.perfil, self.senha]
    
    # def to_updated_array(self) -> list:
    #     return [self.nome, self.cpf, self.perfil, self.senha, self.id]