# Brandon's Journal

## Guidelines:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

## June 20, 2022
* Today I worked on implementing the poller from the User microservice to the Foodie and Owner microservices. I still need to finish the Owner poller but it will be almost identical to the function in the Foodie poller, and should not take long to implement.
* Ariana and I discussed about if we should have two separate poller files in each service for both pulling eateries and users, or if we should call two functions in the while loop of one poller file. We chose to put both in one file in the same while loop. We thought the other way would add un necessary complexity.
* an AHA moment I had today was getting the foodieVO to pull the user data. However a HAH moment because i couldn't get the OwnerVO to pull the user data

## June 18, 2022
* Today I worked on creating Cards in the homepage that houses our data, and introducing a header to the page. 
* I had to make some design choices when it came to how I was going to structure this page. Im using a function component so ill be using hooks to manage the state. I am still not sure how I want to do it, but currently I am using Styled Components and mapping each eatery into a CardBody. I now want to make columns on the page but im not sure how.
* an AHA moment I had today was I learned the benefits of Styled Components by getting the cards to house the data and adjust each field how I wanted.

## June 16, 2022
* Today I worked on researching grabbing user location from IP address. I created the HomePage and was able to receive the location object but currently working on using a different API because the response did not contain the location information I needed.
* Our team discussed how we wanted to handle the functionality of our HomePage. We decided that we were going to gather user location information on page load that would send an api request to return a location object so we can pre populate the home page with eateries in their area.
* an AHA moment I had today was DO NOT RUN npn audit ---force...something. Also that you can use IP addresses to get location. 

## June 15, 2022
* Today, I worked on:
    * finishing the api_return_list_of_restaurants_given_category_and_location function view. Needed to return the actual Eatery objects related to the YelpResult objects, instead of the YelpResult objects - Ariana and I
    * updating models and updating the BoundedContexts diagram based on the model changes
* Cameron and I discussed the teams workflow plan going forward. We talked about the projects bounded context, what truly the MVP was, and how we should delegate which task in the corresponding priority order
* AHA we underestimated the time line! ahhhh

## June 14, 2022
* Today, I worked on refactoring the monster view, I ended up just making comments and running tests.
* No design changes and discussion, just testing and making notes
* Aha testing is fun!

## June 12, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view. Actually thought we were done, but towards the end, we realized we weren't quite done yet! - Ariana and I
* Ariana and I refactored the api_return_list_of_restaurants_given_category_and_location function view. The overall logic (that Curtis helped us come up with is that): 1) If Yelp's API is up and running, then when a foodie makes a request for a list of eateries for a specific location and category, our app will send a request to the Yelp API for a list of eateries. 2) If the location given by the foodie isn't a valid location, then the foodie will get a message letting the foodie know that the location is invalid. 3) If Yelp's API is down, then a) if it's a category and location that has been searched for before, then our database will have some Eatery instances to return to the foodie, b) if it's a category and location that hasn't been searched for before, then our app will return a message to the foodie that something went wrong, and to try again later. Based on that logic, we updated our functions in the acls.py as well as updating our code in api_return_list_of_restaurants_given_category_and_location to be wrapped in try/except and if/else blocks.
* While thinking through the details of the logic above, we ran into a lot of questions and design decisions on every try/except block. One ah-ha moment we had is that while testing what the Yelp API returns with different inputs (as query parameters) we learned about the different JSON response objects that it returns when the API receives info that it doesn't know how to handle. So whereas it's raises and error on their end, we receive a nice error message describing the error message (just like we learned API points should :)) so based on those error messages, we were able to write and update our functions in acls.py

## June 11, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view - Ariana and I
* Ariana and I discussed and made some decisions on how to populate the EateryOpenHours model from the Yelp API (the Yelp API endpoint that returns the open hours for a specific restaurant is a separate one that requires the ID of a specific business). So we wrote the above view based on that, as well as making some updates to the Eatery model by adding some more attributes.
* While working on the integration of the open hours for a business from Yelp into our app, Ariana and I had to figure out how to handle store hours from the Yelp API that we get as a string (e.g. "0800" to create a Django TimeField in the EateryOpenHours model). We learned that feeding the EateryOpenHours model a string formatted as "08:00" was good enough for Django to create a TimeField from that!

## June 10, 2022
* Today, I worked on:
    * continuing writing the api_return_list_of_restaurants_given_category_and_location function view, creating EateryLocation object instances and EateryCategory object instances - Ariana and I
* After receiving the rubric from Curtis, the 4 of us decided what we should consider as part of the MVP for our app, and what becomes a part of the stretch goals.
* The 4 of us also discussed the need for 2 separate models (EateryImage and ReviewImage) vs getting away with just having 1 model (Image) for both the Eatery and Review models. After discussing, we realized we needed 2 separate models as the EateryImage will have a foreign key to the Eatery model, and the ReviewImage will have a foreign key to the Review model.

## June 9, 2022
* Today, I worked on:
    * finishing the poller.py in the Foodies MS that polls the Eatery (and related) models from the Eateries MS - All
    * writing the api_return_list_of_restaurants_given_category_and_location function view - Ariana and I
* In the Foodies MS poller, we decided to flatten the EateryLocation data into the EateryVO model.
* It was a nice realization that while api_return_list_of_restaurants_given_category_and_location is a function view that takes care of a GET request, it creates instances of YelpLocationSearchTerm, YelpCategorySearchTerm, and YelpResult models as a side effect!

## June 08, 2022
Today, I worked on:
* Ariana and I fine tuned the yelp integration

