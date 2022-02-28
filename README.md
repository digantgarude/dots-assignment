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