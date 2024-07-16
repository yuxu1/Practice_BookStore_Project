from django.shortcuts import render
#to protect function-based views
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "sales/home.html")


# define function-based view - records(request)
#keep protected
@login_required
def records(request):
    # do nothing, simply display page
    return render(request, "sales/records.html")
