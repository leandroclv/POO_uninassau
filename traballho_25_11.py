class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True


class Usuario:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def relatorio_livros_disponiveis(self):
        return [livro.titulo for livro in self.livros if livro.disponivel]

    def relatorio_usuarios_com_livros_emprestados(self):
        return [(usuario.nome, [livro.titulo for livro in usuario.livros_emprestados]) for usuario in self.usuarios if usuario.livros_emprestados]
