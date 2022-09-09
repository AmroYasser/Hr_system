# Hr System
API for a tiny HR system, where job applicants can register as potential candidates and upload their resumes, and HR managers can log in and see the list of candidates and download their resumes.

## Features
- Candidates can register with their information.
- Hr managers (admins) can see the list of candidates via the list endpoint.
- Hr managers (admins) can download resume by candidate id via retrieve endpoint.
- Resumes are stored on **aws s3**

## Tech

Technologies used for this project:
- Python3
- Django
- Django rest framework
- Postgresql
- Boto3 and Django-storage (for aws s3)

## Installation
Create the database user and password and then create the database (assuming you're using linux):
```sh
sudo su - postgres
psql
CREATE USER postgres WITH PASSWORD 'postgres';
CREATE DATABASE postgres;
```
Install the dependencies then migrate and start the server.

```sh
cd Hr_system
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints
### create
At `http://127.0.0.1:8000/api/applicant-create-api/`
Candidate can register with his info.

![Alt text](README_pics/create.png?raw=true)

### list
At `http://127.0.0.1:8000/api/applicant-list-api/`
Admins (with ADMIN-X=1 in the header) can see the list of candidates ordered by registration date in descending order.
![Alt text](README_pics/list_admin.png?raw=true)

Not admin users can not see the list and get unauthorized status

![Alt text](README_pics/list_not_admin.png?raw=true)

### retrieve
At `http://127.0.0.1:8000/api/applicant-retrieve-api/<id>`
Admins (with ADMIN-X=1 in the header) can download the resumes by candidate id.

![Alt text](README_pics/download.png?raw=true)

Not admin users can not download and get unauthorized status

![Alt text](README_pics/no_download.png?raw=true)


## To be done
Frontend and UI.
