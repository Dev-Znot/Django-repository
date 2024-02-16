from django.contrib import admin
from .models import Categoria,Produtos


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'categoria') # Define quais campos do modelo serão exibidos na lista de registros no painel
    list_display_links = ('valor',) # Define quais campos na lista de registros serão links para a página de detalhes do registro.
    list_filter = ('categoria',) # Permite filtrar os registros com base nos valores de determinados campos.
    list_select_related = False # Determina se deve ser utilizado select_related ao recuperar os registros da lista.
    list_per_page = 100 # Define o número de registros exibidos por página na lista.
    list_max_show_all = 200 # Define o número máximo de registros que podem ser exibidos na lista completa (sem paginação).
    list_editable = ('categoria',) # Permite a edição de campos diretamente na lista de registros.
    search_fields = ('nome',) # Especifica os campos pelos quais é possível realizar buscas.