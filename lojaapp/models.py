from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128,unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="imagens/")
    slug = models.SlugField(max_length=128)
    preco = models.DecimalField(max_digits=9,decimal_places=2)

    class Meta:
        verbose_name_plural = "Produtos"
        ordering = ("-criado_em",)

    def __str__(self):
        return self.titulo

    def format_preco(self):
        return "R$ " + str(self.preco).replace(".",",")

class ItemCarrinho(models.Model):
    produto = models.OneToOneField(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.quantidade) + "x - " + str(self.produto.titulo)

class Carrinho(models.Model):
    items = models.ManyToManyField(ItemCarrinho,blank=True )
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)

    def count(self):
        total = 0
        for i in ItemCarrinho.objects.all():
            total += i.quantidade
        return total

    def value_format(self):
        total = 0
        for i in ItemCarrinho.objects.all():
            total += i.produto.preco*i.quantidade
        return "R$ " + str(round(total,2)).replace(".",",")


    def __str__(self):
        return "Carrinho:" + str(self.usuario)


