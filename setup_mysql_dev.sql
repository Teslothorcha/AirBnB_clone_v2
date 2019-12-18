--creates new user with privileges
CREATE IF NOT EXISTS DATABASE hbnb_dev_db;
CREATE IF NOT EXISTS USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db. * TO 'hbnb_dev'@'localhost';
GRANT SELECT  ON performance_schema. * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
