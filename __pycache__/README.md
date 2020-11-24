** CONTACT BOOK **
In this project, the user has the ability to search, update and delete a list of contacts.

** Requirements:**
This program was built using python and SQL with Peewee throught the CLI. To run this you will need:

- Python 
- Postgres, or another equivalent program to run SQL
- Peewee
- Knowledge of Python and SQL
Opening the book
To access the contents of this app, you will need to do several things.

1. Make sure the latest version of Python is installed. I used Python 3.8.
2. Check if PostgreseSQL or a similar Object-Relational Database softare is installed. 
3. Run:
    ``` 
    pip install peewee psychopg2-binary autopep8

 To run the virtual environment.

1. In the terminal:
     ```psql``` 
     

Using the book:
Open the app, and run: python contacting.py to seed the database initially. Also make sure to run \c newcontacts then SELECT * FROM Contacts; to seed the SQL tables. To initially seed the database, run python contacting.py. Start the program: python contacting.py When the program is initiated, there will be a prompt that appears on the screen giving the user option of what they want to do with the app. The choices are:


1. To find a specific contact by first name, type the name of the person. Note that the contacts are currently case-sensitive, so make sure the contact you entered is correct
2. Follow the instructions from the Terminal: what contact would you like to update and delete?




** License **

Private License

All right reserve