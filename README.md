# Purpose :

Purge your pipeline's history using the API.

# How to use it : 

From your profile's page create a API key with "api" right.

Setup the endpoint URL (default is gitlab.com)

Change "purgeRepo" value.

Install requests with pip 
  pip install requests

Launch the script 
  python gitlab-purge.py my-secret-api-key

I provide a simple .gitlab-ci if you want to schedule the tasks.

# Use it through Gitlab-ci 

Change the variable : "purgeRepo" in order to not kill the pipeline.

There is two way to use it : 

- Launch the tasks manualy and init the variable when launching the pipeline
- Create & setup a CI/CD variable name API_TOKEN with your api token

Enjoy the script will prompt you which Project is doing + which pipeline it delete.
