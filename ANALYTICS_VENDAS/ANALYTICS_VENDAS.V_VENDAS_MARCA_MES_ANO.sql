--ANALYTICS_VENDAS.V_VENDAS_MARCA_MES_ANO
SELECT  IDMARCA, MARCA, MES, ANO, SUM(QUANTIDADE) AS CONSOLIDADO_VENDAS, FROM `boticario-hruthes.CURATED_VENDAS.VENDAS` 
GROUP BY MARCA, IDMARCA, MES, ANO
ORDER BY MES, ANO, IDMARCA;