# Journaling

## Guidelines
* The date of the entry
* A list of features/issues that you worked on and who you worked with, if applicable.
* A reflection on any design conversations that you had
* At least one ah-ha! moment that you had during your coding, however small. 

## June 1, 2022
* Our group discussed that restaurant and restaurantVO should be a strict many-to-one relationship. The skewered restaurant will be many and restaurantVO will be one. We also discussed that the skewered_restaurant model will represent one single skewered restaurant. This helps clear things up in our BoundedContexts drawing. 

* Our group worked together getting the docker-compose.yaml file working. We were each able to provide solutions for any errors we ran into which helped give a smooth workflow. We did have an issue where the database was having an issue accessing all of the individual containers. This was because the create-multiple-databases.sh file was not executable, so we finally worked through that and resulted in getting all of our Docker containers up and running. Realizing that we needed to change the mode of the create-multiple-databases file to make sure it was executable was a big moment for me. That file was initially only a read/write file. This helps clear up any issues in the future for any database work I may do. 

## May 31, 2022
* Today, the group got together and we identified bounded contexts within our application. Initially, it seemed very daunting, but breaking down the models and grouping them into their respective microservices, really helped give a sense of foundation and structure before we even began coding. We also identified our value objects and the relationships between the models, i.e.: one-to-many, many-to-many, etc. 

* Things really clicked for me when we were able to identify what it was that we wanted inside each of our microservices and realizing what the value objects were. 


## May 27, 2022
* Ariana, Brandon, Cameron, and I worked together to figure out the API endpoints needed and we also went through the apis.md file to decide on the input and output for the individual API endpoints. 

* During our discussion, it was difficult to pinpoint what input was needed for each endpoint and what the output would be as well. Specifically, remembering whether or not the output would have an object returned inside of the JSON, like "restaurant" would return only
a single value or an entire restaurant object. 

* Being able to have a visualization of the layout of our application by creating wireframes and also documenting it in the ghi.md file helped me
gain a better understanding of the functionality of our application and how to make things efficient from the user's standpoint. 

