from django.db import models


# Create your models here.
class Religion(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_religion'


class Gender(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_gender'


class Occupation(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_occupation'


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_country'


class Nationality(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_nationality'


class MotherTongue(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_mother_tongue'


class TaxPayerIndividual(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    tax_payer_id = models.IntegerField()
    first_name_np = models.CharField(max_length=255)
    middle_name_np = models.CharField(max_length=255)
    last_name_np = models.CharField(max_length=255)
    first_name_en = models.CharField(max_length=255)
    middle_name_en = models.CharField(max_length=255)
    last_name_en = models.CharField(max_length=255)
    dob_bs = models.CharField(max_length=255)
    dob_ad = models.CharField(max_length=255)
    other_details = models.CharField(max_length=255)
    phones = models.CharField(max_length=255)
    mobiles = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mail_address = models.CharField(max_length=255)
    citizenship_number = models.CharField(max_length=255)
    citizenship_issued_date_bs = models.CharField(max_length=255)
    citizenship_issued_date_ad = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=255)
    passport_issued_date_bs = models.CharField(max_length=255)
    passport_issued_date_ad = models.CharField(max_length=255)
    voter_card_number = models.CharField(max_length=255)
    voter_card_issued_date_bs = models.CharField(max_length=255)
    voter_card_issued_date_ad = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    permanent_ward_no = models.CharField(max_length=255)
    permanent_house_no = models.CharField(max_length=255)
    permanent_street_name = models.CharField(max_length=255)
    new_permanent_ward_no = models.CharField(max_length=255)
    temp_ward_no = models.CharField(max_length=255)
    temp_house_no = models.CharField(max_length=255)
    temp_street_name = models.CharField(max_length=255)
    new_temp_ward_no = models.CharField(max_length=255)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, db_column='religion_id')
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, db_column='occupation_id')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, db_column='gender')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='country_id')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, db_column='nationality_id')
    mother_tongue = models.ForeignKey(MotherTongue, on_delete=models.CASCADE, db_column='mother_tongue_id')

    class Meta:
        managed = False
        db_table = 'vw_tax_payer_individual'
