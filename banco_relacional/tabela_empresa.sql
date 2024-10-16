create table if not exists empresas(
    id_empresa int unsigned not null auto_increment,
    nome varchar(225) not null,
    cnpj int unsigned,
    primary key (id_empresa),
    unique key(cnpj)
);

create table if not exists empresas_unidade(
    empresa_id int unsigned not null,
    cidade_id int unsigned not null,
    sede tinyint(1) not null,
    primary key(empresa_id, cidade_id)
);