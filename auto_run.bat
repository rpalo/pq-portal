::This file is set to run on computer startup
::It lets the development server restart even
::upon computer restart

:: Activate virtual environment (using conda)
call activate website

:: Switch to project directory
cd C:\Users\ryan\Desktop\pq-portal

:: Run server, serve app on http port 80
python manage.py runserver 0.0.0.0:80

:: not sure if pause is required, but doesn't seem to hurt
PAUSE