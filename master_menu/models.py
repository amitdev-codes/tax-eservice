from django.db import models


class AppClientSettingModel(models.Model):
    client_id = models.SmallIntegerField(null=False)
    client_address = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    muntax_url = models.CharField(max_length=255)
    munacc_url = models.CharField(max_length=255)
    current_fiscal_year_code = models.CharField(max_length=255)
    current_fiscal_year_id = models.SmallIntegerField()
    receipt_type = models.CharField(max_length=255)
    receipt_value = models.CharField(max_length=255)
    current_year_rate_id = models.CharField(max_length=255)
    previous_year_rate_id = models.CharField(max_length=255)
    current_year_rate_value = models.CharField(max_length=255)
    previous_year_rate_value = models.CharField(max_length=255)
    land_measuring_id = models.SmallIntegerField()
    land_measuring_unit = models.SmallIntegerField()
    land_measuring_unit_name = models.CharField(max_length=255)
    length_id = models.SmallIntegerField()
    length_unit = models.SmallIntegerField()
    length_unit_name = models.CharField(max_length=255)
    last_fiscal_year = models.CharField(max_length=255)
    client_username = models.CharField(max_length=255)
    tax_amount_from = models.CharField(max_length=255)
    tax_amount_to = models.CharField(max_length=255)
    is_house_land_tax_implemented = models.BooleanField(default=False)
    is_ward_wise_psp_mode = models.BooleanField(default=False)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'app_client_settings'


class AccReceiptFlagModel(models.Model):
    client_id = models.SmallIntegerField(null=False)
    tax_type_id = models.SmallIntegerField()
    receipt_flag = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'acc_receipt_flags'


class TaxTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    code = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'vw_tax_type_master'


class MstUserType(models.Model):
    client_id = models.SmallIntegerField(null=False)
    code = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mst_user_types'


class MstTaxTypeOnlinePayment(models.Model):
    client_id = models.SmallIntegerField(null=False)
    tax_type_id = models.SmallIntegerField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mst_tax_type_online_payment'


class MstThirdParty(models.Model):
    client_id = models.SmallIntegerField(null=False)
    code = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mst_third_party'


class MstPaymentWallet(models.Model):
    client_id = models.SmallIntegerField(null=False)
    code = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    is_web_payment = models.BooleanField(default=False)
    is_token_payment = models.BooleanField(default=False)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mst_payment_wallets'


class AppSettingMaster(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    code = models.CharField(max_length=255)
    default_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_app_setting_master'


class VwAppClientwiseSetting(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    setting_id = models.IntegerField()
    client_id = models.IntegerField()
    default_value = models.CharField()
    combo_value = models.CharField()

    class Meta:
        managed = False
        db_table = 'vw_app_clientwise_setting'


class VwMstCountry(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    name_np = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_mst_country'


class VwAppClient(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    name_np = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_app_client'


class VwMstFederalHierarchy(models.Model):
    id = models.IntegerField(primary_key=True)
    name_np = models.CharField(max_length=255)
    parent_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vw_mst_federal_hierarchy'
