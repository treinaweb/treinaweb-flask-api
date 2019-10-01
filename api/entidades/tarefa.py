class Tarefa():
    def __init__(self, titulo, descricao, data_expiracao):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_expiracao = data_expiracao

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def data_expiracao(self):
        return self.__data_expiracao

    @data_expiracao.setter
    def data_expiracao(self, data_expiracao):
        self.__data_expiracao = data_expiracao