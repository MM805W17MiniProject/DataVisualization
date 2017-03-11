<snippet>
  <content>
# MiniProject of MM802
 - Visualize crime data collected from Edmonton city open data project. Data used can be found:[here](https://www.edmonton.ca/residential_neighbourhoods/property_tax_assessment/property-assessment.aspx). We aimed to visualize criminal data in Edmonton in bar charts.
 - Further details will be put here.
 - Team members: Xuping Fang, Ke Gong, Comet Li.
 
## Installation
    TODO: Download the components and save to <Project_Root> and prepare required environments:

### virtualenv
    virtualenv creates a isolated Python environment, which can help avoid package issue.
  ```make
  # In command window
  $ sudo apt install virtualenv
  $ cd <Project_Root>
  # adapt the environment
  $ virtualenv venv
  $ source venv/bin/activate
  ```
    to leave the virtual environment:
  ```make
  $ deactivate
  ```
  
#### packages need to be installed within virtualenv:
#####Django
    Django is an open source, high-level Python web framework.
installation of Django can be found [here](https://docs.djangoproject.com/en/1.10/topics/install/)

#####Django Rest Framework
    install needed sub-package for django
  ```make
  $ pip install djangorestframework
  # optional packages may be helpful
  $ pip install markdown       # Markdown support for the browsable API.
  $ pip install django-filter  # Filtering support
  ```
     or
 ```make
 # In command window
 $ git clone git@github.com:tomchristie/django-rest-framework.git
 ```
#####requests (a HTTP library)
  ```make
  # install requests
  $ pip install requests
  ```
  

## Usage
  ```make
  #in venv
  $ cd <Project_Root>/dataVisualization
  $ python mange.py runserver
  ```
  
    Keep the command running and open[this page](http://127.0.0.1:8000/dv) in your browser.
    The usage of the webpage currently provide the crime record in Abbottsfield, Edmonton, 2009.<br />
User can select location(currently only Abbottsfield), year(currently only 2009) and months. The data will be shown in bar chart on top.

## Contributing
..

</content>
  <tabTrigger></tabTrigger>
</snippet>
