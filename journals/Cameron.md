## Guidelines:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

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
*  Today was a tribute to Curtis as a saving grace to our YAML. As a group we worked on creating the docker-compose.yaml file. We ran into issues with the create-multiple-databases.sh file, since it was only set as a read/write file and not “executable” in the file system. We only identified this issue after not being able to get our PostgreSQL database container running in Docker. After running a specific command in the terminal, we could see that the file only had “rw” (r = read, w = write). It needed to be set as rwx, (read, write, and x = executable). This is an attribute of the filesystem, not the file itself. The command we ran in the terminal was ls -al db to see what the files are readable, writeable, executable, etc. In order to change the file from read/write only to include executable, we ran the command “chmod a+x db/create-multiple-databases.sh”.

## June 2, 2022
* We decided that pair programming was for the best, David and I teamed up to take on the Foodies microservice. Together we wrote commented code to describe the models, then filled them in, to test this we created insomnia endpoints in the URLS as well as creating rudimentary views to eventually see it in Insomnia. We also wrote a couple of basic functions and a Foodie Encoder, so that we could use Insomnia to test out our API requests and see what output we were getting. Near the end of the day, the group reconvened and when it came time to commit my work, Brandon and Ariana informed us as a group that certain files needed to be added to our gitignore file as they were causing merging issues, we took care of this and the team logged off for the day.

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

I helped in the designing the Domain Driven Design in Exaclidraw with my team. Brandon took the lead and drew down all the visual models we would need. We finished almost all of the front end conceptual designs. There are a few tweaks that have to be made for it to look like a good production model, but it's getting there.

There were some errors with the API endpoints and data modeling that was adressed

We now wont have a yelp account requirement and now offer a create account form for non Yelp users, because of this we are able to create an easier mechanism.

## May 27, 2022

Today, I worked on:
* Updating the apis.md and ghi.md

Ariana, Brandon, David and I all worked as a group to first, identify which API endpoints our app would need, and second, update the api.md file to include details of input/output for each API endpoint.

We had quite the issue figuring out how we would handle the microservice aspect of our project, if we would even
be using that, turns out it was the best option for us at the time.

Working through the API endpoints has become very valuable as now the team has a clear understanding of what is required of us as we progress to creating the project