from django.http import HttpResponse
from .models import BloodDonatingUsers
import csv
import pickle
from django.core import serializers

def test_method(request):
    # print(request.__dict__)
    if request.method == 'GET':
        bloodGroup = request.GET.get('blood_group')
        donating_users_list = BloodDonatingUsers.objects.filter(blood_group=bloodGroup, label=1)
        print(len(donating_users_list))
        du_json = serializers.serialize('json', donating_users_list)
        return HttpResponse(du_json, content_type='application/json')
    return HttpResponse("Text only, please.", content_type="text/plain")


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