#!/bin/bash
echo Building ------------------------------
git remote add api https://git.heroku.com/mm802miniproject.git
heroku buildpacks:set heroku/python --remote api
git commit --allow-empty -m "Deploying project"
git push --force api master
heroku run python manage.py migrate --remote api
