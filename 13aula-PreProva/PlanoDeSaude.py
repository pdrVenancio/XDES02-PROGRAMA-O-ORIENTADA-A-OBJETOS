class Paciente:
    def __init__(self, nome, cpf, idade, nivelPlano) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__nivelPlano = nivelPlano
        self.__listaServicos = []

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getCpf(self):
        return self.__cpf
    
    @property
    def getIdade(self):
        return self.__idade

    @property
    def getNivelPlano(self):
        return self.__nivelPlano
    
    @property
    def getListaServicos(self):
        return self.__listaServicos
    
 #ouro = so paga o plano
 # prata = paga 50% dos exames
 # bronse = paga 50% exames e consultas  

#######################################################################################################
 
    def insereConsulta(self, dia, mes, ano, valor, nomeMedico):
        nova_consulta = Consulta(dia, mes, ano, valor, nomeMedico)
        self.__listaServicos.append(nova_consulta)
        return True
    
    def insereExame(self, dia, mes, ano, valor, descricao, nomeClinica, clinicaConv):
        novo_exame = Exame(dia, mes, ano, valor, descricao, nomeClinica, clinicaConv)
        self.__listaServicos.append(novo_exame)
        return False

    def obtemCustoFixo(self):
        if self.getIdade <= 19:
            if self.getNivelPlano == "ouro":
                valor = 420
                return valor
            elif self.getNivelPlano == "prata":
                valor = 320
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 220
                return valor
        elif self.getIdade >= 20 and self.getIdade <= 29:
            if self.getNivelPlano == "ouro":
                valor = 520
                return valor
            elif self.getNivelPlano == "prata":
                valor = 420
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 320
                return valor
        elif self.getIdade >= 30 and self.getIdade <= 39:
            if self.getNivelPlano == "ouro":
                valor = 620
                return valor
            elif self.getNivelPlano == "prata":
                valor = 520
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 420
                return valor
        elif self.getIdade >= 40 and self.getIdade <= 49:
            if self.getNivelPlano == "ouro":
                valor = 720
                return valor
            elif self.getNivelPlano == "prata":
                valor = 620
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 520
                return valor
        elif self.getIdade >= 50 and self.getIdade <= 59:
            if self.getNivelPlano == "ouro":
                valor = 820
                return valor
            elif self.getNivelPlano == "prata":
                valor = 720
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 620
                return valor
            
        elif self.getIdade >= 60:
            if self.getNivelPlano == "ouro":
                valor = 920
                return valor
            elif self.getNivelPlano == "prata":
                valor = 820
                return valor
            elif self.getNivelPlano == "bronze":
                valor = 720
                return valor

    def calculaValorMensal(self, mes, ano):

        if self.getNivelPlano == "ouro":
            valor_mensal = self.obtemCustoFixo()
            return valor_mensal
        
        elif self.getNivelPlano == "prata":
            valor_mensal = self.obtemCustoFixo()
            convenio = 0 
            nConvenio = 0

            #%50 exames
            for exames in self.getListaServicos:
                if type(exames) is Exame and exames.getAno == ano and exames.getMes == mes:
                    if exames.getClinicaConv == True: # true significa que temos q acrescentar o valor do desconto
                        convenio = convenio + (exames.getValor - exames.getValor * 0.2) /2 # calcula o valor com desconto
                    elif exames.getClinicaConv == False:
                        nConvenio = nConvenio + exames.getValor / 2
                    
                    valor_exames = convenio + nConvenio

            valor_mensal += valor_exames
            return valor_mensal
        
        elif self.getNivelPlano == "bronze":
            valor_mensal = self.obtemCustoFixo()
            valor_consulta = 0
            convenio = 0 
            nConvenio = 0

            #%50 exames e consultas
            for exames in self.getListaServicos:
                if type(exames) is Exame and exames.getAno == ano and exames.getMes == mes:
                   
                    if exames.getClinicaConv == True:
                       convenio = convenio + (exames.getValor - exames.getValor * 0.2) /2
                    elif exames.getClinicaConv == False:
                        nConvenio = nConvenio + exames.getValor / 2
                    valor_exames = convenio + nConvenio

            for consultas in self.getListaServicos :
                if type(consultas) is Consulta and consultas.getAno == ano and consultas.getMes == mes:
                    valor_consulta += (consultas.getValor / 2)

            valor_mensal += valor_exames + valor_consulta
            return valor_mensal
        

    def imprimeServicosMes(self, mes , ano):
        print(f'Paciente {self.getNome}')
        for servico in self.getListaServicos:
            if servico.getAno == ano and servico.getMes == mes:#servico.getAno pega o valor do ano da classe ServicoMedico na funcao getAno
                if type(servico) is Exame:
                    print(f'{servico.getDia}/{servico.getMes}/{servico.getAno} - Exame: {servico.getDescricao} - Clinica: {servico.getNomeClinica}')
                elif type(servico) is Consulta:
                    print(f'{servico.getDia}/{servico.getMes}/{servico.getAno} - Consulta: {servico.getNomeMedico}')
        print(f'Valor: {self.calculaValorMensal(mes, ano)}')
        print()


######################################################################################################


class ServicoMedico:
    def __init__(self, dia, mes, ano, valor) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor

    @property
    def getDia(self):
        return self.__dia
    
    @property
    def getMes(self):
        return self.__mes
    
    @property
    def getAno(self):
        return self.__ano
    
    @property
    def getValor(self):
        return self.__valor
    

class Consulta(ServicoMedico):
    def __init__(self, dia, mes, ano, valor, nomeMedico) -> None:
        super().__init__(dia, mes, ano, valor)
        self.__nomeMedico =nomeMedico

    @property
    def getNomeMedico(self):
        return self.__nomeMedico
    
class Exame(ServicoMedico):
    def __init__(self, dia, mes, ano, valor, descricao, nomeClinica, clinicaConv) -> None:
        super().__init__(dia, mes, ano, valor)
        self.__descricao = descricao
        self.__nomeClinica = nomeClinica
        self.__clinicaConv = clinicaConv

    @property
    def getDescricao(self):
        return self.__descricao

    @property
    def getNomeClinica(self):
        return self.__nomeClinica

    @property
    def getClinicaConv(self):
        return self.__clinicaConv



if __name__ == "__main__": 
    listaPac = [] 
    pac1 = Paciente('João Santos', '111222', 43, 'ouro') 
    pac1.insereConsulta(10, 4, 2023, 300, 'Dr. Antonio Souza') 
   
    pac2 = Paciente('Felipe Mendes', '222333', 35, 'prata') 
    pac2.insereConsulta(14, 4, 2023, 350, 'Dra. Ana Silva') 
    
    pac2.insereExame(18, 4, 2023, 500, 'Ultrasom abdomen', 'Sul Mineira', True) 
    pac3 = Paciente('Márcio Cruz', '333444', 58, 'bronze')
    pac3.insereConsulta(7, 4, 2023, 350, 'Dra. Ana Silva') 
    pac3.insereConsulta(12, 3, 2023, 320, 'Dr. Marcelo Silveira') 
    pac3.insereConsulta(11, 4, 2023, 300, 'Dr. Antonio Souza') 
    pac3.insereExame(22, 4, 2023, 280, 'Raio X Torax', 'Radiologia Ita', False) 
    pac3.insereExame(24, 4, 2023, 250, 'Hemograma Completo', 'LabClin', True) 
    
    listaPac.append(pac1) 
    listaPac.append(pac2) 
    listaPac.append(pac3) 
    for pac in listaPac: 
        pac.imprimeServicosMes(4, 2023)