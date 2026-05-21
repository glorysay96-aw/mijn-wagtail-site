from django.http import HttpResponse
from django.contrib.auth import get_user_model

def test_users(request):
    User = get_user_model()
    return HttpResponse(str(list(User.objects.all())))