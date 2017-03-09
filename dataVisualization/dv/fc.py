## basic functionality of the website: interacting with the crime data in our example
## returns information of the crime in terms of incident type, location, year and month

from models import *
from dataVisualization.settings import PROJECT_ROOT
import os

def setup():
    CrimeRecord.objects.all().delete()
    incidents = []
    
    places = []
    years = []
    months = []
    
    FLAG_FIRST_LINE = True
    cnt = 0
    # load data from text file
    with open(os.path.join(PROJECT_ROOT, 'crime.txt')) as f:
        for line in f:
            if FLAG_FIRST_LINE:
                FLAG_FIRST_LINE = False
            else:
                splitted = line.split(',')
                splitted[-1] = splitted[-1].strip()
                
                if splitted[1] not in incidents:
                    incidents.append(splitted[1])
                
                if splitted[0] not in places:
                    places.append(splitted[0])                
                if splitted[2] not in years:
                    years.append(splitted[2])
                if splitted[4] not in months:
                    months.append(splitted[4])                
                
                CrimeRecord.objects.create(place = splitted[0], incident = splitted[1], year = int(splitted[2]) ,quarter = splitted[3],
                                           month = int(splitted[4]),times = int(splitted[5]))
                cnt += 1
                if cnt == 450:
                    break
    return [incidents, places, years, months]
