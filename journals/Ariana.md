# Ariana's Journal

## Temporary guidelines for myself:

In the journals, every day that you work on the project, you must make an entry in your journal after you've finished that day. At a minimum, you will need to include the following information:

1) The date of the entry
2) A list of features/issues that you worked on and who you worked with, if applicable
3) A reflection on any design conversations that you had
4) At least one ah-ha! moment that you had during your coding, however small

## May 30, 2022
Today, I worked on:
* Updating the data-models.md and apis.md

I cleaned up some of the models based on our group discussion from last week. Also updated apis.md to include more details as well as thinking a little more critically on whether a certain path is an API endpoint vs. GHI endpoint.

I realized I have a hard time differentiating API endpoint vs GHI endpoint for the login/sign up pages mainly because the implementation of login/signup isn't too clear to me. The distinction between API endpoint and GHI endpoint for NON-login/signup pages is pretty clear to me at this point.

Cleaning up some models to be one-to-many (while removing redundancy with nullable fields in other models) was enlightening! Also, being able to identify the need/use case for one-to-many relationships, many-to-many relationships is becoming easier and clearer.


## May 27, 2022

Today, I worked on:
* Updating the apis.md

Brandon, Cameron, David and I all worked as a group to first, identify which API endpoints our app would need, and second, update the api.md file to include details of input/output for each API endpoint.

I had a hard time clearly identifying what will be an API endpoint, and what will be a web/user endpoint, as some API endpoints could be required for its own web/user endpoint (e.g. login web endpoint requires an API endpoint that handles a POST request to create a foodie/owner instance?), and some API endpoints can be used for many web/user endpoints (e.g. the web endpoint that shows the list of restaurants per location, and the web endpoint that shows the list of Skewered restaurants would both use the API endpoint that handles the GET request to get a list of restaurants -- while the frontend handles how to filter that list of restaurants once returned by the API endpoint).

Thinking about and working through the API endpoints while imagining the GHI was very helpful in visualizing what the process of building the app would look like.