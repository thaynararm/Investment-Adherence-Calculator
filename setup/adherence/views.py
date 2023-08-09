from django.shortcuts import render
from .models import Accounts, Assets
from .calculations import calculate_adherence


def index(request):
	results = []

	accounts = Accounts.objects.all()

	for account in accounts:
		assets = Assets.objects.filter(account_code = account.account_code)
		adherence, _ = calculate_adherence(account, assets)
		_, max_discrepancy_class = calculate_adherence(account, assets)

		results.append({
            'account_code': account.account_code,
            'account_suitability': account.account_suitability,
            'adherence': adherence,
			'max_discrepancy_class': max_discrepancy_class
        })

	results.sort(key=lambda x: x['adherence'])
	return render(request, 'index.html', {'results': results})

