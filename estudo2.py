idade: int
salario: format
nome: str
sexo: str

idade = 24
salario = 8000
nome = "Victor Mosse"
sexo = "M"

print(f"O funcionario {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

print("O funcionario {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))