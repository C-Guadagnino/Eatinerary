## Guidelines:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

## Thursday, June 23nd, 2022
* Today we did CSS, and we did CSS through every aspect of the app, fully revitilizing the homepage, with new logos, spacing, image sorting, search bars, YOU NAME IT I DID IT. Hopped between teammates as we worked throuhout the day putting out small fires.
* ah-ha for me was figuring out how to uniformly create images in a card, and make them functional. 

## Wednesday, June 22nd, 2022
* Unfortunately, today my power went out so I was not a lot of use to the team, I continued to do CSS on the homePage and small edits throughout the app, PLEASE don't check my commit history for these days, as I was up late doing some silly commits

* Todays ah-ha moment has to be understanding more about how row spacing works on a page, and how that works with react-bootstrap

## Tuesday, June 21st, 2022
* Today I touched every single file and compiled a list of everything that need's to be done as far as CSS goes throughout the entire app and created a list of priority to design the front end uninformly.
* I also added in some rough styling to SkeweredHistory, SkeweredList, Create Review Form to mock it up like the wireframes and also for readability purposes. 
* Worked on the create a review form, for leaving a review for a skewered eatery. I ran into some minor issues getting the form to submit properly. We also decided on relocating the "Create a review" form to a separate page, and implementing the details of a review onto another page. 
* Later that night, I worked with Brandon on trying to get all skewered eateries for a specific foodie. We came to a stopping point when we realized we needed help handling the user's token, to possibly get the username out of it and populate the SkeweredList based on that information. 
* My a-ha! moment today was easily relearning CSS going back into this because I haven't used it since Mod 1


## Monday, June 20th, 2022
* I took the day off for the heavy work to do in the next two days haha...
* Fixed the way that the review table was presenting itself
* My a-ha! moment was learning how to write the onClick function


## Friday, June 17th, 2022
* Today I started working on the front-end side of the Foodies microservice. I began working on the MySkeweredList file, which is responsible for getting all of the eateries that a foodie has skewered. Coming to the front-end after working on the back-end for a while, definitely was challenging. It was a while since I had done any React stuff, so I resorted to old projects to help give myself a refresh of how things worked together. I also had some help from Cameron in getting the file set-up in the Nav.js and the App.js files. After I worked for a while, things started clicking again and I felt more confident. 
* I noticed that when we were trying to incorporate elements from Bootstrap that they weren’t appearing. I asked my team if they had it installed into our project, to which they said it was included in the package.json file. However, I remembered from older projects that the Bootstrap link needed to be included in the index.html file inside the public directory. After i included this link, all of the Bootstrap components worked! 
* My a-ha moment/tough thing I encountered was working with grid/layout aspects of the page. I was trying to do a rough mock up of our wireframe without wasting too much time. After a few failed attempts, I did some quick research and saw that the “trinity”/key to Bootstrap is to always use container-> row-> column to have your layout work properly. After I incorporated this, I was able to roughly maneuver divs, containers, etc. around where i temporarily wanted them.

## Thursday, June 16th, 2022


## Wednesday, June 15th, 2022


## Tuesday, June 14th, 2022
* Group got together to discuss dividing and conquering our application. We wanted to start working on front-end items to have them deliverable by the dead-line. 

* No real AHHA today, just a planning day.

## Monday, June 13th, 2022
* David and I worked together on the finished the GET and POST requests for the Reviews. We ran into an issue getting the “id” and “review_image” properties in our ReviewImageEncoder to work. To get the “id” to work, we had to remove the pk from the skewered_restaurant attribute of our Review model. It was trying to use this instead of the id like we were intending to. After removing the pk, the “id” finally worked in the GET request. We still had trouble getting review_images to work and will need to figure out a way to make this happen. When we were trying to make our POST request in Insomnia, I had forgotten that I already made a Review in the Foodies Django admin, so when I tried to create a review for a specific skewered restaurant, it errored out with “Id already taken for skewered_restaurant”. Realizing that skewered_restaurant is a OneToOneField and looking back on our README, we realized that we initially said we would only allow a foodie to create ONE review for a restaurant, not multiple. I deleted the previously made Review in the admin, made the POST request in Insomnia, and it worked. 
* My big a-ha moment was getting reminded on how one-one fields work compared with our earlier django apps, to what we worked on today. 

## Friday, June 10th, 2022
* David and I continued working on the api_views.py file in the Foodies microservice for Deleting and Updating a skewered eatery. We were not able to Delete a skewered_eatery from a foodie’s list, however, we realized we were deleting it from the database, which is not what we intended. We realized we had an “is_active” field on our model for Skewered_Eatery, so that when the foodie does delete it from their skewered_eatery list, it would change the status of “is_active” from true to false. We fixed this by filtering the SkeweredEatery by it’s id, then updating the property to false. 
* Another issue we ran into was trying to work with the skewered_restaurant attribute in Review, which had primary_key set to true? it gave us trouble because it was using the primary key of skewered restaurant as pk, when we wanted the id of the review. Needed to remove the primary_key setting from skewered_restaurant.
* The a-ha moment was realizing we needed to remove the primary_key from the skewered_restaurant attribute in the Review model, so that when we made the request, it would use the id of review, and NOT the pk of skewered_restaurant. 


## June 9th, 2022
* Today the group reconvened and we worked on finishing up the poller.py file inside the Foodies microservice that polls data from the Eateries microservice. After we got to a good stopping point, the group broke off and pair-programmed where I teamed up with David.
* David and I worked on getting more of the we wrote functional views, getting tripped up on creating the views of a skewered resturant, as the eatery object was hard to define, Ariana saved the day by giving us the information to grab the eater object by href
*  think today’s a-ha moment for me with David was when we were working on the poller file and I learned that we could “flatten” the data from EateryLocation into the EateryVO model and we didn’t have to make a special VO model for EateryLocation, which would have caused a lot more work. David and I both had the same ah-hah today. 

## June 8th, 2022
* Brandon and Ariana: close to being done with eateries microservice minus the Yelp stuff. They now have tag as part of the Eatery object the same way category is. No POST for category, added POST. Needed to somehow record Open hours Data
* David and I worked on building out the models, views, encoders, urls, in Foodies microservice. Fixed a couple of settings in the Docker-compose yaml file to get the Poller file working. We discussed how our models would need to be configured when polling data from the Eateries microservice. 
* Still having a-ha! moments with the way the YAML file works, and how we can add and create volumes in docker during different states.

## June 7th, 2022 

* (This jounral entry was based of David's as I drove the code today) 
* Today I worked with David, ran into a migrations issue for our users-api container in Docker. It was not getting the DJWTO_SIGNING_KEY environment variable which was needed although it was in our docker-compose.yaml file. We ran the following command: docker run -it -v "$(pwd)/users/api:/app" -w "/app" -e "DJWTO_SIGNING_KEY=qwerty" restaurant-repo_users-api bash. This let us assign a value to the signing key to help us bypass that error, then re-ran our python manage.py makemigrations inside the container, which finally allowed us to apply migrations. Afterwards, we exited the container and brought up the services again, which got our users-api_1 container running, so that we could use the localhost:8070 port it was running on to use the Django admin to test out our views for the Users microservice. We were able to get API endpoints to function in Insomnia for getting all users, creating a user, and getting the details of a single user. 
* I feel like my breakthrough moment was 100% learning about read/write/executable files.

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