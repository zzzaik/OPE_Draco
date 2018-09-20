create table Usuario (
    idUsuario INT AUTO_INCREMENT,
    loginUsuario VARCHAR(120) NOT NULL,
    senhaUsuario VARCHAR(500) NOT NULL,
    tipoUsuario BOOLEAN DEFAULT FALSE NOT NULL,
    eConfiavel BOOLEAN DEFAULT FALSE NOT NULL,
    CONSTRAINT pk_Usuario PRIMARY KEY (idUsuario)
);

create table Token (
    idTokens INT AUTO_INCREMENT,
    idUsuario INT NOT NULL,
    token VARCHAR(350) NOT NULL,
    tipo BOOLEAN NOT NULL,
    CONSTRAINT pk_Token PRIMARY KEY (idToken),
    CONSTRAINT fk_TokenUsuario FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario)
);

create table Tatuador (
	idTatuador INT AUTO_INCREMENT,
	nomeTatuador VARCHAR(120),
	loginTatuador INT NOT NULL,
	CONSTRAINT pk_Tatuador PRIMARY KEY (idTatuador),
	CONSTRAINT fk_LoginTatuador FOREIGN KEY (loginTatuador) REFERENCES Usuario(idUsuario)
);

create table apiTokens  (
    idApiTokens INT AUTO_INCREMENT,
    Tatuador INT NOT NULL,
    nomeApi VARCHAR(50),
    token VARCHAR(350),
    CONSTRAINT pk_apiTokens PRIMARY KEY (idApiTokens),
    CONSTRAINT fk_Tatuador FOREIGN KEY (Tatuador) REFERENCES Tatuador(idTatuador)
);

create table Cliente (
	idCliente INT AUTO_INCREMENT,
	nomeCliente VARCHAR(120),
	loginCliente INT NOT NULL,
	assiduidade BOOL NULL,
	CONSTRAINT pk_Cliente PRIMARY KEY (idCliente),
	CONSTRAINT fk_LoginCliente FOREIGN KEY (loginCliente) REFERENCES Usuario(idUsuario)
);


create table Agenda (
	idAgenda INT AUTO_INCREMENT,
	dataAgenda DATE,
	horarioAgenda TIME,
	CONSTRAINT pk_Agenda PRIMARY KEY (idAgenda)
);

create table Estilos (
	idEstilo INT AUTO_INCREMENT,
	estilo VARCHAR(50),
	CONSTRAINT pk_Estilos PRIMARY KEY (idEstilo)
);

create table Regiao(
	idRegiao INT AUTO_INCREMENT,
	regiaoDoCorpo VARCHAR(50),
	faixaValor REAL,
	CONSTRAINT pk_Regiao PRIMARY KEY (idRegiao)
);

create table Cor (
	idCor INT AUTO_INCREMENT,
	colorido BOOL,
	faixaValor REAL,
	CONSTRAINT pk_Cor PRIMARY KEY (idCor)
);

create table Tamanho (
	idTamanho INT AUTO_INCREMENT,
	tamanho VARCHAR(8),
	faixaValor REAL,
	CONSTRAINT pk_Tamanho PRIMARY KEY (idTamanho)
);

create table TelefoneCliente (
	idTelefone INT AUTO_INCREMENT,
	idCliente INT NOT NULL,
	numeroTelefone VARCHAR(15),
	CONSTRAINT pk_TelefoneCliente PRIMARY KEY (idTelefone),
	CONSTRAINT fk_Cliente FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

create table EmailCliente (
	idEmail INT AUTO_INCREMENT,
	idCliente INT NOT NULL,
	enderecoEmail VARCHAR(100),
	CONSTRAINT pk_EmailCliente PRIMARY KEY (idEmail),
	CONSTRAINT fk_ClienteTelefone FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

create table Imagem (
	idImagem INT AUTO_INCREMENT,
	urlImagem VARCHAR(350),
	ratins INT NOT NULL,
	idEstilo INT NOT NULL,
	CONSTRAINT pk_Imagem PRIMARY KEY (idImagem),
	CONSTRAINT fk_Estilo FOREIGN KEY (idEstilo) REFERENCES Estilos(idEstilo)
);

create table Tag (
    idTag INT AUTO_INCREMENT,
    tag VARCHAR(50),
    CONSTRAINT pk_Tag PRIMARY KEY (idTag)
);

create table ImagemTag (
    idImagemTag INT AUTO_INCREMENT,
    idImagem INT NOT NULL,
    idTag INT NOT NULL,
    CONSTRAINT pk_ImagemTag PRIMARY KEY (idImagemTag),
    CONSTRAINT fk_Imagem FOREIGN KEY (idImagem) REFERENCES Imagem(idImagem),
    CONSTRAINT fk_Tag FOREIGN KEY (idTag) REFERENCES Tag(idTag)
);

create table Portifolio (
	idPortifolio INT AUTO_INCREMENT,
	idImagem INT NOT NULL,
	CONSTRAINT pk_Portifolio PRIMARY KEY (idPortifolio),
	CONSTRAINT fk_ImagemPortifolio FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
);

create table Catalogo (
	idCatalogo INT AUTO_INCREMENT,
	idImagem INT NOT NULL,
	CONSTRAINT pk_Catalogo PRIMARY KEY (idCatalogo),
	CONSTRAINT fk_ImagemCatalogo FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
);

create table Servicos (
	idServico INT AUTO_INCREMENT,
	idCliente INT NOT NULL,
	idImagem INT NOT NULL,
	idCor INT NOT NULL,
	idTamanho INT NOT NULL,
	idRegiao INT NOT NULL,
	servicoDesconto REAL,
	servicoFinalizado BOOL,
	CONSTRAINT pk_Servico PRIMARY KEY (idServico),
	CONSTRAINT fk_ClienteServico FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	CONSTRAINT fk_ImagemServico FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem),
	CONSTRAINT fk_CorServico FOREIGN KEY (idCor) REFERENCES Cor(idCor),
	CONSTRAINT fk_TamanhoServico FOREIGN KEY (idTamanho) REFERENCES Tamanho(idTamanho),
	CONSTRAINT fk_RegiaoServico FOREIGN KEY (idRegiao) REFERENCES Regiao(idRegiao)
);

create table Sessao (
	idSessao INT AUTO_INCREMENT,
	idAgenda INT NOT NULL,
	idServico INT NOT NULL,
	CONSTRAINT pk_Sessao PRIMARY KEY (idSessao),
	CONSTRAINT fk_AgendaSessao FOREIGN KEY (idAgenda) REFERENCES Agenda(idAgenda),
	CONSTRAINT fk_ServicoSessao FOREIGN KEY (idServico) REFERENCES Servicos(idServico)
);