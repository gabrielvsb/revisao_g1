from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=128)
    cpf = models.CharField("CPF", max_length=50)
    email = models.EmailField('E-mail', null=True, blank=True)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField("Matricula", max_length=50)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField("Nome do departamento",max_length=128)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    numero = models.IntegerField()
    data_criacao = models.DateField("Data de criação", blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, verbose_name="Funcionario", null = True)
    local = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null = True)
    interessados = models.ManyToManyField(Pessoa, related_name="pessoa")
    investigados = models.ManyToManyField(Pessoa, related_name="pessoa1")
    
    
    def __str__(self):
        return "Processo: {}".format(self.numero)

class Documento(models.Model):
    titulo = models.CharField("Titulo", max_length=128)
    conteudo = models.TextField("Conteudo")
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class PortariaDeInstauracao(Documento):
    class meta:
        verbose_name="Portaria de Instauração"
        verbose_name_plural="Portarias de instaurações"

    def __str__(self):
        return self.titulo

class PedidoDePrazo(Documento):
    justificativa = models.TextField("Justificativa")
    data_nova = models.DateField("Novo prazo", blank=True, null=True)
    
    def __str__(self):
        return self.titulo

class EnvioDeProcesso(Documento):
    departamento = models.ForeignKey(Departamento, related_name="departamento", on_delete=models.SET_NULL, null = True)
    data_envio = models.DateField("Data de envio", blank=True, null=True)

    def __str__(self):
        return self.titulo    
    
class Tramite(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, null = True)
    departamento_inicio = models.ForeignKey(Departamento, related_name="departamento2", on_delete=models.SET_NULL, null = True)
    departamento_destino = models.ForeignKey(Departamento, related_name="departamento1", on_delete=models.SET_NULL, null = True)
    data_tramite = models.DateField("Data do tramite", blank=True, null=True)

    def __str__(self):
        return "Tramite do processo: {}".format(self.processo.numero)

    
