from core.models import Usuario, Cliente, Responsavel, Acidente

def cadastraCliente(login, dados):
    msg = ''
    user = Usuario.objects.get(loginusuario=login)
    client = Cliente.objects.filter(logincliente=user)
    if client:
        msg = 'Usuário já é cliente'
        return msg
    else:
        cli = Cliente.objects.create(
            logincliente=user,
            nomecliente=dados['nome'],
            generocliente=dados['genero'],
            datanasccliente=dados['dataNasc'],
            rgcliente=dados['rg'],
            cpfcliente=dados['cpf'],
            enderecocliente=dados['endereco'],
            foneresidencialcliente=dados['foneResidencial'],
            telefonecliente=dados['celular'],
            emailcliente=dados['email'],
            pesocliente=dados['peso'],
            alturacliente=dados['altura'],
            aspitinacliente=dados['aspirina'],
            herpescliente=dados['herpes'],
            hipertensaocliente=dados['hipertensao'],
            hemofiliacliente=dados['hemofilia'],
            tonturascliente=dados['tontura'],
            cancercliente=dados['cancer'],
            cardiopatiacliente=dados['cardiopatia'],
            hivcliente=dados['hiv'],
            menstruadacliente=dados['menstruacao'],
            gravidacliente=dados['gravida'],
            amamentadocliente=dados['amamentando'],
            asmacliente=dados['asma'],
            colesterolcliente=dados['colesterol'],
            eplepsiacliente=dados['eplepsia'],
            problemarenalcliente=dados['problemaRenal'],
            diabetescliente=dados['diabetes'],
            marcapassocliente=dados['marcaPasso'],
            lupuscliente=dados['lupus'],
            circulatoriocliente=dados['circulatorio'],
            glaucomacliente=dados['glaucoma'],
            respiratoriocliente=dados['respiratorio'],
            psoriasecliente=dados['psoriase'],
            hepatitecliente=dados['hepatite'],
            coagulacaocliente=dados['coagulacao'],
            depressaocliente=dados['depressao'],
            gripeh1n1cliente=dados['gripeh1n1'],
            alergiacliente=dados['alergia'],
            outrastatuagenscliente=dados['outrasTatuagens'])

        msg = 'Cliente Registrado'
        cli.save()

        clientDB = Cliente.objects.get(logincliente=user)
        if dados['menor18Anos']:

            cliMenor = Responsavel.objects.create(
                loginmenor=clientDB,
                nomeresponsavel=dados['nomeResponsavel'],
                rgresponsavel=dados['rgResponsavel'],
                cpfresponsavel=dados['cpfResponsavel'],
                datanascresponsavel=dados['dataNascResponsavel'],
                enderecoresponsavel=dados['enderecoResponsavel'],
                cepresponsavel=dados['cep'],
                profissaoresponsavel=dados['profissao'],
                telefoneresponsavel=dados['telefone'],
                emailresponsavel=dados['email'])
            cliMenor.save()

        if dados['registoAcidentes']:
            cliAcidente = Acidente.objects.create(
                loginmenor=clientDB,
                dataacidente=dados['dataAcidente'],
                localacidente=dados['localAcidente'],
                lesaoacidente=dados['lesaoAcidente'],
                alergiaacidente=dados['alergiaAcidente'])
            cliAcidente.save()
    return msg
