from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_admin(request):
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin12345"
        )
        return HttpResponse("admin created")

    return HttpResponse("already exists")
def test_users(request):
    User = get_user_model()
    return HttpResponse(str(list(User.objects.all())))
