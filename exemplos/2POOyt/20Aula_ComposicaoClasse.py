class Insert:
    def insert_many(self):
        print('Insert Many')

    def insert_one(self):
        print('Insert one')

class Select:
    def select_many(self):
        print('select Many')

    def select_one(self):
        print('select one')

class Repositorio:
    def __init__(self) -> None:
        self.__insert = Insert()
        self.__select = Select()
    
    def select_by_id(self):
        self.__select.select_one()


repo = Repositorio()
repo.select_by_id()
    