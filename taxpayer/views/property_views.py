from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render


def land(request):
    taxpayer_id =105535
    fiscal_year_id = 228
    client_id = 178

    query = """
        SELECT DISTINCT
            concat ( mlh.name_np, '-', C.old_ward_no ) AS land_address,
            C.ward_no AS ward_no,
            C.kitta_number,
            tab.applied_eval_value AS evaluation_amount,
            lnk.tax_payer_id,
            lnk.land_id,
            C.land_measuring_unit_id,
            C.area_sqft,
            lu.name_np AS land_measuring,
            CASE
                WHEN (
                    SELECT COUNT(*)
                    FROM vw_tax_house_lands_link
                    WHERE land_id = lnk.land_id AND is_deleted IS FALSE AND status IS TRUE
                ) >= 1 THEN TRUE ELSE FALSE
            END AS houseexist
        FROM
            vw_tax_land C
            INNER JOIN vw_tax_land_owners_link lnk ON C.ID = lnk.land_id AND lnk.is_deleted = C.is_deleted AND C.client_id = lnk.client_id
            INNER JOIN vw_tax_payer_master tpm ON tpm.ID = lnk.tax_payer_id AND tpm.client_id = C.client_id
            LEFT JOIN vw_taxpayer_join vwt ON vwt.ID = lnk.tax_payer_id AND vwt.ID = %s
            LEFT JOIN vw_tax_land_rates lr ON C.ID = lr.land_id AND C.is_deleted = lr.is_deleted AND lr.client_id = C.client_id
            LEFT JOIN vw_tax_land_eval_rate er ON lr.land_rate_id = er.ID AND er.client_id = lr.client_id
            LEFT JOIN vw_tax_land_eval_rate_group eg ON er.rate_group_id = eg.ID AND eg.client_id = er.client_id
            LEFT JOIN vw_calc_land_eval cler ON C.ID = cler.land_id AND cler.fiscal_year_id = %s AND cler.client_id = C.client_id
            LEFT JOIN vw_mst_length_unit lu ON C.land_measuring_unit_id = lu.ID
            LEFT JOIN vw_mst_location_hierarchy mlh ON C.old_vdc_id = mlh.ID
            LEFT JOIN (
                SELECT
                    ce.land_id,
                    ce.client_id,
                    ce.applied_eval_value,
                    RANK() OVER (PARTITION BY ce.land_id ORDER BY ce.calc_id DESC) AS rnk
                FROM
                    vw_calc_land_eval ce
                    INNER JOIN vw_tax_land_owners_link lol ON ce.land_id = lol.land_id AND ce.client_id = lol.client_id AND lol.is_deleted = FALSE
                    INNER JOIN vw_calc_master cm ON ce.calc_id = cm.ID
                    LEFT JOIN vw_coll_receipt_master rm ON rm.ID = cm.receipt_id
                WHERE
                    ce.fiscal_year_id = %s AND lol.tax_payer_id = %s
                    AND ce.client_id = %s AND COALESCE(rm.is_receipt_cancelled, FALSE) = FALSE
            ) tab ON C.ID = tab.land_id AND C.client_id = tab.client_id AND tab.rnk = 1
        WHERE
            COALESCE(C.is_deleted, FALSE) = FALSE AND C.client_id = %s
            AND C.include_in_evaluation = 't' AND lnk.tax_payer_id = %s
            AND lnk.is_deleted = FALSE AND lnk.is_current_owner = TRUE AND tpm.is_deleted = 'f'
    """

    with connection.cursor() as cursor:
        cursor.execute(query,
                       [taxpayer_id, fiscal_year_id, fiscal_year_id, taxpayer_id, client_id, client_id, taxpayer_id])
        land_details = cursor.fetchall()

    land_details_data = []
    for item in land_details:
        land_details_data.append({
            'land_address': item[0],
            'ward_no': item[1],
            'kitta_number': item[2],
            'evaluation_amount': item[3],
            'tax_payer_id': item[4],
            'land_id': item[5],
            'land_measuring_unit_id': item[6],
            'area_sqft': item[7],
            'land_measuring': item[8],
            'house_exist': item[9]
        })
    context = {'land_details': land_details_data}
    return render(request, 'taxpayer/templates/property/land_details.html', context)


