# How to Install
## MacOS and Ubuntu systems
### Easy-Peasy One-Liner
_Replace {variables} with the appropiate path_
`git@github.com:bananabrann/eb-jdavisarrangements.com.git && virtualenv <Your Enviroment Path>/eb-jdavisarrangements && source <Your Enviroment Path>/eb-jdavisarrangements/bin/activate && cd ebjdavisarrangements.com && pip3 install -r requirements.txt`
Then run local server with `python3 manage.py runserver`

### Step by Step
1. Clone repo `git@github.com:bananabrann/eb-jdavisarrangements.com.git`
2. Create virtual enviroment. Example: `virtualenv ~/.virtualenviroments/eb-jdavisarrangements`
> Download virtualenv with `sudo pip3 install virtualenv`, or `sudo apt-get install python-virtualenv`
3. `cd` into the jdavisarrangements directory, then install requirements: `pip3 install -r requirements.txt`
4. You're done! The website is used with Django. Start server and view the site with `python3 manage.py runserver`

## Windows systems
1. Switch to a Linux

# Deployment
For information on deployement, visit https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html