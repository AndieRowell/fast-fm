# Scratchpad

## FastAPI
- **uvicorn main:app --reload

## Alembic
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

## SQL Tools/Postgres
- how to use
    - click on sql tools extension
-
