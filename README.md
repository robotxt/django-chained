# Django Blockchain

### Create environment variables:

Copy template.env to .env

```bash
cp template.env .env
```

### Run docker compose

```docker
docker-compose up --build
```

### Management command to get the Transfer Events
#### Using makefile

```makefile
make seed
```

#### Using manage command 

```python
python manage.py seeder
```

### Management command to delete event data
#### Using makefile

```makefile
make unseed
```

#### Using manage command 

```python
python manage.py unseed 
```

### API Endpoints

#### List of Events API
```
http://localhost:8000/api/events/
```

#### Event Details API
```
http://localhost:8000/api/events/<token_id>/
```