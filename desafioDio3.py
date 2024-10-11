# Desafio dio 3: escrevendo classes de um jogo

# Primeiro, criando a classe conforme especificado no desafio
class UmHeroi:

    def __init__ (self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        match tipo:
            case "mago":
                self.ataque = "magia"
            case "guerreiro":
                self.ataque = "espada"
            case "monge":
                self.ataque = "artes marciais"
            case "ninja":
                self.ataque = "shuriken"
            case _:
                self.ataque = "um ataque estranho"

    def atacar(self):
        print(f"o {self.tipo} atacou usando {self.ataque}")


# Classe criada, agora obtendo dados para criar um objeto e chamar o método atacar
nome = input("Digite o nome do herói")
idade = int(input("Digite a idade do herói"))
tipo = input("Digite a classe do herói")
heroi = UmHeroi(nome, idade, tipo)
heroi.atacar()
input() # Chamada de input pra efeitos de acessibilidade