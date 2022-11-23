# Projeto de CRUD em Python, fazendo conexão ao banco Oracle
## Sistema Escolar

### Bibliotecas Utilizadas (executar se for utilizar o sistema pela primeira vez)
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`


Como executar:

- Primeiro, vá no arquivo oracle_queries.py, dentro da pasta conexion;

Em seguida, modifique a seguinte linha de código (linha 41 ou próximo):
```python
self.conn = cx_Oracle.connect('user/password@localhost:1521/XEPDB1')
```
substitua 'user' e 'password' pelo usuário e senha do seu banco de dados Oracle.

- Após feita a conexão, execute:

```shell
cd .\src\
python .\cria_tabelas_e_insere_registros.py
python .\index.py
```
### Feito isso, o sistema será intuitivo

## Vídeo demonstrativo do sistema
- (https://www.youtube.com/watch?v=6uouQ_-5vqw&ab_channel=GabrielAlves)

## Contato
- [LinkedIn](https://www.linkedin.com/in/gabriel-alves-73860a1ab/)
