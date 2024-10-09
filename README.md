# Django Blockchain

### Create environment variables:

Rename template.env to .env

```bash
mv template.env .env
```

### Run docker compose

```docker
docker-compose up --build
```

### Run the management command to get the Transfer Events
#### Using makefile

```makefile
make seed
```

#### Using manage command 

```python
python manage.py seeder
```