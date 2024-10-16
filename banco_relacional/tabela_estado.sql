-- criando a tabela estados

create table estados(
    	id_estado int UNSIGNED not null AUTO_INCREMENT,
        nome varchar(50) not null,
        sigla varchar(2) not null,
        regiao ENUM('Norte', 'Nordeste', 'Sul', 'Sudeste', 'Oeste', 'Centro-Oeste', 'Leste') not null,
        populacao decimal(5, 2),
        primary key(id_estado),
        UNIQUE KEY (nome),
        UNIQUE KEY (sigla)
);