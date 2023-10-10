class DatabaseConn:
    def __init__(self) -> None:
        self.__dadtabase = 'MySQL'              #__ privado
        self._conn = '//connection_string'      #_protect
        self.user = 'SZn'                       #public

    def get_database(self):
        print(self.__dadtabase)
    
    def _testing_connection(self): #protect
        print('OK')


class Repository(DatabaseConn):
    def __init__(self) -> None:
        super().__init__()
        print(self.user)
        #print(self.__dadtabase)
        print(self._conn)
    
    def select(self):
        self._testing_connection()
        print(f'conectando a {self._conn}')
        print('SELECT * FROM table')


repo = Repository()
repo.select()
