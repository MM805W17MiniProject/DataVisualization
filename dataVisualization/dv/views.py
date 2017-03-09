from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from models import *
from fc import *

# Create your views here.
def index(request):
    
    def _get_frequency_of_crime_(incident_name):
        cnt = 0
        for rec in CrimeRecord.objects.filter(incident = incident_name):
            cnt += rec.times
        return cnt
    
    def get_frequency_of_crime(incidents):
        res = []
        for incident_name in incidents:
            res.append(_get_frequency_of_crime_(incident_name))
        return res
    
    incidents = setup()
    context = {'incidents' : incidents, 'res' : get_frequency_of_crime(incidents)}
    return render(request, 'dv/index.html', context)