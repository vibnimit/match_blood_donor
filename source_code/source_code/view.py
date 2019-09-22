from django.http import HttpResponse


def test_method(request):
    print(request.__dict__)

    return HttpResponse("Text only, please.", content_type="text/plain")