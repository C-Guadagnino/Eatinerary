# Journaling

## Guidelines
* The date of the entry
* A list of features/issues that you worked on and who you worked with, if applicable.
* A reflection on any design conversations that you had
* At least one ah-ha! moment that you had during your coding, however small. 

## June 9th, 2022
* Today the group reconvened and we worked on finishing up the poller.py file inside the Foodies microservice that polls data from the Eateries microservice. After we got to a good stopping point, the group broke off and pair-programmed where I teamed up with Cameron.
* Cameron and I worked on getting more of the function views done in the views.py file in the Foodies microservice. We were able to create, retrieve, update, and delete skewered restaurants that the foodie uses. We got a little stuck when it came to the creating of a skewered restaurant. We were not sure how to call the eatery object, until Ariana came by and helped us realize that we could just grab the eatery object by it’s href that we associated it with earlier. 
* I added in some more view functions for the Reviews model, but still needed to dial them in. Basic view functions such as list all reviews, create a review, get details of a single review, update a review. 
*  think today’s a-ha moment for me was when we were working on the poller file and I learned that we could “flatten” the data from EateryLocation into the EateryVO model and we didn’t have to make a special VO model for EateryLocation, which would have caused a lot more work. 

## June 8th, 2022
* Brandon and Ariana: close to being done with eateries microservice minus the Yelp stuff. They now have tag as part of the Eatery object the same way category is. No POST for category, added POST. Get and Post for tags, open_hours, as well as the specific open_hours_singular, and the images views up and running. That’s all of the models covered in the Eatery side. Basically just added more views yesterday. 
* Cameron and I worked on building out the models, views, encoders, urls, in Foodies microservice. Fixed a couple of settings in the Docker-compose yaml file to get the Poller file working. We discussed how our models would need to be configured when polling data from the Eateries microservice. 
* Still having a-ha! moments with Docker and learning about when to re-start our containers depending on what files we change and modify, what volumes to delete, and when to rebuild images. 

## June 7th, 2022 
* Today I worked with Cameron, ran into a migrations issue for our users-api container in Docker. It was not getting the DJWTO_SIGNING_KEY environment variable which was needed although it was in our docker-compose.yaml file. We ran the following command: docker run -it -v "$(pwd)/users/api:/app" -w "/app" -e "DJWTO_SIGNING_KEY=qwerty" restaurant-repo_users-api bash. This let us assign a value to the signing key to help us bypass that error, then re-ran our python manage.py makemigrations inside the container, which finally allowed us to apply migrations. Afterwards, we exited the container and brought up the services again, which got our users-api_1 container running, so that we could use the localhost:8070 port it was running on to use the Django admin to test out our views for the Users microservice. We were able to get API endpoints to function in Insomnia for getting all users, creating a user, and getting the details of a single user. 
* I feel like my breakthrough moment today was learning a little more about how Docker works, and learning new commands that allow you to override the containers. 

## June 6th, 2022
* The group worked on the Eateries microservice, specifically the api_eateries view function. We were having an issue trying to serialize a model that was using a ManyToMany relationship and resulted in us getting a TypeError for “ManyRelatedManager”. We each tried to implement many different solutions, but ultimately the ModelEncoder needed to be updated to handle the objects associated with ManyRelatedManager. 
* I moved the Dockerfile.dev, requirements.txt into the poll directory where I created a poller.py file for the Foodies microservice to poll from the Eateries microservice for the necessary data. I also coded the rough draft of our EateryVO model based on what was in our data-model.md file we all worked on. 
* My a-ha moment pertains to this day, but wasn’t really spawned on this day, when Ariana showed us that by modifying the ModelEncoder, we could then handle the objects of type ManyRelatedManager error we were getting on this day.

## June 3, 2022
* * As a group we worked on creating the docker-compose.yaml file. We ran into issues with the create-multiple-databases.sh file, since it was only set as a read/write file and not “executable” in the file system. We only identified this issue after not being able to get our PostgreSQL database container running in Docker. After running a specific command in the terminal, we could see that the file only had “rw” (r = read, w = write). It needed to be set as rwx, (read, write, and x = executable). This is an attribute of the filesystem, not the file itself. The command we ran in the terminal was ls -al db to see what the files are readable, writeable, executable, etc. In order to change the file from read/write only to include executable, we ran the command “chmod a+x db/create-multiple-databases.sh”. 

## June 2, 2022
* The group broke off into twos for pair-programming, Brandon and Ariana paired up to write the Owners microservices side of things, while Cameron and I teamed up to take on the Foodies microservice. We wrote the models for the Foodies microservice and tested it out by creating a superuser and using the Django admin to test it out.  We also wrote a couple of basic functions and a Foodie Encoder in the views file, so that we could use Insomnia to test out our API requests and see what output we were getting. Near the end of the day, the group reconvened and when it came time to commit my work, Brandon and Ariana informed me that I needed to delete all of the pyc files because we never included it in the gitignore file. Understanding that while it’s ok to have extra files called out in the gitignore file, it’s not okay to have extra files committed to gitlab. 

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

