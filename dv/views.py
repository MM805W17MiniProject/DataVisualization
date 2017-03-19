from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from models import *
from fc import *

import operator

def _get_frequency_of_crime_(incident_name):
    qs = CrimeRecord.objects.filter(incident = incident_name)
    
    for place in Place.objects.filter(setted = False):
        qs = qs.exclude(place = place.place)
    for year in Year.objects.filter(setted = False):
        qs = qs.exclude(year = int(year.year))
    for month in Month.objects.filter(setted = False):
        qs = qs.exclude(month = int(month.month))
    
    cnt = 0
    for rec in qs:
        cnt += rec.times

    return cnt

def get_frequency_of_crime(incidents):
    res = []
    for incident in incidents:
        res.append(_get_frequency_of_crime_(incident.incident))
    return res

def set_flag(request):
    ex_places = Place.objects.all()
    ex_years = Year.objects.all()
    ex_months = Month.objects.all()
    
    for key in request.POST:
        if 'place' in key:
            ex_places = ex_places.exclude(place = request.POST[key])
            tmp = Place.objects.get(place = request.POST[key])
            tmp.setted = True
            tmp.save()
        
        if 'year' in key:
            ex_years = ex_years.exclude(year = request.POST[key])
            tmp = Year.objects.get(year = request.POST[key])
            tmp.setted = True
            tmp.save()
        
        if 'month' in key:
            ex_months = ex_months.exclude(month = request.POST[key])
            tmp = Month.objects.get(month = request.POST[key])
            tmp.setted = True
            tmp.save()
    
    for obj in ex_places:
        obj.setted = False
        obj.save()
    
    for obj in ex_years:
        obj.setted = False
        obj.save()
        
    for obj in ex_months:
        obj.setted = False
        obj.save()    

# Create your views here.
def index(request):
    if len(CrimeRecord.objects.all()) == 0:
        setup()
    
    if request.method == 'POST':
        set_flag(request)
    
    incidents = list(Incident.objects.all())
    places = list(sorted(Place.objects.all(),key=operator.attrgetter('place')))
    years = list(sorted(Year.objects.all(),key=operator.attrgetter('year')))
    months = list(Month.objects.all())
    
    context = {'incidents' : incidents, 
               'places' : places, 
               'years' : years, 
               'months' : months, 
               'res' : get_frequency_of_crime(incidents)}
    
    return render(request, 'dv/index.html', context)