def house_details(request):

    taxpayer_id = 105535
    fiscal_year_id = 228
    client_id = 178
    land_id = request.GET.get('land_id')

    query = """SELECT
                distinct
                th.ID,
                thll.house_id,
                tl.kitta_number,
                COALESCE(mht.name_np,\'-\')AS house_type,
                COALESCE(th.code,\'-\')AS code,
                COALESCE(th.house_no,\'-\')AS house_no,
                COALESCE(mhct.name_np,\'-\') AS construction_name_np,
                -- COALESCE(th.total_floors,\'-\') AS floor_no,
                th.total_floors AS floor_no,
                th.length_in_feet AS length_in_feet,
                th.width_in_feet AS width_in_feet,
                th.height_in_feet AS height_in_feet,
                COALESCE(mfy.code,\'-\') AS construction_fiscal_year,
                th.area_in_sqft AS area_in_sqft,
                th.plinth_area as plinth_area_sqft,
                COALESCE(th.acquisition_date_bs,\'-\') AS acquisition_date_bs,
                th.has_construction_complete_certificate,
                tlo.land_id
            FROM
            vw_tax_house th
        	INNER JOIN vw_tax_house_lands_link thll ON th.ID = thll.house_id AND thll.is_deleted =FALSE
        	LEFT JOIN vw_tax_land tl ON tl.ID = thll.land_id AND tl.is_deleted =FALSE
            LEFT JOIN vw_tax_land_owners_link tlo ON tlo.land_id = tl.ID AND tlo.is_deleted =FALSE
            LEFT JOIN vw_mst_house_type AS mht ON th.house_type_id = mht.ID
            LEFT JOIN vw_mst_house_construct_type AS mhct ON th.house_construction_type_id = mhct.ID
            LEFT JOIN vw_calc_house_eval AS che ON th.ID = che.house_id and che.fiscal_year_id=%s
            LEFT JOIN vw_mst_fiscal_year AS mfy ON che.fiscal_year_id = mfy.ID
        WHERE
        	(
        	COALESCE ( th.is_deleted, FALSE )) =false
        	AND ( th.client_id ) =%s
        	AND th.include_in_evaluation =true
        	AND thll.land_id =%s
        	AND tlo.tax_payer_id =%s
        ORDER BY
        thll.house_id """
    with connection.cursor() as cursor:
        cursor.execute(query,
                       [fiscal_year_id, client_id, land_id, taxpayer_id])
        house_data = cursor.fetchall()

        house_details_data = []
        for item in house_data:
            house_details_data.append({
                'id': item[0],
                'house_id': item[1],
                'kitta_number': item[2],
                'house_type': item[3],
                'code': item[4],
                'house_no': item[5],
                'construction_name_np': item[6],
                'floor_no': item[7],
                'length_in_feet': item[8],
                'width_in_feet': item[9],
                'height_in_feet': item[10],
                'construction_fiscal_year': item[11],
                'area_in_sqft': item[12],
                'plinth_area_sqft': item[13],
                'acquisition_date_bs': item[14],
                'has_construction_complete_certificate': item[15],
            })
    # context = {'house_details': house_details_data}
    return JsonResponse({'house_details': house_details_data})
    # return render(request, 'taxpayer/templates/property/land_details.html', context)


def house_floor_details(request):
    house_id = request.GET.get('house_id')
    kitta_number = request.GET.get('kitta_number')
    taxpayer_id = 105535
    fiscal_year_id = 228

    query = """SELECT distinct
        thf.ID,
        thf.code,
        COALESCE(th.house_no,\'-\')AS house_no,
        thf.floor_no,
        thf.construction_date_bs,
        tcer.name_np,
        thf.area_in_sqft,
        tcer.rate_per_unit,
        COALESCE(cfe.calculated_value,\'0\') AS calculated_value,
        COALESCE(cfe.depreciation_rate,\'0\') AS depreciation_rate,
        COALESCE(cfe.depreciation_amount,\'0\') AS depreciation_amount,
        COALESCE(cfe.net_eval_value,\'0\') AS net_eval_value,
        thf.is_rented
    FROM
        vw_tax_land_owners_link AS tlo
        LEFT JOIN vw_tax_land AS tl ON tlo.land_id = tl.ID
        LEFT JOIN vw_tax_house_lands_link AS thll ON tl.ID = thll.land_id
        LEFT JOIN vw_tax_house AS th ON thll.house_id = th.ID
        LEFT JOIN vw_mst_house_use AS mhu ON th.uses_type_id = mhu.ID
        LEFT JOIN vw_mst_house_type AS mht ON th.house_type_id = mht.ID
        LEFT JOIN vw_mst_house_construct_type AS mhct ON th.house_construction_type_id = mhct.ID
        LEFT JOIN vw_tax_house_floors AS thf ON th.ID = thf.house_id
        LEFT JOIN vw_calc_floor_eval AS cfe ON thf.ID = cfe.floor_id and cfe.fiscal_year_id=%s
        LEFT JOIN vw_tax_construction_eval_rate AS tcer ON thf.construction_rate_id = tcer.ID
    WHERE
        thll.house_id =%s
        AND tl.kitta_number =%s
        AND tlo.tax_payer_id =%s
    ORDER BY
        floor_no ASC """
    with connection.cursor() as cursor:
        cursor.execute(query,
                       [fiscal_year_id, house_id, kitta_number, taxpayer_id])
        house_floor_data = cursor.fetchall()

        house_floor_details_data = []
        for item in house_floor_data:
            house_floor_details_data.append({
                'id': item[0],
                'code': item[1],
                'house_no': item[2],
                'floor_no': item[3],
                'construction_date_bs': item[4],
                'name_np': item[5],
                'area_in_sqft': item[6],
                'rate_per_unit': item[7],
                'calculated_value': item[8],
                'depreciation_rate': item[9],
                'depreciation_amount': item[10],
                'net_eval_value': item[11],
                'is_rented': item[12],
            })
    return JsonResponse({'house_floor_details': house_floor_details_data})
    # context = {'house_floor_details': house_floor_details_data}
    # return render(request, 'taxpayer/templates/property/land_details.html', context)
