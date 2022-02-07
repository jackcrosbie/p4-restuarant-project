from django.shortcuts import render

# Create your views here.
def index(request):
    """ Return homepage """
    return render(request, 'index.html')


def user_account(request):
    """ return member homepage """
    return render(request, 'user_account.html')