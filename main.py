from pessoa import Pessoa
from cliente import Cliente
from funcionario import Funcionario

pessoa = Pessoa (
                   input ("Digite seu nome:>>"),
                   input('Digite seu sobrenome:>>'),
                   input('Digite sua idade:>>'),
                   input('Digite seu cpf:>>'),
                   input('Digite seu telefone:>>'),
                   input('Digite sua carteira de trabalho:>>'),
                   input('Digite a sua profissão: >>')
                   )
                                  
cliente = Cliente()

funcionario = Funcionario()

cliente.Nome = pessoa.Nome
cliente.Sobrenome = pessoa.Sobrenome
cliente.Idade = pessoa.Idade
cliente.Telefone = pessoa.Telefone


funcionario.Nome = pessoa.Nome
funcionario.Sobrenome = pessoa.Sobrenome
funcionario.Carteiradetrabalho = pessoa.Carteiradetrabalho
funcionario.profissao = pessoa.profissao


        
        
        
