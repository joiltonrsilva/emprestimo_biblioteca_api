from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField("Nome", max_length=35, null=False, blank=False)
    autor = models.CharField("Autor", max_length=20, null=False, blank=False)
    ano_publicacao = models.DecimalField("Ano de Publicação", max_digits=4, decimal_places=0, null=False, blank=False)
    editora = models.CharField("Editora", max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
    
    def __str__(self) -> str:
        return self.titulo

class Emprestimo(models.Model):
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="livro", null=False)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="usuario", related_name="todos", null=False)
    data_emprestimo = models.DateField("Data de Empréstimo", null=False, blank=False)
    data_devolucao = models.DateField("Data de Devolução", null=False, blank=False)

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"
    
    def __str__(self) -> str:
        return f"{self.usuario_id.username, self.livro_id.titulo, self.data_emprestimo, self.data_devolucao}"