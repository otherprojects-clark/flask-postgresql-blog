from postgres:latest
copy . .

env POSTGRES_DB=blog
env POSTGRES_USER=blog
env POSTGRES_PASSWORD=blog 

expose 5432
