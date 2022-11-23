import utils.options as Options
from utils import config
from utils.splash_screen import SplashScreen


options = Options # Arquivo separado que contém as funções de relatorios, inserir, atualizar e excluir

tela_inicial = SplashScreen() # Formato padrao para apresentação do sistema


def run():
  print(tela_inicial.get_updated_screen())
  config.clear_console()

  while True:

    print(config.MENU_PRINCIPAL)
    opcao = int(input("Escolha uma opção [1-5]: "))

    if opcao == 1: # Relatórios

      print(config.MENU_RELATORIOS)
      opcao_relatorio = int(input("Escolha uma opção [0-2]: "))
      config.clear_console(1)

      options.reports(opcao_relatorio=opcao_relatorio)

      config.clear_console(1)

    elif opcao == 2: # Inserir Registros

      print(config.MENU_ENTIDADES)
      opcao_inserir = int(input("Escolha uma opção [1-3]: "))
      config.clear_console(1)

      options.inserir(opcao_inserir=opcao_inserir)

      config.clear_console()
      print(tela_inicial.get_updated_screen()) # Mostra a SplashScreen atualizada
      config.clear_console(5)

    elif opcao == 3: # Atualizar Registros

      print(config.MENU_ENTIDADES)
      opcao_atualizar = int(input("Escolha uma opção [1-3]: "))
      config.clear_console(1)

      options.atualizar(opcao_atualizar=opcao_atualizar)

      config.clear_console()

    elif opcao == 4: # Remover Registros

      print(config.MENU_ENTIDADES)
      opcao_excluir = int(input("Escolha uma opção [1-3]: "))
      config.clear_console(1)

      options.excluir(opcao_excluir=opcao_excluir)

      config.clear_console()
      print(tela_inicial.get_updated_screen())
      config.clear_console()

    elif opcao == 5:
      
      print(tela_inicial.get_updated_screen())
      config.clear_console()
      print("Obrigado por utilizar o nosso Sistema Escolar!")
      exit(0)

    else:
      print("Opção Incorreta")
      exit(1)

    
if __name__ == "__main__":
    run()