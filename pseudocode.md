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
- using CRUD - (create, read, update, delete)
    - think of this from the perspective of a **user**
        - a user wanting to login
        - sort/filter through their playlist, saved songs
        - create, delete, & edit a playlist
        - the possible 'endpoints/routes' a user will want to go to
    - think of this from the perspective of a **developer**
        - a developer wanting to edit the database
        - creating a new table as a new feature (new type of data to store)
        - having the ability to delete a previous 'outdated' feature in the database
        - making sure the user's information is secured - hashing their password
        - consider the user's journey to have minimal pain points
            - not having to login again - refresh token works flawlessly in the background
        -

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
- authenticate the user

## Alembic Data Migration:
### Commands for the CLI:
- to install
    - python -m alembic init alembic
        - *NOTE - creates files - need to edit according to documentation*
- to migrate data
    - python -m alembic autogenerate (check this)
        - once models are done
            - generate your code in the upgrade/downgrade functions
- to upgrade or downgrade - *(updating/deleting current head - metadata - aka save points)*
    - python -m alembic upgrade head
    - python -m alembic downgrade head

### Notes for using Alembic:
- save a base model in a separate file to be imported for compartmentalization
