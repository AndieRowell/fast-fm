# FAST FM PROJECT
- create a music library database/API with FastAPI

## Tech Stack
- python
- fastAPI
- alembic
- postgreSQL
- oauth2

## Plan:
- db diagam of all the relationships within music library
- determine:
    - database design
        - classes
        - models
        - schemas
    - queries
    - API structure
    - routes/endpoints
        - ex. /api/v1/**[object]** --- /api/v1/songs
    - http methods:
        - GET - all, filtered, single instance of models
            - ex. /api/[model-name]/[primary-key]/
        - POST - for each model to be made
            - ex. /model-name
        - UPDATE - for each model to be edited/updated
            - ex. /model-name/pk
        - DELETE - for each model to be deleted
            - ex. /model-name/pk
    - http status codes:
        - 404 NOT FOUND
            - ex. if the user tries to look up a song id that doesn't exist
        - 201 CREATED
            - ex. tells the user the 'thing' has been successfully created
            - typically sent after POST/PUT requests
        - 204 NO CONTENT
            - ex. there is no content to be sent for this request
            - NOTE - make sure don't want to contradict


## Consider Perspectives:
- using **CRUD** - (create, read, update, delete)

    - think of this from the perspective of a **user**
        - a user wanting to login to use this app
        - the possible 'endpoints/routes' a user will want to go to
         - create, delete, & edit a playlist
        **C**reate:
            - create an account (username, password, etc)
            - create a playlist
        **R**ead:
            - sort/filter through their playlist, saved songs
            - select one song
            - look at all the songs in a playlist
            - look at an artist...
            - etc...
        **U**pdate:
            - add a new song to their playlist
            - rename a playlist
        **D**elete:
            - delete a song from a playlist
            - delete all songs from playlist
            - delete a playlist
            - delete all playlist
            - delete account? - *stretch*

    - think of this from the perspective of a **developer**
        - making sure the user's information is secured - hashing their password
        - consider the user's journey to have minimal pain points
            - not having to login again - refresh token works flawlessly in the background
        **C**reate:
            - creating the database
            - creating a new table as a new feature (new type of data to store)
        **R**ead:
            - pull information to check user accounts registered
            - check/read data stored in databse
        **U**pdate:
            - a developer wanting to edit the database structure
            - a developer wanting to edit the data

        **D**elete:
            - having the ability to delete a previous 'outdated' feature in the database
            - deleting all tables
            - deleting a user
            - deleting specific data

## Consider
- information the user can recieve back to understand what is happening that they can't see
    - helpful information to our frontend
    - aka defensive programming
    - http status codes for the future frontend to recieve to know if something works or not
- how the user might want to see/organize their music when using the app
- the relationships between tables/categories
    - one to one
    - one to many
    - many to many

    - parent to child
    - parent + parent to child
    - parent to parent

- extra features of the app
    - likes
    - follows
    - total time of song, playlist, album
    - production credits - tidal wave app has this feature
    - multiple owners/editors of a playlist

## Database Design Outline
### Parent Tables (named as plural, ):
- users
- songs
- artists
- albums
- genres
- playlists

#### stretch possibilities:
- follows
- likes
-

### Child/Bridge/Pivot Tables:
- user/playlist

- song/artist
- song/album
- song/genre
- song/playlist

- artist/album
- artist/genre
- artist/playlist

- album/genre
- album/playlist

- genre/playlist

### Relationship Statements:
- many songs to one artist
- many songs to one album
- many songs to one genre
- many songs to one playlist

- many artists to one song
- many artists to one album
- many artists to one genre
- many artists to one playlist

- many albums to one song - ???
- many albums to one artist
- many albums to one genre
- many albums to one playlist

- many genres to one song
- many genres to one artist
- many genres to one album
- many genres to one playlist

- many playlists to one user
- many playlists to one song - ???
- many playlists to one artist - ???
- many playlists to one genre - ???
- many playlists to one album - ???

- many users to one playlist

### Checklist for Tables:
- primary key
- foreign key
-

## Oauth2 - authentication of user
- create access token
- hash the user's password - securing the info
- encode and store the user's data within the database
- registering the user - user account to be created
- authenticate the user to be allowed to pull data

## Alembic Data Migration:
### Commands for the CLI:
- to install
    - python -m alembic init alembic
        - *NOTE - creates files - need to edit according to documentation*
- to migrate data
    - python -m alembic autogenerate (check this)
        - once models are done to be inserted...
            - this will generate your code within the upgrade/downgrade functions
- to upgrade or downgrade - *(updating/deleting current head - metadata - aka save points)*
    - python -m alembic upgrade head
    - python -m alembic downgrade head

### Notes for using Alembic:
- save a base model in a separate file to be imported for compartmentalization


## GENERAL NOTES/REMINDERS:
- pydantic
    - own separate library that we can use with other python applications
    - use this to help us define what our schema should look like
    - fastapi just makes use of this
    - SCHEMAS
        - **data validation**
        - explicity define what the data should look like so that the frontend can send you back exactly the data you expect
        - *FORCE* the userr into a **schema** - we want to define exactly what the data should look like
            - this is like a *"contract"* between frontend and backend
            - *"if you don't send my data that looks exactly like this, I will give you an error"*
- sqlalchemy
    - MODELS
        - refers to a **class** that represents a table in a relational database
        - also called a **declaritive class** because it is created from DECLARATIVE BASE
        - the **model class** defines attributes that correspond to columns in the database table
            - *attributes* - the instances to sqlalchemy column types - *'str, int, etc'*

- general
    - relationships between tables are defined using sql alchemy's relationship attributes
    - **data validation** - we need to have defensive programming to get the exact data we want
    - when we extract data and save it - it is stored as a *pydantic model*
    - endpoints/routes - written plural - standard convention for api's
    - a path parameter always returns as a string
        - ex. int(id)
        - have to convert it sometimes?
    - api is going to start from the top and go through the list of all of our paths and find the first match
        - be careful with path parameters (variable could be many things) and the order of our structure of paths
        - have to be careful not to match requests that were meant for a different route
    - data goes through as JSON - have to extract the JSON
