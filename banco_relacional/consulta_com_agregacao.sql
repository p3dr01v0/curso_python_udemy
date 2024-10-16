select regiao as 'Região', sum(populacao) as Total from estados
group by regiao 
order by Total desc

select sum(populacao) as Total from estados

-- avg é a funcao que nos traz a media
select avg(populacao) as Total from estados
