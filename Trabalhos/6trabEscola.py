#NOME: Pedro Venancio dos Santos MATRICULA:2023010066

class Pessoa:
    def __init__(self, nome, endereco, idade, cpf) -> None:
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    def get_name(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_idade(self):
        return self.__idade

    def print_descricao(self):
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Idade: {self.__idade}")
        print(f"Endereço: {self.__endereco}")


class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao) -> None:
        super().__init__(nome, endereco, idade, cpf)
        if titulacao != 'doutor':
            raise Exception("Titulação inválida para um professor.")
        if idade < 30:
            raise Exception("Idade mínima para um professor é 30 anos.")
        self.__titulacao = titulacao

    def get_titulacao(self):
        return self.__titulacao


class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso) -> None:
        super().__init__(nome, endereco, idade, cpf)
        if curso not in ['CCO', 'SIN']:
            raise Exception("Curso inválido para um aluno.")
        if idade < 18:
            raise Exception("Idade mínima para um aluno é 18 anos.")
        self.__curso = curso

    def get_curso(self):
        return self.__curso

# Cria uma lista de pessoas, incluindo aquelas que violam e aquelas que atendem aos critérios
cadastro = []

try:
    professor1 = Professor("Prof1", "Endereco1", 35, "11111111111", "doutor")
    cadastro.append(professor1)
except Exception as e:
    print(e)

try:
    aluno1 = Aluno("Aluno1", "Endereco2", 20, "22222222222", "CCO")
    cadastro.append(aluno1)
except Exception as e:
    print(e)

try:
    aluno2 = Aluno("Aluno2", "Endereco3", 17, "33333333333", "SIN")
    cadastro.append(aluno2)
except Exception as e:
    print(e)

try:
    professor2 = Professor("Prof2", "Endereco4", 28, "11111111111", "doutor")
    cadastro.append(professor2)
except Exception as e:
    print(e)

try:
    aluno3 = Aluno("Aluno3", "Endereco5", 25, "44444444444", "ECO")
    cadastro.append(aluno3)
except Exception as e:
    print(e)

# Imprime os detalhes de cada pessoa no cadastro
for pessoa in cadastro:
    pessoa.print_descricao()
    print()

