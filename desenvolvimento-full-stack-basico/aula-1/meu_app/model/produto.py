from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario

# Utilizaremos o ORM para o mapeamento objeto relacional
# quem implementa o ORM é o sqlalchemy 

# A classe produto herda propriedades da classe base para 
# que sera importada para indicar para o sqlalchemy os meios para entender
# um modelo por completo
class Produto(Base):
    # QUAL TABELA O OBJETO SERA SALVO
    __tablename__ = 'produto'

    # prymary_key = true significa que sera chave primaria
    # O ATRIBUTO id SERA pk_produto NO BANCO DE DADOS, 
    # OS OUTROS ATRIBUTOS TERÃO OS MESMOS NOMES
    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    # caso não seja definido a data é now
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # O COMENTÁRIO É UM ITEM DE OUTRA TABELA MAS O SQLALCHEMY PERMITE FAZER ASSOCIAÇÕES
    # PARA NÃO PRECISAR FAZER JOINS
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)

