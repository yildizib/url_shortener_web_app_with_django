from django.http import HttpResponse


# Create your views here.

def index(self):
    return HttpResponse("You're looking at  %s." % ' INDEX Page')


def home_index(self):
    return HttpResponse("You're looking at  %s." % ' HOME INDEX Page')
