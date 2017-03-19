# TeamGQL

-  pip install django
-  pip install virtualenv
-  cd to project directory
-  virtualenv virtualEnvironmentName ... I chose suorgenv for my name
-  source virtualEnvironmentName/bin/activate
-  virtualEnvironment is not active.
-  ./manage.py runserver will run the django test server
-  View in browser @ http://127.0.0.1:8000/

    Django is built using a series of Apps which is essentially a feature group of an entire site
    This code is sampled from book called Django Unleashed
    It currently lists a series of apps that have relevant models classified under Blog, Tag, and Startups
    You can take a look into each one of these app directories and go to the models file to view each model.
    
    Additionally, routing is nicely handled by django with the urls.py files in each respective app. There is a
    project wide urls.py which links to the nested urls.py. This is essentially where we need to add the graphql
    entrypoint.

