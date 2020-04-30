# YoutubeSearch

## Project Goal
An API to fetch latest videos at regular intervals sorted in reverse chronological order of their publishing date-time from YouTube for a given search query in a paginated response.

## Setting Up
1. Create a MySQL database named `youtube`
2. Install dependencies by running `pip3 install -r requirements.txt`
3. Enter database credentials in `search/settings.py`
4. Run migrations by running `python3 manage.py makemigrations && python3 manage.py migrate`
5. Add API keys in `api/helpers.py` in the list `development_keys`
6. Run server by running `python3 manage.py runserver`
7. In another window, run celery worker by running `celery -A search worker -l info`
8. In another window, run celery beat by running `celery -A search beat -l info`
9. The paginated video data can be accessed at `http://localhost:8000/videos?page=[page_number]`