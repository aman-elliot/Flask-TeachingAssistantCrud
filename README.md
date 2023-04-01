# *Flask-CRUD*

This is a Flask web application which enables users to keep a record of the teaching assisstant data. Users can Create, Update, Delete and Retrieve data from the maintained database using the APIs.






## Technologies

- **Flask Web Framework** - Django is a back-end server side web framework. Django is free, open source and written in Python.
- **SQLalchemy** - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **JWT** - JSON Web Token (JWT) is a compact URL-safe means of representing claims to be transferred between two parties.
- **Alembic** - Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database.

## API Reference

![image](https://user-images.githubusercontent.com/55498772/229296895-c4b06e70-4a6d-4255-a938-56af2c85731c.png)

## Installation and Usage

1. Clone the project.
    ```
    git clone https://github.com/aman-elliot/Flask-TeachingAssistantCrud.git
    ```
2. Run virtual environment in the root folder
    ```
    python -m venv vevn
    venv\Scripts\activate
    ```
3. Install required packages using requirement.txt in the movieCollection folder.

    ```
    pip install -r requirement.txt
    ```
    
4. Run migrations
    ```
    flask db init
    flask db migrate
    ```  
5. Run Flask
    ```
    flask run
    ``` 
6. Run Swagger for API references
    ```
    http://127.0.0.1:5000/swagger-ui
    ```     
   
