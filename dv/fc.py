## basic functionality of the website: interacting with the crime data in our example
## returns information of the crime in terms of incident type, location, year and month

from models import *
from dataVisualization.settings import PROJECT_ROOT
import os

def setup():
    
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
                
                if len(Incident.objects.filter(incident = splitted[1])) == 0:
                    Incident.objects.create(incident = splitted[1])
                
                if len(Place.objects.filter(place = splitted[0])) == 0:
                    Place.objects.create(place = splitted[0])
                    
                if len(Year.objects.filter(year = splitted[2])) == 0:
                    Year.objects.create(year = splitted[2])
                
                if len(Month.objects.filter(month = splitted[4])) == 0:
                    Month.objects.create(month = splitted[4])             
                
                CrimeRecord.objects.create(place = splitted[0], incident = splitted[1], year = int(splitted[2]) ,quarter = splitted[3],
                                           month = int(splitted[4]),times = int(splitted[5]))
                
                cnt += 1
		if cnt == 1500:
		    break
