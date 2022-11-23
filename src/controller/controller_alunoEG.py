from model.alunoEG import AlunoEg
from model.cursoEG import CursoEG
from controller.controller_cursoEG import Controller_CursoEG
from conexion.oracle_queries import OracleQueries

class Controller_AlunoEG:
    def __init__(self):
        self.ctrl_curso = Controller_CursoEG()

    def inserir_aluno(self) -> AlunoEg:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuario o novo CPF
        self.listar_alunos(oracle, need_connect=True)
        cpf = input("CPF (NOVO): ")

        if self.verifica_existencia_aluno(oracle, cpf):
            # Solicita os dados do novo aluno ao usuario
            nome = input("Nome do Aluno: ")
            self.listar_cursos(oracle, need_connect=True)
            id_curso = input("id do curso: ")

            curso = self.valida_curso(oracle, id_curso)
            if curso == None:
                return None

            oracle.write(f"insert into alunosEG values (ALUNOS_MATRICULA_SEQ.NEXTVAL, '{nome}', '{cpf}', {curso.get_id_curso()})")
            # Persiste (confirma) as alterações
            oracle.conn.commit()

            # Recupera os dados do novo Aluno criando transformando em um DataFrame
            df_aluno = oracle.sqlToDataFrame(f"select matricula, nome, cpf, id_curso from alunosEG where cpf = {cpf }")

            # Cria um novo objeto Aluno
            novo_aluno = AlunoEg(df_aluno.matricula.values[0], df_aluno.nome.values[0], df_aluno.cpf, curso)

            # Exibe os atributos do Aluno
            print(novo_aluno.to_string())
            # Retorna o objeto novo_aluno para utilização posterior, caso necessário
            return novo_aluno
        else:
            print(f"Aluno com cpf {cpf} já está cadastrado!")


    def atualizar_aluno(self) -> AlunoEg:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o cpf do Aluno a ser alterado
        self.listar_alunos(oracle, need_connect=True)
        cpf = input("Cpf do aluno que deseja alterar os dados: ")

        # se o aluno existir
        if not self.verifica_existencia_aluno(oracle, cpf):

            # solicita ao usuario os dados do aluno a ser atualizado
            nome = input("Nome (NOVO): ")
            id_curso = input("id do curso: (NOVO)")

            # faz a validação para ver se o curso existe na base de dados
            curso = self.valida_curso(oracle, id_curso)
            if curso == None:
                return None
            
            # Atualiza os Dados do Aluno
            oracle.write(f"update alunosEG set nome = '{nome}', id_curso = {curso.get_id_curso()} where cpf = {cpf}")

            # Recupera os dados do novo aluno criado transformando em um DataFrame
            df_aluno = oracle.sqlToDataFrame(f"select matricula, nome, cpf, id_curso from alunosEG where cpf = {cpf}")

            # Cria um novo objeto AlunosEG
            aluno_atualizado = AlunoEg(df_aluno.matricula.values[0], df_aluno.nome.values[0], df_aluno.cpf.values[0], curso)

            # Exibe os atributos do aluno_atualizado
            print(aluno_atualizado.to_string())

            # Retorna o objeto aluno_atualizado para utilização posterior, caso necessário
            return aluno_atualizado
        else:
            print(f"O aluno de cpf {cpf} não está na base de dados")
            return None


    def excluir_aluno(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o cpf do aluno a ser excluído
        self.listar_alunos(oracle, need_connect=True)
        cpf = input("Cpf do aluno que deseja excluir: ")

        # Verifica se o Aluno existe na base de dados
        if not self.verifica_existencia_aluno(oracle, cpf):

            # Recupera os dados do aluno a ser excluido transformando em um DataFrame
            df_aluno = oracle.sqlToDataFrame(f"select matricula, nome, cpf, id_curso from alunosEG where cpf = {cpf}")

            opcao_exlcuir = input(f"Tem certeza que deseja excluir o aluno {df_aluno.nome.values[0]}? [S OU N]: ")

            if opcao_exlcuir in "Ss":
                # Remove o aluno da tabela
                oracle.write(f"delete from alunosEG where cpf = {cpf}")

                # faz a validação para ver se o curso existe na base de dados
                curso = self.valida_curso(oracle, int(df_aluno.id_curso.values[0]))
                if curso == None:
                    return None

                # Cria um novo objeto AlunoEg para informar que foi removido
                aluno_excluido = AlunoEg(df_aluno.matricula.values[0], df_aluno.nome.values[0], df_aluno.cpf.values[0], curso)

                # Exibe os dados do aluno Excluido
                print("Aluno excluido com sucesso!")
                print(aluno_excluido.to_string())

        else:
            print(f"O aluno de cpf = {cpf} não está na base de dados")

    def valida_curso(self, oracle: OracleQueries, id_curso:int=None) -> CursoEG:
        if self.ctrl_curso.verifica_existencia_curso(oracle, id_curso):
            print(f"O curso {id_curso} informado não existe na base de dados")
            return None
        else: 
            oracle.connect()
            # recupera os dados do curso transformando em um dataFrame
            df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, coordenador from cursoEG where id_curso = {id_curso}")

            # Cria um novo objeto CursoEG
            curso = CursoEG(df_curso.id_curso.values[0], df_curso.nome.values[0], df_curso.coordenador.values[0])
            return curso

    
    def listar_alunos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select matricula, nome, cpf, id_curso from alunosEG
        """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
        print("")


    def listar_cursos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select id_curso, nome, coordenador from cursoEG
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
        print("")



    def verifica_existencia_aluno(self, oracle: OracleQueries, cpf:str=None) -> bool:
        # Recupera os dados do aluno transformando em um DataFrame
        df_aluno = oracle.sqlToDataFrame(f"select cpf, nome, id_curso from alunosEG where cpf = {cpf}")
        return df_aluno.empty