from django.db import models


# Create your models here.

class VwAppClientModel(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    name_en = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vw_app_client'


class PaymentWardModel(models.Model):
    id = models.IntegerField(primary_key=True)  # Assuming 'id' is the primary key
    payment_ward = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'payment_wards'


class EsewaWebCredential(models.Model):
    client_id = models.SmallIntegerField(max_length=128)
    esewa_payment_ward = models.SmallIntegerField(max_length=128)
    esewa_login_url = models.CharField(max_length=255)
    esewa_web_verification_url = models.CharField(max_length=255)
    esewa_success_url = models.CharField(max_length=255)
    esewa_failure_url = models.CharField(max_length=255)
    esewa_merchant_code = models.CharField(max_length=255)
    esewa_merchant_key = models.CharField(max_length=255)
    esewa_merchant_secret = models.CharField(max_length=255)
    esewa_transaction_details_url = models.CharField(max_length=255)
    esewa_callback_url = models.CharField(max_length=255)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'esewa_web_credentials'

    def is_valid(self):
        pass


class FonepayWebCredential(models.Model):
    client_id = models.SmallIntegerField(max_length=128)
    fonepay_payment_ward = models.SmallIntegerField(max_length=128)
    fonepay_login_url = models.CharField(max_length=255)
    fonepay_web_verification_url = models.CharField(max_length=255)
    fonepayQrGenerationUrl = models.CharField(max_length=255)
    fonepay_merchant_code = models.CharField(max_length=255)
    fonepay_merchant_key = models.CharField(max_length=255)
    fonepay_merchant_secret = models.CharField(max_length=255)
    fonepay_username = models.CharField(max_length=255)
    fonepay_password = models.CharField(max_length=255)
    fonepay_success_url = models.CharField(max_length=255)
    fonepay_failure_url = models.CharField(max_length=255)
    fonepay_transaction_details_url = models.CharField(max_length=255)
    fonepay_callback_url = models.CharField(max_length=255)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fonepay_web_credentials'

    def is_valid(self):
        pass


class KhaltiWebCredential(models.Model):
    client_id = models.SmallIntegerField()
    app_id = models.SmallIntegerField()
    app_name = models.CharField(max_length=255)
    khalti_payment_ward = models.SmallIntegerField()
    khalti_login_url = models.CharField(max_length=255)
    khalti_web_verification_url = models.CharField(max_length=255)
    khalti_success_url = models.CharField(max_length=255)
    khalti_failure_url = models.CharField(max_length=255)
    khalti_transaction_details_url = models.CharField(max_length=255)
    khalti_callback_url = models.CharField(max_length=255)
    khalti_secret_key = models.CharField(max_length=255)
    khalti_public_key = models.CharField(max_length=255)
    khalti_product_url = models.CharField(max_length=255)
    khalti_callback_success_url = models.CharField(max_length=255)
    khalti_callback_error_url = models.CharField(max_length=255)
    khalti_token_generation_url = models.CharField(max_length=255)
    khalti_return_url = models.CharField(max_length=255)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'khalti_web_credentials'


class IpsWebCredential(models.Model):
    client_id = models.SmallIntegerField()
    app_id = models.SmallIntegerField()
    app_name = models.CharField(max_length=255)
    ips_payment_ward = models.SmallIntegerField()
    ips_login_url = models.CharField(max_length=255)
    ips_web_verification_url = models.CharField(max_length=255)
    ips_transactions_details_url = models.CharField(max_length=255)
    ips_success_url = models.CharField(max_length=255)
    ips_failure_url = models.CharField(max_length=255)
    ips_merchant_id = models.CharField(max_length=255)
    ips_username = models.CharField(max_length=255)
    ips_password = models.CharField(max_length=255)
    pfx_file_name = models.CharField(max_length=255)
    cert_password = models.CharField(max_length=255)
    ips_callback_success_url = models.CharField(max_length=255)
    ips_callback_error_url = models.CharField(max_length=255)
    is_ebps = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ips_web_credentials'
