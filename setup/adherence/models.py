from django.db import models

class Accounts(models.Model):
    account_code = models.CharField(max_length = 6, null = False, blank = False, primary_key = True)
    account_suitability = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return f'Accounts [code={self.account_code}]'

    class Meta:
        managed = False
        db_table = 'accounts'

class Assets(models.Model):
    id = models.AutoField(primary_key = True)
    account_code = models.CharField(max_length = 6, null = False, blank = False)
    asset_name = models.TextField()
    asset_cnpj = models.CharField(max_length = 16)
    class_name = models.CharField(max_length = 50)
    position_value = models.FloatField()

    def __str__(self) -> str:
        return f'Asset [id={self.id}]'

    class Meta:
        managed = False
        db_table = 'assets'

class Clients(models.Model):
    account_code = models.CharField(max_length = 6, null = False, blank = False, primary_key = True)
    account_suitability = models.CharField(max_length = 30)
    asset_name = models.TextField()
    asset_cnpj = models.CharField(max_length = 16)
    class_name = models.CharField(max_length = 50)
    position_value = models.FloatField()

    def __str__(self) -> str:
        return f'Clients [code={self.account_code}]'

    class Meta:
        managed = False
        db_table = 'clients'

