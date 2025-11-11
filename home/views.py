from django.shortcuts import render
from .models import DailySpecial

def todays_specials(request):
    specials = DailySpecial.objects.for_today()
    return render(request, 'home/todays_specials.html', {'specials': specials})
