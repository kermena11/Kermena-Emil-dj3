# ITI Django Task - Database Version

The project now uses Django ORM with SQLite instead of hard-coded track data.

## What was changed
- Added `Track` model in `tracks/models.py`.
- Connected the Tracks app to the SQLite database through Django ORM.
- Tracks list is read from the database.
- Added Create, Read, Update and Delete operations.
- Added Django migrations for the Track model.
- Added real signup/login/logout using Django's built-in User model.
- Added an Add Track page and updated navigation.

## Run
```bash
cd myproject
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open:
- `/track/` - list tracks from database
- `/track/create/` - insert a track
- `/admin/` - Django admin
- `/signup/` - create a user
- `/login/` - login

The SQLite database file is created automatically by `migrate`.
