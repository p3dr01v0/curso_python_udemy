create table if not exists cidades(
    id_cidade int unsigned not null auto_increment,
    nome varchar(225) not null,
    estado_id int unsigned not null,
    area decimal(10, 2),
    primary key(id_cidade),
    foreign key(estado_id) references estados(id_estado)
);

-- create table if not exists teste(
--     id int auto_increment primary key
-- );

-- drop table if exists teste;
