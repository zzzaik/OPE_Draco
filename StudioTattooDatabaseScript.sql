create table Tatuador (
	idTatuador INT AUTO_INCREMENT,
	nomeTatuador VARCHAR(120),
	loginTatuador VARCHAR(100),
	senhaTatuador VARCHAR(300),
	apiTokens VARCHAR(350) NULL,
	CONSTRAINT pk_Tatuador PRIMARY KEY (idTatuador)
);

create table Cliente (
	idCliente INT AUTO_INCREMENT,
	nomeCliente VARCHAR(120),
	loginCliente VARCHAR(100),
	senhaCliente VARCHAR(300),
	assiduidade BOOL NULL,
	CONSTRAINT pk_Cliente PRIMARY KEY (idCliente)
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
	idCliente INT,
	numeroTelefone VARCHAR(15),
	CONSTRAINT pk_TelefoneCliente PRIMARY KEY (idTelefone),
	CONSTRAINT fk_Cliente FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

create table EmailCliente (
	idEmail INT AUTO_INCREMENT,
	idCliente INT,
	enderecoEmail VARCHAR(100),
	CONSTRAINT pk_EmailCliente PRIMARY KEY (idEmail),
	CONSTRAINT fk_Cliente FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

create table Imagens (
	idImagem INT AUTO_INCREMENT,
	urlImagem VARCHAR(350),
	ratins INT,
	idEstilo INT,
	CONSTRAINT pk_Imagem PRIMARY KEY (idImagem),
	CONSTRAINT fk_Estilo FOREIGN KEY (idEstilo) REFERENCES Estilos(idEstilo)
);

create table Portifolio (
	idPortifolio INT AUTO_INCREMENT,
	idImagem INT,
	CONSTRAINT pk_Portifolio PRIMARY KEY (idPortifolio),
	CONSTRAINT fk_ImagemPortifolio FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
);

create table Catalogo (
	idCatalogo INT AUTO_INCREMENT,
	idImagem INT,
	CONSTRAINT pk_Catalogo PRIMARY KEY (idCatalogo),
	CONSTRAINT fk_ImagemCatalogo FOREIGN KEY (idImagem) REFERENCES Imagens(idImagem)
);

create table Servicos (
	idServico INT AUTO_INCREMENT,
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
);

create table Sessao (
	idSessao INT AUTO_INCREMENT,
	idAgenda INT,
	idServico INT,
	CONSTRAINT pk_Sessao PRIMARY KEY (idSessao),
	CONSTRAINT fk_AgendaSessao FOREIGN KEY (idAgenda) REFERENCES Agenda(idAgenda),
	CONSTRAINT fk_ServicoSessao FOREIGN KEY (idServico) REFERENCES Servicos(idServico)
);mysql> status
--------------

Connection id:		64194996
Current database:	zzzaik$JustinoTattooDB
Current user:		zzzaik@10.0.0.4
SSL:			Cipher in use is AES256-SHA
Current pager:		stdout
Using outfile:		'/home/zzzaik/OPE_Draco/StudioTattooDatabaseScript.sql'
Using delimiter:	;
Server version:		5.6.27-log MySQL Community Server (GPL)
Protocol version:	10
Connection:		zzzaik.mysql.pythonanywhere-services.com via TCP/IP
Server characterset:	utf8
Db     characterset:	utf8
Client characterset:	utf8
Conn.  characterset:	utf8
TCP port:		3306
Uptime:			257 days 58 min 55 sec

Threads: 106  Questions: 4267765010  Slow queries: 34643  Opens: 24788501  Flush tables: 1  Open tables: 992  Queries per second avg: 192.169
--------------

mysql> print
--------------

--------------

mysql> ego
ERROR: 
No query specified

mysql> clear
mysql> status
--------------

Connection id:		64194996
Current database:	zzzaik$JustinoTattooDB
Current user:		zzzaik@10.0.0.4
SSL:			Cipher in use is AES256-SHA
Current pager:		stdout
Using outfile:		'/home/zzzaik/OPE_Draco/StudioTattooDatabaseScript.sql'
Using delimiter:	;
Server version:		5.6.27-log MySQL Community Server (GPL)
Protocol version:	10
Connection:		zzzaik.mysql.pythonanywhere-services.com via TCP/IP
Server characterset:	utf8
Db     characterset:	utf8
Client characterset:	utf8
Conn.  characterset:	utf8
TCP port:		3306
Uptime:			257 days 59 min 49 sec

Threads: 105  Questions: 4267809558  Slow queries: 34643  Opens: 24788595  Flush tables: 1  Open tables: 992  Queries per second avg: 192.171
--------------

mysql> print ego
    -> StudioTattooDatabaseScript.sql
    -> ^C
mysql> print
--------------

--------------

mysql> \h

For information about MySQL products and services, visit:
   http://www.mysql.com/
For developer information, including the MySQL Reference Manual, visit:
   http://dev.mysql.com/
To buy MySQL Enterprise support, training, or other products, visit:
   https://shop.mysql.com/

List of all MySQL commands:
Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with $EDITOR.
ego       (\G) Send command to mysql server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to mysql server.
help      (\h) Display this help.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.

For server side help, type 'help contents'

mysql> \x
ERROR 1047 (08S01): Unknown command
mysql> \X
ERROR: 
Unknown command '\X'.
    -> ^C
mysql> resetconnection
ERROR 1047 (08S01): Unknown command
mysql> notee
