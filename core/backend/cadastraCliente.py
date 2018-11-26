from core.models import Usuario, Cliente, Responsavel, Acidente

def cadastraCliente(request, login, dados):
    user = Usuario.objects.get(loginusuario=login)
    client = Cliente.objects.filter(logincliente=user)
    if client:
        return True
    else:
        if dados['menor18Anos']:
            cliMenor = Responsavel.objects.create(
                loginmenor=user,
                nomeresponsavel=dados['nomeResponsavel'],
                rgresponsavel=dados['rgResponsavel'],
                cpfresponsavel=dados['cpfResponsavel'],
                datanasresponsavel=dados['dataNascResponsavel'],
                enderecoresponsavel=dados['enderecoResponsavel'],
                cepresponsavel=dados['cep'],
                profissaoresponsavel=dados['profissao'],
                telefoneresponsavel=dados['telefone'],
                emailresponsavel=dados['email'])
            cliMenor.save()
        if dados['registoAcidentes']:
            cliAcidente = Acidente.objects.create(
                loginmenor=user,
                dataacidente=dados['dataAcidente'],
                localacidente=dados['localAcidente'],
                lesaoacidente=dados['lesaoAcidente'],
                alergiaacidente=dados['alergiaAcidente'])
            cliAcidente.save()
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
            aspirinacliente=dados['aspirina'],
            herpescliente=dados['herpes'],
            hipertensaocliente=dados['hipertensao'],
            hemofiliacliente=dados['hemofilia'],
            tonturascliente=dados['tontura'],
            cancercliente=dados['cancer'],
            cardiopatiacliente=dados['cardiopatia'],
            hivcliente=dados['hiv'],
            menstruacaocliente=dados['menstruacao'],
            gravidacliente=dados['gravida'],
            amamentandocliente=dados['amamentando'],
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
            alergiaCliente=dados['alergia'],
            outrastatuagenscliente=dados['outrasTatuagens'])
        cli.save()
        return False
