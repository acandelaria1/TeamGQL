# TeamGQL

-  pip install django
-  pip install virtualenv
-  cd to project directory
-  virtualenv virtualEnvironmentName ... I chose suorgenv for my name
-  source virtualEnvironmentName/bin/activate
-  virtualEnvironment is not active.
-  ./manage.py runserver will run the django test server
-  View in browser @ http://127.0.0.1:8000/

    There are many graphql libraries for python but this project will use a python graphene integration
    viewable here at https://github.com/graphql-python/graphene-django/

    Django is built using a series of Apps which is essentially a feature group of an entire site
    This code is sampled from book called Django Unleashed
    It currently lists a series of apps that have relevant models classified under Blog, Tag, and Startups
    You can take a look into each one of these app directories and go to the models file to view each model.
    
    Additionally, routing is nicely handled by django with the urls.py files in each respective app. There is a
    project wide urls.py which links to the nested urls.py. This is essentially where we need to add the graphql
    entrypoint.

    UPDATE: Have currently created schemas for graphql integration. To achieve graphql integration for multiple models within
    several apps, you can implement several app level schema files that implement a Query class that inherits from the graphene
    AbstractObjectType. To combine all of these graphene schemas into a project wide schema you can implement a query that inherits
    from all of the app level schemas as is done in the suorganzizer/schema file. This is very similar to how the url configuration tree
    is constructed with several different app levels included into the project level urls file. Instead of listing several regular expressions
    in the urls you specify a query type for each model and this handles all possible data request permutations. The effort invested in defining
    graphene Query types is realized when you no longer have growing lists of urls for various permutation of data and the response data does not
    become bloated either.

