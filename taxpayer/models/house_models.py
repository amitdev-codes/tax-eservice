from django.db import models


class TaxHouse(models.Model):
    house_no = models.CharField(max_length=255)
    total_floors = models.IntegerField()
    length_in_feet = models.DecimalField(max_digits=10, decimal_places=2)
    width_in_feet = models.DecimalField(max_digits=10, decimal_places=2)
    height_in_feet = models.DecimalField(max_digits=10, decimal_places=2)
    area_in_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    construction_date_bs = models.CharField(max_length=255)
    acquisition_date_bs = models.CharField(max_length=255)
    has_construction_complete_certificate = models.BooleanField()
    client_id = models.IntegerField()
    include_in_evaluation = models.BooleanField()
    is_deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vw_tax_house'


class TaxHouseLandsLink(models.Model):
    house_id = models.IntegerField()
    land_id = models.IntegerField()
    is_deleted = models.BooleanField()
    tax_house = models.ForeignKey(TaxHouse, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vw_tax_house_lands_link'


class TaxLand(models.Model):
    kitta_number = models.CharField(max_length=255)
    remarks = models.TextField()
    status = models.CharField(max_length=255)
    is_deleted = models.BooleanField()
    tax_house_lands_link = models.ForeignKey('TaxHouseLandsLink', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vw_tax_land'


class TaxLandOwnersLink(models.Model):
    land_id = models.IntegerField()
    tax_payer_id = models.IntegerField()
    is_deleted = models.BooleanField()

    tax_land = models.ForeignKey(TaxLand, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'vw_tax_land_owners_link'


class HouseType(models.Model):
    name_np = models.CharField(max_length=255)


class HouseConstructType(models.Model):
    name_np = models.CharField(max_length=255)


class FiscalYear(models.Model):
    code = models.CharField(max_length=255)
