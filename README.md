# Flesh Eating Youkai
## What's that?
Fey is a framework built on top of Pygame designed to make the development of  2D games/application in Pygame easier. 
My goal for this project is to recreate one of the Touhou main games with fey.

## Fey's current status 
Unfortunately fey is currently unuseable since the development has just started. Many features are not implemented yet and documentation is missing.
Of course i am looking forward to change this :D

## Quickstart
**NOTE:** Python 3.9+ is required to run fey and the example
<hr>
To run the example:

* **Clone the repository**
    ```shell
    git clone https://github.com/ShisatOwO/flesh_eating_youkai
    ```
* **Install Pygame**
    ```shell
    pip install pygame
    ```
* **Execute the example**

    Navigate into the repo you just cloned and execute
    the python file located at "*app/app.py*"
    
    Dont forget to add the root of the repo to your PYTHONPATH, otherwise python
    will not be able to locate the "*fey*" package. The commmands below will add fey to the
    PYTHONPATH temporarely.
    
    **Linux/Mac**
    ```shell
    cd flesh_eating_youkai && PYTHONPATH=./ python app/app.py
    ```
    
    **Windows**
    ```cmd
    cd flesh_eating_youkai
    set PYTHONPATH=%PYTHONPATH%;"./"
    python app/app.py
    ```
 
 ## Note
 This README is temporary and will hopefully get more detailed as fey grows
