from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from models import *
from fc import *

import copy

# Create your views here.
def index(request):
    
    def _get_frequency_of_crime_(incident_name):
        cnt = 0
        for rec in CrimeRecord.objects.filter(incident = incident_name):
            cnt += rec.times
        return cnt
    
    def _get_frequency_of_crime_with_settings_(incident_name, request, places, years, months):
        cnt = 0
        query_set = CrimeRecord.objects.filter(incident = incident_name)
        
        for key in request.POST:
            if 'place' in key:
                places.remove(request.POST[key])
            if 'year' in key:
                years.remove(request.POST[key])
            if 'month' in key:
                months.remove(request.POST[key])
        
        for ex_place in places:
            query_set = query_set.exclude(place = ex_place)
        for ex_year in years:
            query_set = query_set.exclude(year = ex_year)
        for ex_month in months:
            query_set = query_set.exclude(month = ex_month)        
        
        for rec in query_set:
            cnt += rec.times
        return cnt    
    
    def get_frequency_of_crime(incidents, request ,POST_FLAG, places, years, months):
        res = []
        for incident_name in incidents:
            if not POST_FLAG:
                res.append(_get_frequency_of_crime_(incident_name))
            else:
                res.append(_get_frequency_of_crime_with_settings_(incident_name, request, copy.copy(places), copy.copy(years), copy.copy(months)))
        return res
                   
    
    data_lists = setup()
    
    incidents = data_lists[0]
    places = data_lists[1]
    years = data_lists[2]
    months = data_lists[3]
    
    places.sort()
    years.sort()
    months.sort()
    
    POST_FLAG = False
    if request.method == 'POST':
        POST_FLAG = True
        
    
    res = get_frequency_of_crime(incidents, request, POST_FLAG, places, years, months)
    
    context = {'incidents' : incidents, 
               'places' : places, 
               'years' : years, 
               'months' : months, 
               'res' : res}
    
    return render(request, 'dv/index.html', context)