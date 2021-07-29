# _Quick Check Test Project_
-   -   -
## Description
A project that consumes the HackerNews API periodically(5 minutes) saves 
the content to a databases, exposes API endpoints for easy consumption and gives an interface for browsing the saved objects. 

***Originally for a [code test](https://form.jotform.com/211856214308452) for a job application.***

### _Requirements_
* Have Python Installed
* Have redis Installed 
    * On windows install Ubuntu WSL with [here](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10)
    * install  and activate redis on WSL with [this](https://anggo.ro/note/installing-redis-in-ubuntu-wsl/)
    * install and activate redis on Linux(Ubuntu) with [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
* Get redis running with
  * `sudo service redis-server start`
  * `redis-cli`

## _To run on Local_
* Navigate to the Project Directory
* Activate a Python virtual environment
* run `pip install -r requirements.txt` in terminal
* run `celery -A QuickCheckProject beat` 
* Open another terminal and run `python manage.py runserver`

The Project should be up and running at this point

## _Routes_
* All routes are relative to the base url
> http://127.0.0.1:8000/ : The base url has a list of recent stories, both pulled from Hacker news and created on the API

>http://127.0.0.1:8000/story/{story_id}/:  The detail page Containing the detail of a story and its descendants(comments etc) can be reached by clicking on a story title on the Story List Page 

***The Search and filter functionalities can be accessed from the navigation bar***

***Documentation to the api can be found [here](https://documenter.getpostman.com/view/15225360/TzscqSxE)***




