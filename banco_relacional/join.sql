select cid.nome, est.sigla from estados est, cidades cid 
where est.id_estado = cid.estado_id

select cid.nome, est.sigla, est.regiao 
from estados est inner join cidades cid
on est.id_estado = cid.estado_id