class CursoEG:
    def __init__(self,
                 id_curso:int=None,
                 nome:str=None,
                 coordenador:str=None
                 ):
        
        self.set_id_curso(id_curso)
        self.set_nome(nome)
        self.set_coordenador(coordenador)
        

    def set_id_curso(self, id_curso:int):
        self.id_curso = id_curso

    def set_nome(self, nome:str):
        self.nome = nome

    def set_coordenador(self, coordenador:str):
        self.coordenador = coordenador

    def get_id_curso(self) -> int:
        return self.id_curso

    def get_nome(self) -> str:
        return self.nome

    def get_coordenador(self) -> str:
        return self.coordenador

    def to_string(self) -> str:
        return f"id curso: {self.get_id_curso()} | Nome: {self.get_nome()} | Coordenador: {self.get_coordenador()}"