class PostgresDB:
    def __init__(self) -> None:
        self.__conexao = 'Postgres'

    def conectar(self):
        print('Conectando ...')
        return self.__conexao
    
    def desconectar(self):
        print('desconectando')

#repositorio.py
class Repositorio:# Possui comportamento geral, serve para qualquer novo banco cadastrado
    def select(self, db_connection):
        conection = db_connection.conectar()
        print(f'conectei ao banco {conection}')
        print('Fazendo um SELECT *FROM ...')
        db_connection.desconectar()

    def insert(self, db_connection):
        conection = db_connection.conectar()
        print(f'conectei ao banco {conection}')
        print('Fazendo um Insert Values ...')
        db_connection.desconectar()
    
#main.py
#from repositorio import repositorio
#from database import PostgresDB

db_conn = PostgresDB()
repo = Repositorio()

repo.insert(db_conn)
repo.select(db_conn)















# #Fechado se o modulo  estiver disponiveis para uso por outros modulo
# #Aberto se ainda estiver disponivel para extenção

# #FECHADO

# class Circo:
#     def apresentar(self, tipo):
#         if tipo == 1:
#             self.apresentar_malabarista()
#         if tipo == 2:                   # Limita os tipo de apresentaçao onde temos q modificar o codigo 
#             self.apresentar_palhaco()   #para add um novo show
            

#     def apresentar_malabrista(self):
#         print('malabarista apresentando')
    
#     def aprensentar_palhaco(self):
#         print('Palhaco apresentando')

# #Aberto

# class Circo:
#     def apresentar(self, apresentador):
#         apresentador.apresentar_show()


# class Malabarista:
#     def apresentar_show(self):
#         print('malabarista apresentando')

# class Palhaco:
#     def aprensentar_show(self):
#         print('Palhaco apresentando')


