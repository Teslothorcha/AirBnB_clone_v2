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

In the following steps, you will make multiple changes:
* the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
* add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)
Please follow all these steps:
Update BaseModel: (models/base_model.py)
* Create Base = declarative_base() before the class definition of BaseModel
* Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
* Add or replace in the class BaseModel:
    * class attribute id
        * represents a column containing a unique string (60 characters)
        * can’t be null
        * primary key
    * class attribute created_at
        * represents a column containing a datetime
        * can’t be null
        * default value is the current datetime (use datetime.utcnow())
    * class attribute updated_at
        * represents a column containing a datetime
        * can’t be null
        * default value is the current datetime (use datetime.utcnow())
* Move the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self): and call it just before models.storage.save()
* In def __init__(self, *args, **kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
* Update the to_dict() method of the class BaseModel:
    * remove the key _sa_instance_state from the dictionary returned by this method only if this key exists
* Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete
Update City: (models/city.py)
* City inherits from BaseModel and Base (respect the order)
* Add or replace in the class City:
    * class attribute __tablename__ -
        * represents the table name, cities
    * class attribute name
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute state_id
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to states.id
Update State: (models/state.py)
* State inherits from BaseModel and Base (respect the order)
* Add or replace in the class State:
    * class attribute __tablename__
        * represents the table name, states
    * class attribute name
        * represents a column containing a string (128 characters)
        * can’t be null
    * for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
    * for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
New engine DBStorage: (models/engine/db_storage.py)
* Private class attributes:
    * __engine: set to None
    * __session: set to None
* Public instance methods:
    * __init__(self):
        * create the engine (self.__engine)
        * the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
            * dialect: mysql
            * driver: mysqldb
        * all of the following values must be retrieved via environment variables:
            * MySQL user: HBNB_MYSQL_USER
            * MySQL password: HBNB_MYSQL_PWD
            * MySQL host: HBNB_MYSQL_HOST (here = localhost)
            * MySQL database: HBNB_MYSQL_DB
        * don’t forget the option pool_pre_ping=True when you call create_engine
        * drop all tables if the environment variable HBNB_ENV is equal to test
    * all(self, cls=None):
        * query on the current database session (self.__session) all objects depending of the class name (argument cls)
        * if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
        * this method must return a dictionary: (like FileStorage)
            * key = <class-name>.<object-id>
            * value = object
    * new(self, obj): add the object to the current database session (self.__session)
    * save(self): commit all changes of the current database session (self.__session)
    * delete(self, obj=None): delete from the current database session obj if not None
    * reload(self):
        * create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
        * create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
Update __init__.py: (models/__init__.py)
* Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
    * If equal to db:
        * Import DBStorage class in this file
        * Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
    * Else:
        * Import FileStorage class in this file
        * Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
* This “switch” will allow you to change storage type directly by using an environment variable (example below)
	
### DBStorage - User

We updated User: (models/user.py):
* User inherits from BaseModel and Base (respect the order)
* Add or replace in the class User:
    * class attribute __tablename__
        * represents the table name, users
    * class attribute email
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute password
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute first_name
        * represents a column containing a string (128 characters)
        * can be null
    * class attribute last_name
        * represents a column containing a string (128 characters)
        * can be null
	
### DBStorage - Place

Update Place: (models/place.py)
* Place inherits from BaseModel and Base (respect the order)
* Add or replace in the class Place:
    * class attribute __tablename__
        * represents the table name, places
    * class attribute city_id
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to cities.id
    * class attribute user_id
        * represents a column containing a string (60 characters)
        * can’t be null
        * is a foreign key to users.id
    * class attribute name
        * represents a column containing a string (128 characters)
        * can’t be null
    * class attribute description
        * represents a column containing a string (1024 characters)
        * can be null
    * class attribute number_rooms
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute number_bathrooms
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute max_guest
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute price_by_night
        * represents a column containing an integer
        * can’t be null
        * default value: 0
    * class attribute latitude
        * represents a column containing a float
        * can be null
    * class attribute longitude
        * represents a column containing a float
        * can be null
Update User: (models/user.py)
* Add or replace in the class User:
    * class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user
Update City: (models/city.py)
* Add or replace in the class City:
    * class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities


## Authors

 - [Kevin Yook] (https://github.com/yook00627)
 - [Juan David Marín](https://github.com/Teslothorcha) - 939@holbertonschool.com
 - [Doniben Jimenez](https://github.com/Doniben) - 921@holbertonschool.com
