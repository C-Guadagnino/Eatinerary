## Guidelines:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

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