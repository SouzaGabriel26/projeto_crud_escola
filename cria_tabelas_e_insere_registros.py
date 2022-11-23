from conexion.oracle_queries import OracleQueries

def execute_commands(query: str):
  list_of_commands = query.split(";")

  oracle = OracleQueries(can_write = True)
  oracle.connect()

  for command in list_of_commands:
    if len(command) > 0:
      print(command)
      try:
        oracle.executeDDL(command)
        print("Sucessfully excecuted")
      except Exception as e:
        print(e)


def generate_records(query: str, sep: str=";"):
  list_of_commands = query.split(sep)

  oracle = OracleQueries(can_write=True)
  oracle.connect()

  for command in list_of_commands:
    if len(command) > 0:
      print(command)
      oracle.write(command)
      print("Sucessfuly executed")



def run():
  
  with open("../sql/creatingTables.sql") as f:
    query_create = f.read()

  print("Creating tables...")
  execute_commands(query=query_create)
  print("Tables succesfully created")

  with open("../sql/insertingRecords.sql") as f:
    query_generate_records = f.read()

  print("Generating Records")
  generate_records(query=query_generate_records)
  print("Records successfully generated")

if __name__ == '__main__':
  run()