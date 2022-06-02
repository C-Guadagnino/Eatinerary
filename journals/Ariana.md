# Ariana's Journal

## Temporary guidelines for myself:

In the journals, every day that you work on the project, you must make an entry in your journal after you've finished that day. At a minimum, you will need to include the following information:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

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