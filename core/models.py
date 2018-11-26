# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acidente(models.Model):
    idacidente = models.AutoField(db_column='idAcidente', primary_key=True)  # Field name made lowercase.
    loginmenor = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='loginMenor')  # Field name made lowercase.
    dataacidente = models.DateField(db_column='dataAcidente')  # Field name made lowercase.
    localacidente = models.CharField(db_column='localAcidente', max_length=100)  # Field name made lowercase.
    descriacaoacidente = models.CharField(db_column='descriacaoAcidente', max_length=500)  # Field name made lowercase.
    lesaoacidente = models.IntegerField(db_column='lesaoAcidente')  # Field name made lowercase.
    alergiaacidente = models.IntegerField(db_column='alergiaAcidente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Acidente'


class Agenda(models.Model):
    idagenda = models.AutoField(db_column='idAgenda', primary_key=True)  # Field name made lowercase.
    dataagenda = models.DateField(db_column='dataAgenda', blank=True, null=True)  # Field name made lowercase.
    horarioagenda = models.TimeField(db_column='horarioAgenda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agenda'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nomecliente = models.CharField(db_column='nomeCliente', max_length=120, blank=True, null=True)  # Field name made lowercase.
    logincliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='loginCliente')  # Field name made lowercase.
    assiduidade = models.IntegerField(blank=True, null=True)
    datanasccliente = models.DateField(db_column='dataNascCliente')  # Field name made lowercase.
    rgcliente = models.CharField(db_column='rgCliente', max_length=12)  # Field name made lowercase.
    cpfcliente = models.CharField(db_column='cpfCliente', max_length=14)  # Field name made lowercase.
    enderecocliente = models.CharField(db_column='enderecoCliente', max_length=300)  # Field name made lowercase.
    foneresidencialcliente = models.CharField(db_column='foneResidencialCliente', max_length=8, blank=True, null=True)  # Field name made lowercase.
    telefonecliente = models.CharField(db_column='telefoneCliente', max_length=9, blank=True, null=True)  # Field name made lowercase.
    emailcliente = models.CharField(db_column='emailCliente', max_length=150)  # Field name made lowercase.
    pesocliente = models.CharField(db_column='pesoCliente', max_length=6, blank=True, null=True)  # Field name made lowercase.
    alturacliente = models.CharField(db_column='alturaCliente', max_length=6, blank=True, null=True)  # Field name made lowercase.
    aspitinacliente = models.IntegerField(db_column='aspitinaCliente')  # Field name made lowercase.
    herpescliente = models.IntegerField(db_column='herpesCliente')  # Field name made lowercase.
    hipertensaocliente = models.IntegerField(db_column='hipertensaoCliente')  # Field name made lowercase.
    hemofiliacliente = models.IntegerField(db_column='hemofiliaCliente')  # Field name made lowercase.
    tonturascliente = models.IntegerField(db_column='tonturasCliente')  # Field name made lowercase.
    cancercliente = models.IntegerField(db_column='cancerCliente')  # Field name made lowercase.
    cardiopatiacliente = models.IntegerField(db_column='cardiopatiaCliente')  # Field name made lowercase.
    hivcliente = models.IntegerField(db_column='hivCliente')  # Field name made lowercase.
    menstruadacliente = models.IntegerField(db_column='menstruadaCliente')  # Field name made lowercase.
    gravidacliente = models.IntegerField(db_column='gravidaCliente')  # Field name made lowercase.
    amamentadocliente = models.IntegerField(db_column='amamentadoCliente')  # Field name made lowercase.
    asmacliente = models.IntegerField(db_column='asmaCliente')  # Field name made lowercase.
    colesterolcliente = models.IntegerField(db_column='colesterolCliente')  # Field name made lowercase.
    eplepsiacliente = models.IntegerField(db_column='eplepsiaCliente')  # Field name made lowercase.
    problemarenalcliente = models.IntegerField(db_column='problemaRenalCliente')  # Field name made lowercase.
    diabetescliente = models.IntegerField(db_column='diabetesCliente')  # Field name made lowercase.
    marcapassocliente = models.IntegerField(db_column='marcaPassoCliente')  # Field name made lowercase.
    lupuscliente = models.IntegerField(db_column='lupusCliente')  # Field name made lowercase.
    circulatoriocliente = models.IntegerField(db_column='circulatorioCliente')  # Field name made lowercase.
    glaucomacliente = models.IntegerField(db_column='glaucomaCliente')  # Field name made lowercase.
    respiratoriocliente = models.IntegerField(db_column='respiratorioCliente')  # Field name made lowercase.
    psoriasecliente = models.IntegerField(db_column='psoriaseCliente')  # Field name made lowercase.
    hepatitecliente = models.IntegerField(db_column='hepatiteCliente')  # Field name made lowercase.
    coagulacaocliente = models.IntegerField(db_column='coagulacaoCliente')  # Field name made lowercase.
    depressaocliente = models.IntegerField(db_column='depressaoCliente')  # Field name made lowercase.
    gripeh1n1cliente = models.IntegerField(db_column='gripeH1n1Cliente')  # Field name made lowercase.
    alergiacliente = models.CharField(db_column='alergiaCliente', max_length=500)  # Field name made lowercase.
    outrastatuagenscliente = models.CharField(db_column='outrasTatuagensCliente', max_length=500)  # Field name made lowercase.
    generocliente = models.CharField(db_column='generoCliente', max_length=6)  # Field name made lowercase.

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


class Estilo(models.Model):
    idestilo = models.AutoField(db_column='idEstilo', primary_key=True)  # Field name made lowercase.
    estilo = models.CharField(max_length=50, blank=True, null=True)
    complexidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Estilo'


class Imagem(models.Model):
    idimagem = models.AutoField(db_column='idImagem', primary_key=True)  # Field name made lowercase.
    urlimagem = models.CharField(db_column='urlImagem', unique=True, max_length=255)  # Field name made lowercase.
    ratins = models.IntegerField(blank=True, null=True)
    idestilo = models.ForeignKey(Estilo, models.DO_NOTHING, db_column='idEstilo', blank=True, null=True)  # Field name made lowercase.
    fonteimagem = models.IntegerField(db_column='fonteImagem')  # Field name made lowercase.
    idtag = models.IntegerField(db_column='idTag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Imagem'


class PromoImagem(models.Model):
    idpromo = models.ForeignKey('Promocao', models.DO_NOTHING, db_column='idPromo', blank=True, null=True)  # Field name made lowercase.
    idimagem = models.ForeignKey(Imagem, models.DO_NOTHING, db_column='idImagem', blank=True, null=True)  # Field name made lowercase.
    validade = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PromoImagem'


class Promocao(models.Model):
    idpromo = models.AutoField(db_column='idPromo', primary_key=True)  # Field name made lowercase.
    desconto = models.FloatField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Promocao'


class Regiao(models.Model):
    idregiao = models.AutoField(db_column='idRegiao', primary_key=True)  # Field name made lowercase.
    regiaodocorpo = models.CharField(db_column='regiaoDoCorpo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    faixavalor = models.FloatField(db_column='faixaValor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regiao'


class Responsavel(models.Model):
    idresponsavel = models.AutoField(db_column='idResponsavel', primary_key=True)  # Field name made lowercase.
    loginmenor = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='loginMenor', blank=True, null=True)  # Field name made lowercase.
    rgresponsavel = models.CharField(db_column='rgResponsavel', max_length=12)  # Field name made lowercase.
    cpfresponsavel = models.CharField(db_column='cpfResponsavel', max_length=14)  # Field name made lowercase.
    datanascresponsavel = models.DateField(db_column='dataNascResponsavel', blank=True, null=True)  # Field name made lowercase.
    enderecoresponsavel = models.CharField(db_column='enderecoResponsavel', max_length=300)  # Field name made lowercase.
    cepresponsavel = models.CharField(db_column='cepResponsavel', max_length=9)  # Field name made lowercase.
    profissaoresponsavel = models.CharField(db_column='profissaoResponsavel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefoneresponsavel = models.CharField(db_column='telefoneResponsavel', max_length=9)  # Field name made lowercase.
    emailresponsavel = models.CharField(db_column='emailResponsavel', max_length=100)  # Field name made lowercase.
    nomeresponsavel = models.CharField(db_column='nomeResponsavel', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsavel'


class Servico(models.Model):
    idservico = models.AutoField(db_column='idServico', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    idimagem = models.ForeignKey(Imagem, models.DO_NOTHING, db_column='idImagem')  # Field name made lowercase.
    idcor = models.ForeignKey(Cor, models.DO_NOTHING, db_column='idCor')  # Field name made lowercase.
    idtamanho = models.ForeignKey('Tamanho', models.DO_NOTHING, db_column='idTamanho')  # Field name made lowercase.
    idregiao = models.ForeignKey(Regiao, models.DO_NOTHING, db_column='idRegiao')  # Field name made lowercase.
    servicodesconto = models.FloatField(db_column='servicoDesconto', blank=True, null=True)  # Field name made lowercase.
    servicofinalizado = models.IntegerField(db_column='servicoFinalizado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Servico'


class Sessao(models.Model):
    idsessao = models.AutoField(db_column='idSessao', primary_key=True)  # Field name made lowercase.
    idagenda = models.ForeignKey(Agenda, models.DO_NOTHING, db_column='idAgenda')  # Field name made lowercase.
    idservico = models.ForeignKey(Servico, models.DO_NOTHING, db_column='idServico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessao'


class Tag(models.Model):
    idtag = models.AutoField(db_column='idTag', primary_key=True)  # Field name made lowercase.
    tag = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tag'


class Tamanho(models.Model):
    idtamanho = models.AutoField(db_column='idTamanho', primary_key=True)  # Field name made lowercase.
    tamanho = models.CharField(max_length=20, blank=True, null=True)
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


class Token(models.Model):
    idtoken = models.AutoField(db_column='idToken', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    token = models.CharField(max_length=350)
    tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Token'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    loginusuario = models.CharField(db_column='loginUsuario', max_length=120)  # Field name made lowercase.
    senhausuario = models.CharField(db_column='senhaUsuario', max_length=500)  # Field name made lowercase.
    tipousuario = models.IntegerField(db_column='tipoUsuario')  # Field name made lowercase.
    econfiavel = models.IntegerField(db_column='eConfiavel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class Apitoken(models.Model):
    idapitokens = models.AutoField(db_column='idApiTokens', primary_key=True)  # Field name made lowercase.
    tatuador = models.ForeignKey(Tatuador, models.DO_NOTHING, db_column='Tatuador')  # Field name made lowercase.
    nomeapi = models.CharField(db_column='nomeApi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apiToken'


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
