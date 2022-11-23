from model.cursoEG import CursoEG

class AlunoEg:
    def __init__(self,
                 matricula:int=None,
                 nome:str=None,
                 cpf:str=None,
                 curso:CursoEG=None
                    ):
        
        self.set_matricula(matricula)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_curso(curso)

    def set_matricula(self, matricula:int):
        self.matricula = matricula
    
    def set_nome(self, nome:str):
        self.nome = nome
    
    def set_cpf(self, cpf:str):
        self.cpf = cpf

    def set_curso(self, curso:CursoEG):
        self.curso = curso

    def get_matricula(self) -> int:
        return self.matricula

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_curso(self) -> CursoEG:
        return self.curso

    def to_string(self) -> str:
        return f"Matricula: {self.get_matricula()} | Nome: {self.get_nome()} | CPF: {self.get_cpf()} | Curso: {self.get_curso().to_string()}"
        

