# Ariana's Journal

## Temporary guidelines for myself:

In the journals, every day that you work on the project, you must make an entry in your journal after you've finished that day. At a minimum, you will need to include the following information:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

## June 9, 2022
* Today, I worked on:
    * finishing the poller.py in the Foodies MS that polls the Eatery (and related) models from the Eateries MS - All
    * writing the api_return_list_of_restaurants_given_category_and_location function view - Brandon and I
* In the Foodies MS poller, we decided to flatten the EateryLocation data into the EateryVO model.
* It was a nice realization that while api_return_list_of_restaurants_given_category_and_location is a function view that takes care of a GET request, it creates instances of YelpLocationSearchTerm, YelpCategorySearchTerm, and YelpResult models as a side effect!

## June 8, 2022
* Today, I worked on:
    * fine-tuning the yelp integration - Brandon and I
* Our api_get_yelp_category_and_location function is now able to take in a location and category input and it will be used in the front end to take in search input from the user.
* A struggle that we have been going back and forth on is the many to many relationship and how to pull from the eateries microservice to the foodies/owners microservices.
* We learned that the pattern of categories that the yelp api takes and now know how to normalize out inputs from the users and feed them into the yelp request parameter.

## June 7, 2022
* Today, I worked on:
    * finishing the views for the models in the eateries microservice - Brandon and I
* We changed the many to many holder of the relationship between Eatery and Tag to live on the Eatery model. Also a sweet AHA moment learning that we can chose what side to put it on and it doesn't matter -- They're have a many-to-many relationship!
* Huge aha moment was when Brandon and I thought about using the get_extra_data() function to output (as Json Response) the model with a many-to-many relationship because of the circular logic from the encoders because we needed to include the encoders into each other but couldn't because of inheritance laws, so we added in the extra data to one encoder.

## June 6, 2022
* Today, I worked on:
    * finishing the eateries microservice by creating views for specifically getting the eateries - All
* We talked about incorporating a loop somewhere to go through the list of objects (e.g. EateryCategory) from the models that have a many to many relationship to the Eatery model and record each as part of that eatery instance. But we were not sure on how exactly to do that or where to write it. We also struggled with adding the categories to a list in the views and found that the many to many manager had a method .add() that we were able to use for each iteration through the list we are getting from the request.
* I made additions to the json.py file in the common directory so that our model encoder would be able to return many to many relationships as a nested object.
* Tuesday morning this was the AHA ^

## Jun 4, 2022
* Today I worked on:
    * Implementing the POST method for the api_eateries view function - All
    * Updating the ModelEncoder to now be able to serialize ManyRelatedManager objects
    * Updating some models in the Eateries MS to have some more constraints

* When trying to serialize a model that has a ManyToMany relationship with another model, we kept getting a "TypeError: Object of type ManyRelatedManager is not JSON serializable" with the existing ModelEncoder.

* The above problem was solved by updating the ModelEncoder to also account for objects of type ManyRelatedManager.

## Jun 3, 2022
* Today I worked on:
    * Updating the models in the Owners microservice(MS) - with Brandon
    * Writing the models in the Eateries MS - with Brandon
    * Re-structuring our Bounded Contexts (moving models from Owners MS to Eateries MS)
    * Brainstorming and writing the models in the Users MS - with Brandon
    * Brainstorming how we should populate our Eateries database from the YELP API - with Brandon and David
    * Sending requests to the Yelp API and successfully getting a response back - All

* When 2 models have a ManyToMany relationship, Brandon and I hard time deciding which should be the model that contains the other as an attribute.

* Brandon, David and I had an ah-ha! moment when Curtis explained to us how we can go about populating our Eateries database from the YELP API -- don't need to grab the entire Yelp database and store it in our database -- we're not YELP!

## Jun 2, 2022
* Today I worked on the models in the Owners microservice.

* Brandon and I pair-programmed as we wrote the models for the Owners microservice, setting up the admin, and testing the models in the Django admin.

