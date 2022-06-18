# Ariana's Journal

## Temporary guidelines for myself:
1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

## June 17, 2022
* Today, I:
    * Changed EateryTagVO, EateryCategoryVO to have a ManyToMany relationship with EateryVO (instead of ForeignKey), and updated pollers and encoders accordingly
    * updated __str__ method for Eatery model to show all the categories associated to it
    * updated all the encoders in the Foodies MS to nest Eatery-Related-VO objects inside of EateryVO JSON response (as desired)
    * updated Tag model in Eateries MS to EateryTag to have consistent naming throughout the project + made necessary changes accordingly
*  Updated EateryCategoryVO and EateryTagVO models relationships to EateryVO model from ForeignKey to ManyToManyField, as well as poller updates accordingly
* ah-ha moment: nesting EateryTagVO, EateryCategoryVO, and all other Eatery-Related-VO objects inside the EateryVO JSONResponse was possible! Didn't realize this was possible and had previously written function views to access for example: All EateryCategoryVOs related to an EateryVO, All EateryTagVOs related to an EateryVO, All EateryOpenHoursVOs related to an EateryVO, etc.

## June 16, 2022
* Today, I worked on:
    * Modifying the view functions in the Foodies that raise a DoesNotExist exception from 400 status to 404
    * Writing the view function to GET a specific eateryvo instance in Foodies MS
    * Modified view function names in Foodies MS to be more reflective of their functionality
* When creating tags, the tag was created, but there was no association with it to an eatery. However, we discussed that foodie could create a tag, the front end will make sure to create the tag and associate the tag to the eatery that the foodie is adding the tag to.
* The design decision was that we didn't need to change/rewrite the view for TagVOs. And the Ah-ha moment was that it would be taken care of by making 2 API calls to the backend from the React front-end!


## June 15, 2022
* Today, I worked on:
    * finishing the api_return_list_of_restaurants_given_category_and_location function view. Needed to return the actual Eatery objects related to the YelpResult objects, instead of the YelpResult objects - Brandon and I
    * writing and updating some more views in the Foodies MS - David and I
    * writing view to get all reviews based on an eatery, and get a review based on SkeweredEatery - David and I
    * updating models and updating the BoundedContexts diagram based on the model changes
* David and I discussed path "conventions" in the api_urls.py in the Foodies MS given that there are so many views, plus we are starting to write even more for the "double" function views referenced below.
* David and I realized that a lot of the views in the Foodies MS need "double" function for the GET all function views: Get all instances of X model (in general) + Get all instances of X model related to Y model.

## June 14, 2022
* Today, I:
    * looked into and took care of some merge issues from the codes that David/Cameron and Brandon/I have been working on. (migrations files we had deleted and should have stayed deleted were accidentally added back to the remote main branch) - David and I
* David and I decided that the Review model will have a DELETE view function for the administrators to be able to remove reviews (in case a foodie leaves an inappropriate review). However, the foodie will not be able to delete a review -- they will only be able to update a review.
* David and I realized that the EateryImageVO, EateryCategoryVO and EateryTagVO will need views with GET requests, since the EateryVO's JSON response does not include the data of the 3 models (EateryImageVO, EateryCategoryVO and EateryTagVO) nested inside of it.

## June 12, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view. Actually thought we were done, but towards the end, we realized we weren't quite done yet! - Brandon and I
* Brandon and I refactored the api_return_list_of_restaurants_given_category_and_location function view. The overall logic (that Curtis helped us come up with is that): 1) If Yelp's API is up and running, then when a foodie makes a request for a list of eateries for a specific location and category, our app will send a request to the Yelp API for a list of eateries. 2) If the location given by the foodie isn't a valid location, then the foodie will get a message letting the foodie know that the location is invalid. 3) If Yelp's API is down, then a) if it's a category and location that has been searched for before, then our database will have some Eatery instances to return to the foodie, b) if it's a category and location that hasn't been searched for before, then our app will return a message to the foodie that something went wrong, and to try again later. Based on that logic, we updated our functions in the acls.py as well as updating our code in api_return_list_of_restaurants_given_category_and_location to be wrapped in try/except and if/else blocks.
* While thinking through the details of the logic above, we ran into a lot of questions and design decisions on every try/except block. One ah-ha moment we had is that while testing what the Yelp API returns with different inputs (as query parameters) we learned about the different JSON response objects that it returns when the API receives info that it doesn't know how to handle. So whereas it's raises and error on their end, we receive a nice error message describing the error message (just like we learned API points should :)) so based on those error messages, we were able to write and update our functions in acls.py

## June 11, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view - Brandon and I
* Brandon and I discussed and made some decisions on how to populate the EateryOpenHours model from the Yelp API (the Yelp API endpoint that returns the open hours for a specific restaurant is a separate one that requires the ID of a specific business). So we wrote the above view based on that, as well as making some updates to the Eatery model by adding some more attributes.
* While working on the integration of the open hours for a business from Yelp into our app, Brandon and I had to figure out how to handle store hours from the Yelp API that we get as a string (e.g. "0800" to create a Django TimeField in the EateryOpenHours model). We learned that feeding the EateryOpenHours model a string formatted as "08:00" was good enough for Django to create a TimeField from that!

## June 10, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view, creating EateryLocation object instances and EateryCategory object instances - Brandon and I
* After receiving the rubric from Curtis, the 4 of us decided what we should consider as part of the MVP for our app, and what becomes a part of the stretch goals.
* The 4 of us also discussed the need for 2 separate models (EateryImage and ReviewImage) vs getting away with just having 1 model (Image) for both the Eatery and Review models. After discussing, we realized we needed 2 separate models as the EateryImage will have a foreign key to the Eatery model, and the ReviewImage will have a foreign key to the Review model.

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