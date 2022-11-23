from conexion.oracle_queries import OracleQueries

class Relatorio:
  def __init__(self):
    # Abre o arquivo com a consulta e associa a um atributo da classe
    with open('./sql/relatorio_curso_dos_alunos.sql') as f:
      self.query_relatorio_curso_dos_alunos = f.read()
    
    with open('./sql/relatorio_alunos_por_turma.sql') as f:
      self.query_relatorio_alunos_por_turma = f.read()


  def getRelatorioCursoDosAlunos(self):
    # Cria uma nova conexão com o banco que permite alteração
    oracle = OracleQueries()
    oracle.connect()

    # Recupera os dados transformando em um DataFrame
    print(oracle.sqlToDataFrame(self.query_relatorio_curso_dos_alunos))
    input("Pressione Enter para Sair do Relatório de Pedidos")

  def getRelatorioAlunosPorTurma(self):
    # Cria uma nova conexão com o banco que permite alteração
    oracle = OracleQueries()
    oracle.connect()

    # Recupera os dados transformando em um DataFrame
    print(oracle.sqlToDataFrame(self.query_relatorio_alunos_por_turma))
    input("Pressione Enter para Sair do Relatório de Pedidos")

