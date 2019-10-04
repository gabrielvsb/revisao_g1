from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Documento, Processo, PedidoDePrazo, EnvioDeProcesso, PortariaDeInstauracao, Tramite


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Processo)
class ProcessoAdmin(admin.ModelAdmin):
    pass

@admin.register(Documento)
class DocumentoaAdmin(admin.ModelAdmin):
    pass

@admin.register(PedidoDePrazo)
class PedidoDePrazoAdmin(admin.ModelAdmin):
    pass

@admin.register(EnvioDeProcesso)
class EnvioDeProcessoAdmin(admin.ModelAdmin):
    pass

@admin.register(PortariaDeInstauracao)
class PortariaDeInstauracaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tramite)
class TramiteAdmin(admin.ModelAdmin):
    pass