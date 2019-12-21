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

### Console Improvements
we have Updated the `def do_create(self, arg)`: function of our command
interpreter (console.py) to allow for object creation with given parameters:

	    - Command syntax: `create <Class name> <param 1> <param 2> <param 3>...`
	    - Param syntax: `<key name>=<value>`
	    - Value syntax:
	    	  String: `"<value>"` => starts with a double quote
		  	  - any double quote inside the value must be escaped
			  with a backslash \
			  - all underscores _ must be replace by spaces .
			  Example: You want to set the string My little house
			  to the attribute name, your command line must be
			  name= `"My_little_house"`
	    - Float: `<unit>.<decimal>` => contains a dot .
	    - Integer: `<number>` => default case
	    - If any parameter doesn’t fit with these requirements or can’t be
	    recognized correctly by your program, it must be skipped.

Also, this new feature will be tested here only with FileStorage engine.

### MySQL setup development

We Wrote a script that prepares a MySQL server for the project:

- A database hbnb_dev_db
- A new user hbnb_dev (in localhost)
- The password of hbnb_dev should be set to hbnb_dev_pwd
- hbnb_dev should have all privileges on the database hbnb_dev_db
  (and only this database)
- hbnb_dev should have SELECT privilege on the database performance_schema
  (and only this database)
- If the database hbnb_dev_db or the user hbnb_dev already exists, our script
  should not fail.

### MySQL setup test

We wrote a script that prepares a MySQL server for the project:

- A database hbnb_test_db
- A new user hbnb_test (in localhost)
- The password of hbnb_test should be set to hbnb_test_pwd
  hbnb_test should have all privileges on the database hbnb_test_db (and
  only this database)
- hbnb_test should have SELECT privilege on the database performance_schema
  (and only this database)
- If the database hbnb_test_db or the user hbnb_test already exists, your
  script should not fail

### Delete object

We updated the FileStorage: (models/engine/file_storage.py)

- Add a new public instance method: def delete(self, obj=None): to delete obj
  from __objects if it’s inside
- Update the prototype of def all(self) to def all(self, cls=None) - that
  returns the list of objects of one type of class. Example below with State -
  it’s an optional filtering

### DBStorage - States and Cities

We changed our storage engine and use SQLAlchemy

## Authors

 - [Kevin Yook] (https://github.com/yook00627)
 - [Juan David Marín](https://github.com/Teslothorcha) - 939@holbertonschool.com
 - [Doniben Jimenez](https://github.com/Doniben) - 921@holbertonschool.com
