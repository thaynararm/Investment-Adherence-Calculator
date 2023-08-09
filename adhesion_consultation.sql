-- Esta consulta calcula a aderência das contas à sua política de investimentos.
-- A aderência é medida como a diferença percentual entre a alocação atual e a alocação esperada

SELECT
	account_code, -- Código da conta
	account_suitability, -- Perfil do Investidor
	ROUND(SQRT(SUM(POW(percentage_expected - percentage_current, 2))),2) AS adherence 
	-- Cálculo da aderência percentual usando a fórmula do desvio-padrão

FROM(
	SELECT
		c.account_code, -- Código da conta
		c.account_suitability, -- Perfil do Investidor
		a.class_name, -- Classificação do ativo
		SUM(a.position_value) AS total_position_value_class, -- Valor investido em cada classe
		p.total_position_value_account, -- Valor total da conta
		ROUND((SUM(a.position_value)/p.total_position_value_account)*100, 2) AS percentage_current,
		-- Porcentagem de alocação em cada classe de ativo
		CASE
			WHEN c.account_suitability = 'conservador' THEN
				CASE
					WHEN a.class_name = 'Renda Fixa Pós-Fixada' THEN 70.00
					WHEN a.class_name = 'Renda Fixa Inflação' THEN 12.00
					WHEN a.class_name = 'Renda Fixa Pré-Fixada' THEN 5.00
					WHEN a.class_name = 'Renda Variável' THEN 2.00
					WHEN a.class_name = 'Multimercado' THEN 9.00
					WHEN a.class_name = 'Alternativos' THEN 0.00
					WHEN a.class_name = 'Internacional' THEN 2.00
					ELSE 0.00
				END
			WHEN c.account_suitability = 'moderado-conservador' THEN
				CASE
					WHEN a.class_name = 'Renda Fixa Pós-Fixada' THEN 46.00
					WHEN a.class_name = 'Renda Fixa Inflação' THEN 16.00
					WHEN a.class_name = 'Renda Fixa Pré-Fixada' THEN 8.00
					WHEN a.class_name = 'Renda Variável' THEN 4.00
					WHEN a.class_name = 'Multimercado' THEN 21.00
					WHEN a.class_name = 'Alternativos' THEN 0.00
					WHEN a.class_name = 'Internacional' THEN 5.00
					ELSE 0.00
				END
			WHEN c.account_suitability = 'moderado' THEN
				CASE
					WHEN a.class_name = 'Renda Fixa Pós-Fixada' THEN 30.00
					WHEN a.class_name = 'Renda Fixa Inflação' THEN 24.00
					WHEN a.class_name = 'Renda Fixa Pré-Fixada' THEN 10.00
					WHEN a.class_name = 'Renda Variável' THEN 7.00
					WHEN a.class_name = 'Multimercado' THEN 22.00
					WHEN a.class_name = 'Alternativos' THEN 0.00
					WHEN a.class_name = 'Internacional' THEN 7.00
					ELSE 0.00
				END
			WHEN c.account_suitability = 'moderado-agressivo' THEN
				CASE
					WHEN a.class_name = 'Renda Fixa Pós-Fixada' THEN 15.00
					WHEN a.class_name = 'Renda Fixa Inflação' THEN 20.00
					WHEN a.class_name = 'Renda Fixa Pré-Fixada' THEN 11.00
					WHEN a.class_name = 'Renda Variável' THEN 14.00
					WHEN a.class_name = 'Multimercado' THEN 30.00
					WHEN a.class_name = 'Alternativos' THEN 0.00
					WHEN a.class_name = 'Internacional' THEN 10.00
					ELSE 0.00
				END
			WHEN c.account_suitability = 'agressivo' THEN
				CASE
					WHEN a.class_name = 'Renda Fixa Pós-Fixada' THEN 5.00
					WHEN a.class_name = 'Renda Fixa Inflação' THEN 19.00
					WHEN a.class_name = 'Renda Fixa Pré-Fixada' THEN 10.00
					WHEN a.class_name = 'Renda Variável' THEN 20.00
					WHEN a.class_name = 'Multimercado' THEN 31.00
					WHEN a.class_name = 'Alternativos' THEN 0.00
					WHEN a.class_name = 'Internacional' THEN 15.00
					ELSE 0.0
				END
			ELSE 0.0 -- Valor padrão caso a adequação da conta não se encaixe a nenhum perfil
		END AS percentage_expected
		
	FROM accounts c
	INNER JOIN assets a ON c.account_code = a.account_code

	LEFT JOIN
		(SELECT
			account_code,
			SUM(position_value) AS total_position_value_account
		 FROM assets a
		 GROUP BY account_code) p ON c.account_code = p.account_code

	GROUP BY c.account_code, c.account_suitability, a.class_name, p.total_position_value_account
) AS subquery

GROUP BY subquery.account_code, subquery.account_suitability
ORDER BY adherence