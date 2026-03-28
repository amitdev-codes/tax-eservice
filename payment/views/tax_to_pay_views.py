from django.shortcuts import render
from django.db import connection
from master_menu.models import MstPaymentWallet


def tax_to_pay(request):
    client_id = 178
    taxpayer_id = 105535
    current_fiscal_year = 228

    query = """SELECT A.calc_id,A.tax_type_id,A.calc_date_bs,A.tax_type,A.fiscal_year,A.tax_amount,A.due_amount,A.tax_paid_amount,A.remaining_amount 
                FROM
                    (
                    SELECT C
                        .*,
                        ( CASE WHEN C.tax_type_id = 30 THEN 0 ELSE COALESCE ( pp.tax_paid_amount, 0 ) END ) AS tax_paid_amount,
		                COALESCE (
		                     CASE
				WHEN COALESCE ( C.due_amount, 0 ) > 0 THEN
				round( CAST ( C.due_amount AS NUMERIC ), 2 ) - round( CAST ( CASE WHEN C.tax_type_id = 30 THEN 0 ELSE pp.tax_paid_amount END AS NUMERIC ), 2 ) ELSE 0
			END,
			0
		) AS remaining_amount,
                        C.ID AS calc_id,
                        mfy.code AS fiscal_year,
                        total as tax_amount
                    FROM
                    public.vw_tax_due
                        C LEFT JOIN vw_mst_fiscal_year AS mfy ON C.fiscal_year_id = mfy.
                        ID LEFT JOIN (
                        SELECT
                            calc_id,
                            tax_type_id,
                            taxpayer_id,
                            valuation_date_bs,
                            SUM ( tax_amount ) total,
                        			SUM ( round( CAST ( total_paid_amount AS NUMERIC ), 2 ) ) AS tax_paid_amount,
			SUM ( round( CAST ( tax_amount AS NUMERIC ), 2 ) - round( CAST ( total_paid_amount AS NUMERIC ), 2 ) ) AS due_amount
                        FROM
                        public.vw_tax_summary C
                        WHERE
                            (
                            COALESCE ( C.is_deleted, FALSE )) = FALSE
                            AND C.client_id =%s
                            AND C.taxpayer_id =%s
                        GROUP BY
                            calc_id,
                            tax_type_id,
                            taxpayer_id,
                            valuation_date_bs
                        ) pp ON pp.calc_id = C.ID
                        AND pp.tax_type_id = C.tax_type_id
                        AND pp.taxpayer_id = C.taxpayer_id
                        AND pp.valuation_date_bs = C.calc_date_bs
                    WHERE
                        (
                        COALESCE ( C.is_deleted, FALSE )) = FALSE
                        AND ( C.client_id ) =%s
                        AND C.fiscal_year_id =%s
                        AND C.taxpayer_id =%s
                        AND C.tax_type_id in (1,2,5)
                        OFFSET 0
                    )
                    A LEFT JOIN vw_taxpayer_auto_eval_status taes ON taes.tax_payer_id = A.taxpayer_id
                    AND taes.is_verified IS TRUE"""
    with connection.cursor() as cursor:
        cursor.execute(query,
                       [client_id, taxpayer_id, client_id, current_fiscal_year, taxpayer_id])
        tax_payment = cursor.fetchall()

        print(tax_payment)

    tax_to_pay_data = []
    for item in tax_payment:
        tax_to_pay_data.append({
            'calc_id': item[0],
            'tax_type_id': item[1],
            'calc_date_bs': item[2],
            'tax_type': item[3],
            'fiscal_year': item[4],
            'tax_amount': item[5],
            'due_amount': item[6],
            'tax_paid_amount': item[7],
            'remaining_amount': item[8]
        })

    context = {'tax_to_pay_details': tax_to_pay_data}
    return render(request, 'payment/templates/tax_to_pay.html', context)


def initiate_payment(request):
    tax_type_id = request.GET.get('tax_type_id')
    amount = request.GET.get('amount')

    list_active_wallets = MstPaymentWallet.objects.filter(is_web_payment=True, client_id=178).values_list('code',
                                                                                                          flat=True).order_by(
        'name_en')
    data = {
        'full_name': 'test data',
        'amount': amount,
        'tax_type': tax_type_id
    }
    context = {'data': data, 'list_active_wallets': list_active_wallets}
    return render(request, 'payment/templates/payment_confirmation.html', context)


def redirect_psp(request):
    # do process and redirect to their page
    return render(request, 'payment/templates/payment_confirmation.html')
