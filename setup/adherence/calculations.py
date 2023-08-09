from decimal import Decimal
from django.db.models import Sum
from .queries import percentage_expected_conservador, percentage_expected_moderado_conservador, percentage_expected_moderado, percentage_expected_moderado_agressivo, percentage_expected_agressivo


def calculate_adherence(account, assets):
    account_position_values = assets.values_list('position_value', flat=True) 
    account_position_values_sum = sum(account_position_values) 
    asset_sum_by_class = assets.values('class_name').annotate(total_value=Sum('position_value')) 

    adherence = 0
    class_discrepancies = {}
	
    for asset_class in asset_sum_by_class:
        class_name = asset_class['class_name']
        total_value = asset_class['total_value'] 
        percentage_current = round(((Decimal(total_value)/Decimal(account_position_values_sum))*100), 2)

        percentage_expected = get_expected_percentage(account, class_name)
        
        discrepancy = round(((Decimal(percentage_expected) - Decimal(percentage_current)) ** 2),2)
        class_discrepancies[class_name] = discrepancy

        adherence += discrepancy

    max_discrepancy_class = max(class_discrepancies, key=class_discrepancies.get)
	
    adherence = round((adherence ** Decimal(0.5)), 2)

    return adherence, max_discrepancy_class
    

def get_expected_percentage(account, class_name):
	suitability_mapping = {
		'conservador': percentage_expected_conservador,
		'moderado-conservador': percentage_expected_moderado_conservador,
		'moderado': percentage_expected_moderado,
		'moderado-agressivo': percentage_expected_moderado_agressivo,
		'agressivo': percentage_expected_agressivo,
	}

	suitability_function = suitability_mapping.get(account.account_suitability, lambda _: 0.00)
	return suitability_function(class_name)
