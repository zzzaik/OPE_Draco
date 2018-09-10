# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    idagenda = models.AutoField(db_column='idAgenda', primary_key=True)  # Field name made lowercase.
    dataagenda = models.DateField(db_column='dataAgenda', blank=True, null=True)  # Field name made lowercase.
    horarioagenda = models.TimeField(db_column='horarioAgenda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agenda'


class Catalogo(models.Model):
    idcatalogo = models.AutoField(db_column='idCatalogo', primary_key=True)  # Field name made lowercase.
    idimagem = models.ForeignKey('Imagens', models.DO_NOTHING, db_column='idImagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Catalogo'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nomecliente = models.CharField(db_column='nomeCliente', max_length=120, blank=True, null=True)  # Field name made lowercase.
    logincliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='loginCliente')  # Field name made lowercase.
    assiduidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'


class Cor(models.Model):
    idcor = models.AutoField(db_column='idCor', primary_key=True)  # Field name made lowercase.
    colorido = models.IntegerField(blank=True, null=True)
    faixavalor = models.FloatField(db_column='faixaValor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cor'


class Emailcliente(models.Model):
    idemail = models.AutoField(db_column='idEmail', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    enderecoemail = models.CharField(db_column='enderecoEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmailCliente'


class Estilos(models.Model):
    idestilo = models.AutoField(db_column='idEstilo', primary_key=True)  # Field name made lowercase.
    estilo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Estilos'


class Imagens(models.Model):
    idimagem = models.AutoField(db_column='idImagem', primary_key=True)  # Field name made lowercase.
    urlimagem = models.CharField(db_column='urlImagem', max_length=350, blank=True, null=True)  # Field name made lowercase.
    ratins = models.IntegerField()
    idestilo = models.ForeignKey(Estilos, models.DO_NOTHING, db_column='idEstilo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Imagens'


class Portifolio(models.Model):
    idportifolio = models.AutoField(db_column='idPortifolio', primary_key=True)  # Field name made lowercase.
    idimagem = models.ForeignKey(Imagens, models.DO_NOTHING, db_column='idImagem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Portifolio'


class Regiao(models.Model):
    idregiao = models.AutoField(db_column='idRegiao', primary_key=True)  # Field name made lowercase.
    regiaodocorpo = models.CharField(db_column='regiaoDoCorpo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faixavalor = models.FloatField(db_column='faixaValor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regiao'


class Servicos(models.Model):
    idservico = models.AutoField(db_column='idServico', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    idimagem = models.ForeignKey(Imagens, models.DO_NOTHING, db_column='idImagem')  # Field name made lowercase.
    idcor = models.ForeignKey(Cor, models.DO_NOTHING, db_column='idCor')  # Field name made lowercase.
    idtamanho = models.ForeignKey('Tamanho', models.DO_NOTHING, db_column='idTamanho')  # Field name made lowercase.
    idregiao = models.ForeignKey(Regiao, models.DO_NOTHING, db_column='idRegiao')  # Field name made lowercase.
    servicodesconto = models.FloatField(db_column='servicoDesconto', blank=True, null=True)  # Field name made lowercase.
    servicofinalizado = models.IntegerField(db_column='servicoFinalizado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Servicos'


class Sessao(models.Model):
    idsessao = models.AutoField(db_column='idSessao', primary_key=True)  # Field name made lowercase.
    idagenda = models.ForeignKey(Agenda, models.DO_NOTHING, db_column='idAgenda')  # Field name made lowercase.
    idservico = models.ForeignKey(Servicos, models.DO_NOTHING, db_column='idServico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessao'


class Tamanho(models.Model):
    idtamanho = models.AutoField(db_column='idTamanho', primary_key=True)  # Field name made lowercase.
    tamanho = models.CharField(max_length=8, blank=True, null=True)
    faixavalor = models.FloatField(db_column='faixaValor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tamanho'


class Tatuador(models.Model):
    idtatuador = models.AutoField(db_column='idTatuador', primary_key=True)  # Field name made lowercase.
    nometatuador = models.CharField(db_column='nomeTatuador', max_length=120, blank=True, null=True)  # Field name made lowercase.
    logintatuador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='loginTatuador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tatuador'


class Telefonecliente(models.Model):
    idtelefone = models.AutoField(db_column='idTelefone', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    numerotelefone = models.CharField(db_column='numeroTelefone', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TelefoneCliente'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    loginusuario = models.CharField(db_column='loginUsuario', max_length=120)  # Field name made lowercase.
    senhausuario = models.CharField(db_column='senhaUsuario', max_length=500)  # Field name made lowercase.
    tipousuario = models.IntegerField(db_column='tipoUsuario')  # Field name made lowercase.
    econfiavel = models.IntegerField(db_column='eConfiavel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class Apitokens(models.Model):
    idapitokens = models.AutoField(db_column='idApiTokens', primary_key=True)  # Field name made lowercase.
    tatuador = models.ForeignKey(Tatuador, models.DO_NOTHING, db_column='Tatuador')  # Field name made lowercase.
    nomeapi = models.CharField(db_column='nomeApi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiTokens'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

    def __str__():
        return "%s, %s, %s" %(self.session_key, self.session_data, self.expire_date)
