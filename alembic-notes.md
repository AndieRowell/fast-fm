# Learning Alembic - Getting Alembic Started

## Commands
- **pip install alembic**
    - installs the library for you
- **alembic --help**
    - shows you all the possible commands you can do with alembic
- **alembic revision --help**
    - shows all the specific commands that work with revisions
- **alembic init**
    - initializes alembic
    - creates an alembic directory for us
    - do this first
- **alembic init --help**
    - shows us


## Procedure:
- pip install

- alembic init

- alembic --help
    - to see if we have to pass in any extra flags

- then have to give it a directory name
    - ex. alembic init alembic
        - alembic is the folder/directory name

- folder will then appear in your file structure outside of your app folder
    - alembic.ini file will also be created

- in the alembic folder will be an env.py file

- we need to make changes within this env file
    - because alembic uses sqlalchemy models - need to make sure it has access to your Base object (found in database.py file?)
    - have to import that Base object into the env.py file
        - we want to import this from models
            - by importing it from the models file - instead of from database file - this allows alembic to read all of our models
            - if you import directly from database it WILL NOT work
        - from app.models import Base
            - this gives access to all of the sql alchemy models
    - for "target_metadata = None" - need to change to "target_metadata = Base.metadata"

- go to alembic.ini file
    - have to pass in one value here which is the "sqlalchemy.url"
        - basically what's the url to access our postgresql database
        - ex. "driver://user:pass@localhost/dbname"
            - this shouldn't be different from the sqlalchemy_database_url you have in database.py
        - change to:
            - postgresql://postgres:postgres@localhost:5432/dbname
                - (default driver for postgres is psychopg)
                - (user is username for postgres)
                - (pass is password for postgres)
                - (running on localhost)
                    - can provide the port here - ex. localhost:5432
                - (dbname - database name (i think main repo name?))

            - BUT THIS IS ALL HARDCODING... (not great)
            - INSTEAD...

            - override the value for sqlalchemy.url that's stored in the alembic.ini file - instead withint the env.py file
                - under "config = context.config"
                - set up a new option
                    - "config.set_main_option()"
                        - meaning we can override any options we have in the alembic.ini file
                        - pass in a string
                    - "config.set_main_option("sqlalchemy.url, postgresql://postgres:postgres@localhost:5432/dbname")

                    - here should make sure have a config file that makes use of pydantic class called Settings
                        - so we can use settings object
                        - import settings into the env.py file so we can access all of our environment variables
                            - from app.config import settings
                            - so now we can override these config in env file

                    - change AGAIN
                        - within "config.set_main_option()"
                            - "config.set_main_option("sqlalchemy.url, postgresql://{settings.database_username}:{settings.database_password}@localhost{settings.database_hostname}:{settings.database_post}/{settings.database_name}")
                        - NOW we are not hardcoding any values at this point yay!
                        - alembic should be set!

- alembic --help
    see what commands we have
- when we want to make a change to our database we create a **revision**
