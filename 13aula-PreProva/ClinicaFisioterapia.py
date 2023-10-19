from abc import abstractmethod, ABC

class Paciente(ABC):
    def __init__(self, nome, endereco) -> None:
        self.__nome = nome
        self.__endereco = endereco
        self.__sessoes = []

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getEndereco(self):
        return self.__endereco

        
    def getSessoes(self):
        return self.__sessoes
    
    def addSessao(self, sessao):
        nova_sessao = sessao
        self.__sessoes.append(nova_sessao)

    @abstractmethod
    def geraFichaPaciente(self, mes = None):
        pass

    @abstractmethod
    def calculaValorDevido(self, mes):
        pass
                
#  Ortopedica 30 50
#  respiratoria 40 60
#  pilate 50 70
    
class Particular(Paciente):
    def __init__(self, nome, endereco, cpf) -> None:
        super().__init__(nome, endereco)
        self.__cpf = cpf
    
    @property
    def getCpf(self):
        return self.__cpf
    
    def geraFichaPaciente(self, mes = None):
        print(f'Nome: {self.getNome}')
        print(f'Endereco: {self.getEndereco}')
        print(f'CPF: {self.getCpf}')
        print('Sessoes realizadas:')
        print('Data  -   Tipo')
        if mes is None: #verifica se o mes foi informado
                for sessao in self.getSessoes():
                    print(f'{sessao.getDia}/{sessao.getMes} - {sessao.getTipo.getNome}')
        else:
            for sessao in self.getSessoes():
                if sessao.getMes == mes:
                    print(f'{sessao.getDia}/{sessao.getMes} - {sessao.getTipo.getNome}') #para acessar o campo nome da sessao antes precisamos acessar o tipo onde temos a funcao que possui o nome
        

    def calculaValorDevido(self, mes):
        faturamento_particular = 0
        for sessao in self.getSessoes():
            if sessao.getTipo.getNome == 'Ortopédica' and sessao.getMes == mes:
                faturamento_particular += 50
            elif sessao.getTipo.getNome == 'Respiratória' and sessao.getMes == mes:
                faturamento_particular += 60
            elif sessao.getTipo.getNome == 'Pilates' and sessao.getMes == mes:
                faturamento_particular += 70
    
        return faturamento_particular 
    
class Convenio(Paciente):
    def __init__(self, nome, endereco, nomeConv, nroCartao) -> None:
        super().__init__(nome, endereco)
        self.__nomeConv = nomeConv
        self.__nroCartao = nroCartao
    
    @property
    def getNomeConv(self):
        return self.__nomeConv
    
    @property
    def  getNroCartao(self):
        return self.__nroCartao
    
    def geraFichaPaciente(self, mes = None):
        
            print(f'Nome: {self.getNome}')
            print(f'Endereco: {self.getEndereco}')
            print(f'Convenio: {self.getNomeConv}')
            print(f'Nro cartao: {self.getNroCartao}')
            print('Sessoes realizadas:')
            print('Data  -   Tipo')
           
            
            if mes is None:
                for sessao in self.getSessoes():
                    print(f'{sessao.getDia}/{sessao.getMes} - {sessao.getTipo.getNome}')
            else:
                for sessao in self.getSessoes():
                    if sessao.getMes == mes:
                        print(f'{sessao.getDia}/{sessao.getMes} - {sessao.getTipo.getNome}')

    def calculaValorDevido(self, mes):
        faturamento_convenio = 0
        for sessao in self.getSessoes():
            if sessao.getTipo.getNome== 'Ortopédica' and sessao.getMes== mes:
                faturamento_convenio += 50 * 0.6
            elif sessao.getTipo.getNome== 'Respiratória' and sessao.getMes== mes:
                faturamento_convenio += 60 * 0.6
            elif sessao.getTipo.getNome== 'Pilates' and sessao.getMes== mes:
                faturamento_convenio += 70 * 0.6
    
        return faturamento_convenio

class Sessao:
    def __init__(self, dia, mes, tipo) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__tipo = tipo

    @property
    def getDia(self):
        return self.__dia

    @property
    def getMes(self):
        return self.__mes

    @property
    def getTipo(self):
        return self.__tipo
    
class TipoSessao:
    def __init__(self, nome, duracao, preco) -> None:
        self.__nome = nome
        self.__duracao = duracao
        self.__preco = preco

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getDuracao(self):
        return self.__duracao
    
    @property 
    def getPreco(self):
        return self.__preco
        

if __name__=="__main__":
    listaPac = []
    orto = TipoSessao('Ortopédica', 30, 50)
    resp = TipoSessao('Respiratória', 40, 60)
    pil = TipoSessao('Pilates', 50, 70)
    pac1 = Convenio('Pedro', 'Av BPS, 1303', 'Unimed', 123456)
    pac1.addSessao(Sessao(10, 9, resp))
    pac1.addSessao(Sessao(12, 9, resp))
    pac1.addSessao(Sessao(18, 9, pil))
    pac1.addSessao(Sessao(5, 10, resp))
    listaPac.append(pac1)
    pac2 = Particular('Maria', 'Av Cesario Alvin, 55', 654321)
    pac2.addSessao(Sessao(11, 9, orto))
    pac2.addSessao(Sessao(15, 9, orto))
    pac2.addSessao(Sessao(23, 9, pil))
    pac2.addSessao(Sessao(12, 10, orto))
    listaPac.append(pac2)
    pac1.geraFichaPaciente(10)
    print()
    pac2.geraFichaPaciente()
    print()
    faturamento = 0
    for paciente in listaPac:
        faturamento += paciente.calculaValorDevido(9)
    print('Faturamento do mês 9: {}'.format(faturamento))