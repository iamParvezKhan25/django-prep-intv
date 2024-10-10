from django.http import HttpResponse, request
from .models import ApplicationUser

def view1(request):
    return HttpResponse("This is view 1.")


def view2(request):
    return HttpResponse("This is view 2.")


def view3(request):
    users = ApplicationUser.objects.all()
    return HttpResponse(users)
