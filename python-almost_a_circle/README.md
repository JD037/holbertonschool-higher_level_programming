# Almost a Circle Project
This is a project designed to consolidate your knowledge of everything about Python:

Import
Exceptions
Class
Private attribute
Getter/Setter
Class method
Static method
Inheritance
Unittest
Read/Write file
You will also be introduced to:

Args and kwargs
Serialization/Deserialization
JSON
Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python 3.8.5
Ubuntu 20.04 LTS
Installing
Clone this repository
git clone https://github.com/<your_username>/python-almost_a_circle.git
Running the tests
You can execute all tests by using this command:
python3 -m unittest discover tests
Or you can test file by file by using this command:
python3 -m unittest tests/test_models/test_base.py

## Deployment
Add additional notes about how to deploy this on a live system

Built With
Python 3.8.5

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

### Versioning
For the versions available, see the tags on this repository.

### Authors
See also the list of contributors who participated in this project.

## Acknowledgments
Hat tip to anyone whose code was used
Inspiration
etc

## Project Tasks
Base class: Write the first class Base. This class will manage id attribute in all your future classes and to avoid duplicating the same code.

First Rectangle: Write the class Rectangle that inherits from Base. This class will have private instance attributes for width, height, x, y, each with its own public getter and setter.

Validate attributes: Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).

Area first: Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

...More tasks to come...

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
Resources
args/kwargs
JSON encoder and decoder
unittest module
Python test cheatsheet