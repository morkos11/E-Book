# E-Book
THIS PROJECT IS FOR THE ITI GRADUATION PROJECT


# Instillation
1- download git on ur machine

2- choose ur directore in cmd (prefer putting it in desktop)

3- write this command ==> git clone https://github.com/morkos11/E-Book.git


# Install requirments
1- Enter the directory where project data saved 

2- create env in the directory

3- activate the env the install the requrements from requirements.txt file ===> pip install -r requirements.txt

# First time to runthe app
1- python manage.py makemigrations

2-python manage.py migrate

3-python manage.py runserver


# Create super user 
1-python manage.py createsuperuser 

# REPO DEPARTMENTS
1-the repo is organized in three apps with the core app which is the main and where the home page is viewed  

2-accounts-app: every thing relate to login,logout,signup,forgetpass found in this app 

3- users-app: every thing about the profiles and search found on it 

4- books-app: contain all views about books,update,delete,add them too

5-each app has its own templates folder

