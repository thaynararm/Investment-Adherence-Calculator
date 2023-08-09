def percentage_expected_conservador(asset_class_name):
	expected_percentage = {
		'Renda Fixa Pós-Fixada': 70.00,
		'Renda Fixa Inflação': 12.00,
		'Renda Fixa Pré-Fixada': 5.00,
		'Renda Variável': 2.00,
		'Multimercado': 9.00,
		'Alternativos': 0.00,
		'Internacional': 2.00,
	}
	
	return expected_percentage.get(asset_class_name, 0.00)

def percentage_expected_moderado_conservador(asset_class_name):
	expected_percentage = {
		'Renda Fixa Pós-Fixada': 46.00,
		'Renda Fixa Inflação': 16.00,
		'Renda Fixa Pré-Fixada': 8.00,
		'Renda Variável': 4.00,
		'Multimercado': 21.00,
		'Alternativos': 0.00,
		'Internacional': 5.00,
	}
	
	return expected_percentage.get(asset_class_name, 0.00)


def percentage_expected_moderado(asset_class_name):
	expected_percentage = {
		'Renda Fixa Pós-Fixada': 30.00,
		'Renda Fixa Inflação': 24.00,
		'Renda Fixa Pré-Fixada': 10.00,
		'Renda Variável': 7.00,
		'Multimercado': 22.00,
		'Alternativos': 0.00,
		'Internacional': 7.00,
}
	
	return expected_percentage.get(asset_class_name, 0.00)


def percentage_expected_moderado_agressivo(asset_class_name):
	expected_percentage = {
		'Renda Fixa Pós-Fixada': 15.00,
		'Renda Fixa Inflação': 20.00,
		'Renda Fixa Pré-Fixada': 11.00,
		'Renda Variável': 14.00,
		'Multimercado': 30.00,
		'Alternativos': 0.00,
		'Internacional': 10.00,
}
	
	return expected_percentage.get(asset_class_name, 0.00)


def percentage_expected_agressivo(asset_class_name):
	expected_percentage = {
		'Renda Fixa Pós-Fixada': 5.00,
		'Renda Fixa Inflação': 19.00,
		'Renda Fixa Pré-Fixada': 10.00,
		'Renda Variável': 20.00,
		'Multimercado': 31.00,
		'Alternativos': 0.00,
		'Internacional': 15.00,
}
	
	return expected_percentage.get(asset_class_name, 0.00)