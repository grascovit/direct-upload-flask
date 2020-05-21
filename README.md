# Direct Upload
Simple Flask API to demonstrate how direct upload to AWS S3 is done.

### Requirements
- Python 3.8
- PostgreSQL 9.5+

### Setup
- Create a new virtual environment
- Install the required packages using `pip install -r requirements.txt`
- Create a new PostgreSQL database called `direct_upload` (or the name you prefer):
```
sudo -u postgres psql
CREATE DATABASE direct_upload;
\q
```
- Create the `.env` file copying the example file: `cp .env.example .env`
- Input your AWS credentials and change the `DATABASE_URL` if you have custom credentials: `postgresql://<user>:<password>@<host>:<port>/<database_name>`
- Run the migrations with `flask db upgrade`
- Run the API with `flask run`
