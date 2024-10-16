create table if not exists prefeitos(
    id_prefeito int unsigned not null auto_increment,
    nome varchar(225) not null,
    cidade_id int unsigned,
    primary key(id_prefeito),
    foreign key(cidade_id) references cidades(id_cidade),
    unique key(cidade_id)
);

select * from prefeitos