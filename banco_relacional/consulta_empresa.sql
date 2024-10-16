select e.nome Empresa, c.nome Cidade from empresas e, cidades c, empresas_unidade eu
where e.id_empresa = c.id_cidade 
and c.id_cidade = eu.cidade_id and sede