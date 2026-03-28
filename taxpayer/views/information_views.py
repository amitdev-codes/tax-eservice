import logging

from django.contrib.messages.storage import session
from django.db import connection
from django.db.models import Q
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from taxpayer.models.information_models import TaxPayerIndividual

logger = logging.getLogger(__name__)


def get_field_value(obj, field_name):
    try:
        field_value = getattr(obj, field_name)
        return getattr(field_value, 'name_np', "Unknown")
    except AttributeError:
        print(f"An error occurred: {obj} has no {field_name}")
        return "Unknown"


def get_field_value_en(obj, field_name):
    try:
        field_value = getattr(obj, field_name)
        return getattr(field_value, 'name_en', "")
    except AttributeError:
        print(f"An error occurred: {obj} has no {field_name}")
        return ""


def personal(request):
    language = request.session.get('language')
    try:
        personal_data = TaxPayerIndividual.objects.prefetch_related('gender', 'country', 'occupation', 'nationality'
                                                                    ).filter(tax_payer_id=105535)

        data = []
        for p in personal_data:
            full_name = f"{p.first_name_np if language == 'ne' else p.first_name_en or ''} {p.middle_name_np or '' if language == 'ne' else p.middle_name_en or ''} {p.last_name_np if language == 'ne' else p.last_name_en or ''}".strip()
            dob = f"{p.dob_bs or '' if language == 'ne' else p.dob_ad or ''}"
            occupation_name = f"{get_field_value(p, 'occupation') if language == 'ne' else get_field_value(p, 'occupation') or ''}"
            gender_name = f"{get_field_value(p, 'gender') if language == 'ne' else get_field_value(p, 'gender') or ''}"
            country_name = f"{get_field_value(p, 'country') if language == 'ne' else get_field_value(p, 'country') or ''}"
            nationality_name = f"{get_field_value(p, 'nationality') if language == 'ne' else get_field_value(p, 'nationality') or ''}"

            record = {
                'id': p.id,
                'tax_payer_id': p.tax_payer_id,
                'full_name': full_name,
                'gender': gender_name,
                'dob': dob,
                'country': country_name,
                'occupation': occupation_name,
                'nationality_name': nationality_name,
                # Add other related data as needed
            }
            data.append(record)
        response_data = data
        context = {'response_data': response_data}
        return render(request, 'taxpayer/templates/information/personal.html', context)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return HttpResponseServerError("An error occurred while processing your request.")
