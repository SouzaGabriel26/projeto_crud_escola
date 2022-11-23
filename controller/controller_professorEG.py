from conexion.oracle_queries import OracleQueries
from controller.controller_cursoEG import Controller_CursoEG
from model.cursoEG import CursoEG
from model.professoresEG import ProfessoresEG

class Controller_ProfessorEG:
    def __init__(self):
        self.ctrl_curso = Controller_CursoEG()

    def inserir_professor(self) -> ProfessoresEG:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect() 
        
        # Solicita ao usuário o id_professor que deseja inserir
        self.listar_professores(oracle, need_connect=True)
        id_professor = int(input("Digite o id_professor (NOVO): "))

        if self.verifica_existencia_professor(oracle, id_professor):
            # Solicita ao usuário os dados para preencher o novo professor
            nome = input("Nome do professor (NOVO): ")
            qtde_turmas = int(input("Quantidade de turmas do professor (NOVO): "))


            # Lista os cursos cadastrados
            self.ctrl_curso.listar_cursos(oracle, need_connect=True)

            id_curso = int(input("id_curso que o professor da aula: "))

            curso = self.valida_curso(oracle, id_curso)
            if curso == None:
                return None

            oracle.write(f"insert into professoresEG values (PROFESSOR_ID_PROFESSOR.NEXTVAL, '{nome}', '{qtde_turmas}', {curso.get_id_curso()})")
            # Persiste (confirma) as alterações
            oracle.conn.commit()

            # Recupera os dados do novo Professor criando transformando em um DataFrame
            df_professor = oracle.sqlToDataFrame(f"select id_professor, nome, qtde_turmas, id_curso from professoresEG where id_professor = {id_professor}")

            # Cria um novo objeto Professor
            novo_professor = ProfessoresEG(df_professor.id_professor.values[0], df_professor.nome.values[0], df_professor.qtde_turmas.values[0], curso)

            # Exibe os atributos do Professor
            print(novo_professor.to_string())
            # Retorna o objeto novo_professor para utilização posterior, caso necessário
            return novo_professor
        else:
            print(f"Professor com id_professor = {id_professor} já cadastrado!")


    def atualiza_professor(self) -> ProfessoresEG:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o id_professor do professor a ser atualizado
        self.listar_professores(oracle, need_connect=True)
        id_professor = int(input("id do professor que deseja alterar os dados: "))

        # Verifica a existencia do professor no banco
        if not self.verifica_existencia_professor(oracle, id_professor):
            # Solicita ao usuário os novos dados do professor
            nome = input("Nome do professor (NOVO): ")
            qtde_turmas = int(input("Quantidade de turmas do professor: "))
            id_curso = int(input("Id do curso que o professor da aula: "))

            # faz a validação para ver se o curso existe na base de dados
            curso = self.valida_curso(oracle, id_curso)
            if curso == None:
                return None
            
            oracle.write(f"update professoresEG set nome = '{nome}', qtde_turmas = {qtde_turmas}, id_curso = {curso.get_id_curso()} where id_professor = {id_professor}")

            # Recupera os dados do novo professor criado transformando em um DataFrame
            df_professor = oracle.sqlToDataFrame(f"select id_professor, nome, qtde_turmas, id_curso from professoresEG where id_professor = {id_professor}")

            # Cria um novo objeto ProfessoresEG
            professor_atualizado = ProfessoresEG(df_professor.id_professor.values[0], df_professor.nome.values[0], df_professor.qtde_turmas.values[0], curso)

            # Exibe os dados do professor atualizado
            print(professor_atualizado.to_string())
            return professor_atualizado
        
        else: 
            print(f"O professor de id = {id_professor} não existe no banco! ")
            return None


    def excluir_professor(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o id_professor que deseja excluir
        self.listar_professores(oracle, need_connect=True)
        id_professor = int(input("Id do professor que deseja excluir: "))

        # Verifica a existencia do professor
        if not self.verifica_existencia_professor(oracle, id_professor):
            # Recupera os dados do professor transformando em um DataFrame
            df_professor = oracle.sqlToDataFrame(f"select id_professor, nome, qtde_turmas, id_curso from professoresEG where id_professor = {id_professor}")

            # Valida id_curso
            curso = self.valida_curso(oracle, df_professor.id_curso.values[0])

            opcao_excluir = input(f"Tem certeza que deseja excluir o professor {df_professor.nome.values[0]} [S ou N]: ")

            if opcao_excluir in "Ss":
                # Remove o professor da tabela
                oracle.write(f"delete from professoresEG where id_professor = {id_professor}")

                # faz a validação para ver se o curso existe na base de dados
                curso = self.valida_curso(oracle, int(df_professor.id_curso.values[0]))
                if curso == None:
                    return None
                
                # Cria um novo objeto ProfessoresEG
                professor_excluido = ProfessoresEG(df_professor.id_professor.values[0], df_professor.nome.values[0], df_professor.qtde_turmas.values[0], curso)

                print("Professor removido! ")
                print(professor_excluido.to_string())
        
        else:
            print(f"O professor de id = {id_professor} não está na base de dados ")





    def listar_professores(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
            select id_professor, nome, qtde_turmas, id_curso from professoresEG
        """
        if need_connect:
            oracle.connect()
            print(oracle.sqlToDataFrame(query))
            print("")


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


    def verifica_existencia_professor(self, oracle: OracleQueries, id_professor:int=None) -> bool:
        # Recupera os dados do professor transformando em um DataFrame
        df_professor = oracle.sqlToDataFrame(f"select id_professor, nome from professoresEG where id_professor = {id_professor}")
        return df_professor.empty