* When we were done and wanted to push the changes to the remote repository, we ran into a gitignore issue with .pyc files. Because we had the .gitignore file always given to us ready to use, we forgot to keep it in mind, so all the .pyc files were included in the git add and git commit commands. (To be continued on next bullet).

* We eventually learned that the .gitignore file should be at the root directory and should contain the directories and files for git to ignore. I learned that it doesn't matter if the .gitignore file contains a lot of files and directories that don't even exist in the project. It also doesn't matter if the same directory/file is written more than once. The worry should be a directory/file NOT having been explicitly specified in the .gitignore file, which results in unwanted directories/files being pushed to the remote repository. But "extra" stuff being specified in the .gitignore file is NOT a concern.

## Jun 1, 2022
* Today I worked on putting together the docker-compose.yaml file.

* Brandon, Cameron, David and I worked as a group to put together the docker-compose.yaml file and getting all the containers to be up and running.

* We struggled with getting the database container to run while we were trying to set up the RDBMS and databases with PostgreSQL and the create-multiple-databases.sh file.

* The above issue was caused by the create-multiple-databases.sh file not being set as executable (which is an attribute of the filesystem). This can be seen when running the <ls -al db> command on the terminal at the top-level directory restaurant-repo (where db is the directory at restaurant-repo/db). Then it would show that create-multiple-databases.sh is not an executable file by NOT showing an "x" ("r" stands for "read", "w" stands for "write"). So we need to run the command <chmod a+x db/create-multiple-databases.sh> so that it changes the create-multiple-databases.sh to executable.
Another thing: the executable thing is an attribute of the FILE SYSTEM, not the file itself. that's why it can't be explicitly seen on a file that gets pushed to GitLab. However, because git DOES pay attention to that, if someone else were to clone down the repository, then the create-multiple-databases.sh would maintain it's "executable" state.


## May 31, 2022
* Today, I worked on updating the data-model.md, identifying the bounded contexts and microservices of the project at a high level

* Brandon, Cameron, David and I worked as a group to identify the bounded contexts before jumping into writing implementation code.

* I struggled to identify the relationship between Skewered_restaurant and Restaurant_VO models, as there was some confusion.

* We finally got confirmation from Chris that the relationship should indeed be many-to-one (from Skewered_restaurant to Restaurant_VO)

## May 30, 2022
* Today, I worked on updating the data-models.md and apis.md

* I cleaned up some of the models based on our group discussion from last week. Also updated apis.md to include more details as well as thinking a little more critically on whether a certain path is an API endpoint vs. GHI endpoint.

* I realized I have a hard time differentiating API endpoint vs GHI endpoint for the login/sign up pages mainly because the implementation of login/signup isn't too clear to me. The distinction between API endpoint and GHI endpoint for NON-login/signup pages is pretty clear to me at this point.

* Cleaning up some models to be one-to-many (while removing redundancy with nullable fields in other models) was enlightening! Also, being able to identify the need/use case for one-to-many relationships, many-to-many relationships is becoming easier and clearer.


## May 27, 2022

* Today, I worked on updating the apis.md

* Brandon, Cameron, David and I all worked as a group to first, identify which API endpoints our app would need, and second, update the api.md file to include details of input/output for each API endpoint.

* I had a hard time clearly identifying what will be an API endpoint, and what will be a web/user endpoint, as some API endpoints could be required for its own web/user endpoint (e.g. login web endpoint requires an API endpoint that handles a POST request to create a foodie/owner instance?), and some API endpoints can be used for many web/user endpoints (e.g. the web endpoint that shows the list of restaurants per location, and the web endpoint that shows the list of Skewered restaurants would both use the API endpoint that handles the GET request to get a list of restaurants -- while the frontend handles how to filter that list of restaurants once returned by the API endpoint).

* Thinking about and working through the API endpoints while imagining the GHI was very helpful in visualizing what the process of building the app would look like.