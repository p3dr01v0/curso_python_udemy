insert into cidades(nome, area, estado_id) values
('Campinas', 795, 25),
('Niterói', 133.9, 19);

insert into cidades(nome, area, estado_id) values
('Caruaru', 920.6, (select id_estado from estados where sigla = 'PE')),
('Juazeiro do Norte', 248.2, (select id_estado from estados where sigla = 'CE'));

select * from cidades

select * from estados