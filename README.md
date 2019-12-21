# AirBnB_clone_v2
The goal of the project is to deploy on your server a simple copy of the AirBnB website.
# <a href="https://ibb.co/n0F13LS"><img src="https://www.pngkey.com/png/full/60-605967_airbnb-logo-png.png" alt="Sin-ti-tulo-1" width="100" height="80" border="0"></a> Airbnb

<a href="https://holbertonschool.com"><img src="https://i.ibb.co/RyBcXY6/cherry72.png" align="right" width="200" height="200" alt="cherry72" border="0"></a>

By this part of the project we not only have a console /command interpreter for
the Holberton Airbnb clone project, that can be used to store objects in and
retrieve objects from a JSON, but also it will has the possible to switch the
storage engine and use SQLAlchemy.

We have learned how to manage a console which classes allows us
to handle information like Users, places, states, cities and others ones by
changing the engine storage with SQLAlchemy.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Specific improvements

### Authors

 - [Kevin Yook] (https://github.com/yook00627)
 - [Juan David Marín](https://github.com/Teslothorcha) - 939@holbertonschool.com
 - [Doniben Jimenez](https://github.com/Doniben) - 921@holbertonschool.com
