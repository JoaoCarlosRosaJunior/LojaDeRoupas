from django.contrib import admin
from .models import Carrinho, Categoria, ItemCarrinho,Produto
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome","slug")
    prepopulated_fields = { "slug": ("nome",)}
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "preco"]
    list_editable = ( "preco",)
    prepopulated_fields = { "slug": ("titulo",)}

@admin.register(Carrinho)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    pass