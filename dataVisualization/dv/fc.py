from models import *
from dataVisualization.settings import PROJECT_ROOT
import os

def setup():
    CrimeRecord.objects.all().delete()
    
    incidents = []
    
    FLAG_FIRST_LINE = True
    cnt = 0
    with open(os.path.join(PROJECT_ROOT, 'crime.txt')) as f:
        for line in f:
            if FLAG_FIRST_LINE:
                FLAG_FIRST_LINE = False
            else:
                splitted = line.split(',')
                splitted[-1] = splitted[-1].strip()
                if splitted[1] not in incidents:
                    incidents.append(splitted[1])
                CrimeRecord.objects.create(place = splitted[0], incident = splitted[1], year = int(splitted[2]) ,quarter = splitted[3],
                                           month = int(splitted[4]),times = int(splitted[5]))
                cnt += 1
                if cnt == 500:
                    break
    return incidents