class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = "Disponivel"
        self.cod_livro = cod_livro
        self.usuario = None

    def emprestar_livro(self, usuario):
        if self.status != 'Disponivel':
            return
        
        self.usuario = usuario
        self.status = 'Emprestado'
        
    def devolver_livro(self):
        if self.status != 'Emprestado':
            return 'Não pode ser devolvido!'
        
        self.usuario = None
        self.status = 'Disponivel'



    