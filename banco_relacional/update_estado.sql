update estados set nome='Maranhão' where id_estado = 10;

update estados set nome='Paraná' where sigla = 'PR';

update estados set populacao = 11.32 where sigla='PR';
-- select nome, populacao from estados where sigla="PR"

select * from cidades