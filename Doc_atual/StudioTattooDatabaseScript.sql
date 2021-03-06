create table Tatuador (
	idTatuador Serial,
	nomeTatuador VARCHAR,
	loginTatuador VARCHAR,
	senhaTatuador VARCHAR,
	apiTokens VARCHAR NULL,
	CONSTRAINT pk_Tatuador PRIMARY KEY (idTatuador)
)

create table Cliente (
	idCliente Serial,
	nomeCliente VARCHAR,
	loginCliente VARCHAR,
	senhaCliente VARCHAR,
	assiduidade BOOL NULL,
	CONSTRAINT pk_Cliente PRIMARY KEY (idCliente)
)


create table Agenda (
	idAgenda Serial,
	dataAgenda DATE,
	horarioAgenda TIME,
	CONSTRAINT pk_Agenda PRIMARY KEY (idAgenda)
)

create table Estilos (
	idEstilo Serial,
	estilo VARCHAR,
	CONSTRAINT pk_Estilos PRIMARY KEY (idEstilo)
)

create table Regiao(
	idRegiao SERIAL,
	regiaoDoCorpo VARCHAR,
	faixaValor REAL,
	CONSTRAINT pk_Regiao PRIMARY KEY (idRegiao)
)

create table Cor (
	idCor Serial,
	colorido BOOL,
	faixaValor REAL,
	CONSTRAINT pk_Cor PRIMARY KEY (idCor)
)

create table Tamanho (
	idTamanho Serial,
	tamanho VARCHAR,
	faixaValor REAL,
	CONSTRAINT pk_Tamanho PRIMARY KEY (idTamanho)
)

create table TelefoneCliente (
	idTelefone Serial,
	idCliente INT,
	numeroTelefone VARCHAR,
	CONSTRAINT pk_TelefoneCliente PRIMARY KEY (idTelefone),
	CONSTRAINT fk_Cliente FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
)

create table EmailCliente (
	idEmail Serial,
	idCliente INT,
	enderecoEmail VARCHAR,
	CONSTRAINT pk_EmailCliente PRIMARY KEY (idEmail),
	CONSTRAINT fk_Cliente FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
)

create table Imagens (
	idImagem Serial,
	urlImagem VARCHAR,
	ratins INT,
	idEstilo INT,
	CONSTRAINT pk_Imagem PRIMARY KEY (idImagem),
	CONSTRAINT fk_Estilo FOREIGN KEY (idEstilo) REFERENCES Estilos(idEstilo)
)

create table Portifolio (
	idPortifolio Serial,
	idImagem INT,
	CONSTRAINT pk_Portifolio PRIMARY KEY (idPortifolio),
	CONSTRAINT fk_ImagemPortifolio FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
)

create table Catalogo (
	idCatalogo Serial,
	idImagem INT,
	CONSTRAINT pk_Catalogo PRIMARY KEY (idCatalogo),
	CONSTRAINT fk_ImagemCatalogo FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
)

create table Servicos (
	idServico Serial,
	idCliente INT,
	idImagem INT,
	idCor INT,
	idTamanho INT,
	idRegiao INT,
	servicoDesconto REAL,
	servicoFinalizado BOOL,
	CONSTRAINT pk_Servico PRIMARY KEY (idServico),
	CONSTRAINT fk_ClienteServico FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	CONSTRAINT fk_ImagemServico FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem),
	CONSTRAINT fk_CorServico FOREIGN KEY (idCor) REFERENCES Cor(idCor),
	CONSTRAINT fk_TamanhoServico FOREIGN KEY (idTamanho) REFERENCES Tamanho(idTamanho),
	CONSTRAINT fk_RegiaoServico FOREIGN KEY (idRegiao) REFERENCES Regiao(idRegiao)
)

create table Sessao (
	idSessao Serial,
	idAgenda INT,
	idServico INT,
	CONSTRAINT pk_Sessao PRIMARY KEY (idSessao),
	CONSTRAINT fk_AgendaSessao FOREIGN KEY (idAgenda) REFERENCES Agenda(idAgenda),
	CONSTRAINT fk_ServicoSessao FOREIGN KEY (idServico) REFERENCES Servicos(idServico)
)



