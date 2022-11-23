from reports.relatorios import Relatorio
from controller.controller_cursoEG import Controller_CursoEG
from controller.controller_alunoEG import Controller_AlunoEG
from controller.controller_professorEG import Controller_ProfessorEG

relatorio = Relatorio()
ctrl_curso = Controller_CursoEG()
ctrl_aluno = Controller_AlunoEG()
ctrl_professor = Controller_ProfessorEG()

def reports(opcao_relatorio:int=0):
    if opcao_relatorio == 1:
        relatorio.getRelatorioCursoDosAlunos()
    elif opcao_relatorio == 2:
        relatorio.getRelatorioAlunosPorTurma()

def inserir(opcao_inserir:int=0):
    if opcao_inserir == 1:
        novo_aluno = ctrl_aluno.inserir_aluno()
    elif opcao_inserir == 2:
        novo_curso = ctrl_curso.inserir_curso()
    elif opcao_inserir == 3:
        novo_professor = ctrl_professor.inserir_professor()

def atualizar(opcao_atualizar:int=0):
    if opcao_atualizar == 1:
        aluno_atualizado = ctrl_aluno.atualizar_aluno()
    elif opcao_atualizar == 2:
        curso_atualizado = ctrl_curso.atualizar_curso()
    elif opcao_atualizar == 3:
        professor_atualiado = ctrl_professor.atualiza_professor()
    
def excluir(opcao_excluir:int=0):
    if opcao_excluir == 1:
        ctrl_aluno.excluir_aluno()
    elif opcao_excluir == 2:
        ctrl_curso.excluir_curso()
    elif opcao_excluir == 3:
        ctrl_professor.excluir_professor()