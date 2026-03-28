from django.db import models


class TaxLand(models.Model):
    id = models.IntegerField(primary_key=True)
    old_ward_no = models.CharField(max_length=100)
    ward_no = models.CharField(max_length=100)
    kitta_number = models.CharField(max_length=100)
    land_measuring_unit_id = models.IntegerField()
    area_sqft = models.FloatField()
    include_in_evaluation = models.BooleanField(default=True)
    old_vdc_id = models.IntegerField()  # Assuming this is a ForeignKey to the location hierarchy model
    is_deleted = models.BooleanField(default=False)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vw_tax_land'


class TaxLandOwnersLink(models.Model):
    id = models.IntegerField(primary_key=True)
    # land = models.ForeignKey(TaxLand, on_delete=models.CASCADE, related_name='owners')
    tax_payer_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    is_current_owner = models.BooleanField(default=True)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vw_tax_land_owners_link'


class TaxPayer(models.Model):
    id = models.IntegerField(primary_key=True)

    # Define fields for TaxPayerMaster model as needed
    class Meta:
        managed = False
        db_table = 'vw_tax_payer_master'


class CollReceiptMaster(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    land_id = models.IntegerField()
    fiscal_year_id = models.CharField()
    calc_id = models.IntegerField()
    area_sqft = models.IntegerField()

    # cm__receipt__is_receipt_cancelled = models.ForeignKey

    class Meta:
        managed = False
        db_table = 'vw_coll_receipt_master'


class CalcLandEval(models.Model):
    id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    fiscal_year_id = models.CharField()
    calc_id = models.IntegerField()
    area_sqft = models.IntegerField()
    applied_eval_value = models.FloatField()
    land = models.ForeignKey(TaxLand, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vw_tax_land'
