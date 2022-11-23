from model.cursoEG import CursoEG
from conexion.oracle_queries import OracleQueries

class Controller_CursoEG:
    def __init__(self):
        pass

    def inserir_curso(self) -> CursoEG:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_cursos(oracle, need_connect=True)
        id_curso = input("id do curso (NOVO): ")

        # Verifica se o curso existe na base de dados
        if self.verifica_existencia_curso(oracle, id_curso):
            nome = input("nome do curso (novo): ")
            coordenador = input("nome do coordenador: ")

            oracle.write(f"insert into CursoEG values ('{id_curso}', '{nome}', '{coordenador}')")
            
            # Persiste (confirma) as alterações
            oracle.conn.commit()

            # Recupera os dados do novo curso criado transformando em um DataFrame
            df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, coordenador from CursoEG where id_curso = '{id_curso}'")

            # Cria um novo objeto CursoEG
            novo_curso = CursoEG(id_curso, df_curso.nome.values[0], df_curso.coordenador.values[0])

            # Exibe os atributos do novo curso
            print("")
            print(novo_curso.to_string())
            
            # Retorna o objeto novo_curso para utilização posterior, caso necessário
            return novo_curso

        else:
            print(f"O curso de id {id_curso} já está cadastrado")
            return None


    def atualizar_curso(self) -> CursoEG:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_cursos(oracle, need_connect=True)
        id_curso = input("Id do curso que deseja atualizar os dados: ")

        # Verifica se o curso existe na base de dados
        if not self.verifica_existencia_curso(oracle, id_curso):
            # solicita a nova descriçao do curso
            novo_nome_curso = input("Novo nome do Curso: ")
            novo_nome_coordenador = input("Novo nome do coordenador: ")

            # Atualiza o nome do curso existente
            oracle.write(f"update CursoEG set nome = '{novo_nome_curso}' where id_curso = '{id_curso}' ")

            # Atualiza o coordenador do curso existente
            oracle.write(f"update CursoEG set coordenador = '{novo_nome_coordenador}' where id_curso = '{id_curso}' ")

            # Recupera os dados do novo curso criado transformando em um DataFrame
            df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, coordenador from CursoEG where id_curso = {id_curso}")

            # Cria um novo obejto curso
            curso_atualizado = CursoEG(id_curso, df_curso.nome.values[0], df_curso.coordenador.values[0])

            # Exibe os atributos do novo curso
            print(curso_atualizado.to_string())
            # Retorna o objeto curso_atualizado para utilização posterior, caso necessário
            return curso_atualizado
        else:
            print(f"O id_curso {id_curso} não existe.")
            return None


    def excluir_curso(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_cursos(oracle, need_connect=True)
        id_curso = input("Id do curso que deseja excluir: ")

        # Verifica se o curso existe na base de dados
        if not self.verifica_existencia_curso(oracle, id_curso):

            # Recupera os dados do novo curso criado transformando em um DataFrame
            df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, coordenador from CursoEG where id_curso = {id_curso}")

            opcao_excluir = input(f"Tem certeza que deseja excluir o curso {df_curso.nome.values[0]} [S ou N]: ")

            if opcao_excluir in "Ss":
                # Pede uma confirmação ao usuário
                print("Atenção, caso o curso possua professores ou alunos vinculados, também serão excluídos")
                opcao_excluir = input(f"Tem certeza que deseja excluir o curso {df_curso.nome.values[0]} [S ou N]: ")

                if opcao_excluir in "Ss":

                    # Remove o curso da tabela e as entidades que possuem alguma referência com o curso
                    oracle.write(f"delete from AlunosEG where id_curso = {id_curso}")
                    oracle.write(f"delete from ProfessoresEG where id_curso = {id_curso}")
                    oracle.write(f"delete from CursoEG where id_curso = {id_curso}")

                    # Cria um novo obejto curso exlcuido
                    curso_excluido = CursoEG(id_curso, df_curso.nome.values[0], df_curso.coordenador.values[0])

                    # Exibe os atributos do curso excluido
                    print(curso_excluido.to_string())
        else:
            print(f"O id_curso {id_curso} não existe.")

    def listar_cursos(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
            select id_curso, nome, coordenador from cursoEG
        """
        if need_connect:
            oracle.connect()
            print(oracle.sqlToDataFrame(query))
            print("")

    def verifica_existencia_curso(self, oracle:OracleQueries, id_curso:int=None) -> bool:
        # Recupera os dados do novo curso criado transformando em um DataFrame
        df_curso = oracle.sqlToDataFrame(f"select id_curso, nome from CursoEG where id_curso = {id_curso}")
        return df_curso.empty