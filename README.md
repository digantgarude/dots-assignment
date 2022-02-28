# Dots

## Installation

### Using docker
(Make sure the docker-compose file exists or cd into the appropriate directory.)

```bash
docker volume create --name=data
```

In Mac OS and Windows
```bash
docker-compose up
```

In Linux based system
```bash
sudo docker-compose up
```

### Normal Way

* If you're using conda to manage environments.

```bash
conda create --name dots python=3.10
conda activate dots
```

* If not conda then install python `v3.10` 
  
```bash
pip install -r requirements.txt
```

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run django server
```bash
python manage.py runserver
```

---

### To test the API Calls (Optional):

> Import the `Dots_Assignment.har` file into Insomnia or Postman or other compatible client.

---

### Main File Structure:

> `dots/player_apis/views.py` -> All the views and functions.

> `dots/player_apis/urls.py` -> All routing info is managed here.

> `dots/dots/urls.py` -> Main `/api` route is defined here.

> `dots/player_apis/models.py` -> Models used are defined here.

> `dots/Dockerfile` -> Docker File

> `docker-compose.yml` -> Docker Compose

---

## Generate Requirements.txt
```bash
pip3 freeze > requirements.txt
```

## NOTE : 

* migrate  - which is responsible for applying and unapplying migrations.
* makemigrations - which is responsible for creating new migrations based on the changes you have made to your models.
* sqlmigrate - which displays the SQL statements for a migration.
* showmigrations - which lists a project’s migrations and their status.
* [Migrations Help](https://docs.djangoproject.com/en/3.2/topics/migrations/)