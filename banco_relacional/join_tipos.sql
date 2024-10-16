select p.nome as 'Prefeito', c.nome as 'Cidade' 
from prefeitos p 
inner join cidades c 
on p.cidade_id = c.id_cidade;

select * from cidades c inner join prefeitos p on p.cidade_id = c.id_cidade;

select * from cidades c left join prefeitos p on p.cidade_id = c.id_cidade;

select * from cidades c right join prefeitos p on p.cidade_id = c.id_cidade;
-- select * from cidades c full join prefeitos p on p.cidade_id = c.id_cidade

select * from cidades c left join prefeitos p on p.cidade_id = c.id_cidade
union
select * from cidades c right join prefeitos p on p.cidade_id = c.id_cidade;