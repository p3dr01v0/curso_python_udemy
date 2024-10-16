alter table empresas modify cnpj varchar(14)

insert into empresas(nome, cnpj) values
('Bradesco', 12345678901234),
('Vale', 09876543211234),
('Cielo', 01928374651234);

insert into empresas_unidade(empresa_id, cidade_id, sede) values
(1,1,1),
(1,2,0),
(2,1,0),
(2,2,1);