* Our api_get_yelp_category_and_location function is now able to take in a location and category input and it will be used in the front end to take in search input form the user.

* A struggle that we have been going back and forth on is the many to many relationship and how to pull from the eateries microservice to the foodies/owners microservices. 

* We learned that the pattern of categories that the yelp api takes and now know how to normalize out inputs form the users and feed them into the yelp request parameter.


## June 07, 2022
Today, I worked on:
* Ariana and I worked on finishing the views for the models in the eateries microservice

* We changed the many to many holder of the relationship between Eatery and Tag to live on the Eatery model. Also a sweet AHA moment learning that we can chose what side to put it on and it doesn't matter. 

* Huge aha moment was when Ariana thought about using the get_extra_data() function to add in the many to many field because of the circular logic from the encoders because we needed to include the encoders into eachother but couldnt because of inheritance laws, so we added in the extra data to one encoder.

## June 06, 2022
Today, I worked on:
* We worked as a team towards finishing the eateries microservice by creating views for specifically getting the eateries.

* We talked about incorporating a loop somewhere to go through the many to many lists and record each as part of that eatery instance but we were not sure on how to do that or where that goes. We also struggled with adding the categories to a list in the views and found that the many to many manager had a method .add() that we were able to use for each iteration through the list we are getting from the request.

* Ariana (the GOAT) made additions to the json.py file in the common directory so that our model encoder would be able to return many to many relationships as nested object. 

* Tuesday morning this was the AHA ^

## June 04, 2022
Today, I worked on:
* I worked on Testing the Models, Views, and Poller service

I tested Owner and Eateries Models through the admin panel, I got the Owner and Entity GET requests to go through insomnia, I got the poller service working and container running. 

I had trouble getting the POST request working through insonia, manytomany manager wasnt serializable, need to dive into how to fix this issue.

No AH-HA's today

## June 03, 2022
Today, I worked on:
* We split up into pairs today, Ariana and myself have started the models implementation for the Owners service.

As a team we got two different yelp api requests to come through with the parameters and output we were looking for.

We were able to use the Yelp documentation to guide the acls file design. Ariana, David and I spoke about the change of the eateries microservice handling all the eatery sub models, although now we realize that was logical in the first place.

Our ah-ha moment today was getting the yelp request to go through and talking to curtis on our new method to collect yelp data through user requests, also using a bot to make get requests to users to populate our database.

## June 02, 2022
Today, I worked on:
* We split up into pairs today, Ariana and myself have started the models implementation for the Owners service.

Ariana and myself worked on creating the models for the owners microservice. We are waiting to create the EateryVO and OwnerVO for obvious reasons of the Respective microservices are not built yet containing the Entities of those VOs.

We had some fun digging around with how to handle the hours of operations set-up. We decided to create a list of unique values tied to the weekdays, use that with the "choices=" argument in the PositveSmallInterger field, then used the Meta class to order that field by a "start_time" field and then we constrained it to be uniquely together based on start and end time fields. We Also had merge issues because we forgot to add the pycache to the gitignore file. 

We had an ah-ha moment by finding the solution I described above. This was an issue we worked through and eventually we were able to identify in the admin panel tht we were getting back the information and formatting we were looking for. Chris gave us the command " find . -name "*.pyc" -exec git rm -f "{}" "


## June 01, 2022
Today, I worked on:
* Creating the YML file with my team and creating the virtual environment for the project

We worked on the complete file. We added the 4 services foodies, owners, users, eateries. We also created 3 databases, one to support all the services and one for each Yelp and Google Maps data. We also added the react service to the compose file.

We went through a lot of error handling of moving directories around and changing files to meet the requirements. Because we are not creating the data base we decided to use the postgres:14-2-bullseye image for our database. We still need to understand the environment variables we set for the services and the multiple database file we addded.  

We had a great aha moment when we got all our containers to build and compose-up. We figured out how to incorporate the multiple database file

## May 31, 2022
Today, I worked on:
* Updating the data-models.md and ghi.md - bounded context formulation

The team and I worked on identifying the bounded contexts for our project. We wanted to look into whether or not we were going to use microservices or a monolith and if we are using microservices how will we communicate with the data. 

As a team we struggled to identify the realtionship of the skewered model and our restaurant model. It was hard to determain if it was a many to many or one to many relationship. 

We later got confirmation from an instructor that it was best to have a one to many relationship between our data for the purposes we needed. We also were able to finish a rough draft of our bounded context after establishing some core functionalities of our project.

## May 30, 2022
Today, I worked on:
* Updating the data-models.md and ghi.md

I began designing the Domain Driven Design in Exaclidraw with my team. We finished almost all of the front end conceptual designs. Working with changes in the data-models and the effects it has on the front end design. 

I realized that we had more work to do with the data models and api end points before we could put together a comprehensive collection of designs.

One aha moment was reconfiguring our data models to better reflect our core application functionality. We now wont have a yelp account requirement and now offer a create account form for non Yelp users.

## May 27, 2022

Today, I worked on:
* Updating the apis.md and ghi.md

Ariana, Cameron, David and I all worked as a group to first, identify which API endpoints our app would need, and second, update the api.md file to include details of input/output for each API endpoint.

I had a tough time figuring out how we will handle our user microservice's models for the Users. We are unsure if we will use Django base user or change the default. Still unsure on how to connect to the login endpoints if we don't decide to use LoginRequiredMixin from Django.

Thinking about and working through the API endpoints while imagining the GHI was very helpful in visualizing what the process of building the app would look like.