--View Vendas
SELECT 
CV.idmarca AS IDMARCA,
M.marca AS MARCA,
CV.idlinha AS IDLINHA,
L.linha AS LINHA,
CV.qtdvenda AS QUANTIDADE,
substring(datavenda,4,2) AS MES,
substring(datavenda,7,2) AS ANO
FROM `boticario-hruthes.RAW_VENDAS.T_RAW_CONSOLIDADO_VENDAS` as CV
left outer join `boticario-hruthes.DIM.LINHAS` L ON L.idlinha=CV.idlinha
left outer join  `boticario-hruthes.DIM.MARCAS` M ON M.idmarca=CV.idmarca
