-- selecione os trechos que vc queira executar

select * from estados

select sigla, nome as 'Nome dos estados' from estados

select sigla, nome from estados where regiao='sul'

-- order by estamos ordenando que seja exibido da menor para a maoir
select nome, populacao from estados where populacao >= 10 order by populacao

-- usando o desc é exibido do maior para o menor
select nome, populacao from estados where populacao >= 10 order by populacao desc