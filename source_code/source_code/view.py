from django.http import HttpResponse
from .models import BloodDonatingUsers
import csv
from django.core import serializers
import json

def test_method(request):
    # print(request.__dict__)
    if request.method == 'GET':
        bloodGroup = request.GET.get('blood_group')
        donating_users_list = BloodDonatingUsers.objects.filter(blood_group=bloodGroup, label=1)
        print(len(donating_users_list))


        du_json = serializers.serialize('json', donating_users_list)
        print(du_json)
        du_geoJson = createGeoJson(du_json)
        print(du_geoJson)
        return HttpResponse(json.dumps(du_geoJson), content_type='application/json')
    return HttpResponse("Text only, please.", content_type="text/plain")

def createGeoJson(records):
    dict = {"features":[],"metadata":[]}
    records_json = json.loads(records)
    for row in records_json:
        prop = {
            "Name":row['fields']['name'],
            "BloodGroup": row['fields']['blood_group'],
            "Phone": row['fields']['phone']
        }

        geometry = {
            "type":"Point",
            "coordinates":[row['fields']['longitude'], row['fields']['latitude']]
        }

        rec_dicts = {"properties":prop,"geometry":geometry}

        dict["features"].append(rec_dicts)
    return dict

def load_data_from_csv():
    with open("source_code/table_data.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            _, created = BloodDonatingUsers.objects.get_or_create(
                name=row[0],
                phone=row[1],
                latitude=row[2],
                longitude=row[3],
                blood_group=row[4],
                label=row[5],
            )