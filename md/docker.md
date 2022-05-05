# Docker

Change working directory to the same path as **Dockerfile**.

To Linux Users: add **sudo** if needed.

Build: <br>
`docker build -t flask-postgres-blog .` 

 Run (Windows): <br>
`docker run -d -p 5432:5432/tcp -v %cd%/postgres:/var/lib/postgresql/data flask-postgres-blog` <br>
 Run (Linux): <br>
`sudo docker run -d -p 5432:5432/tcp -v ${PWD}/postgres:/var/lib/postgresql/data flask-postgres-blog`

PostgreSQL Console: <br>
`docker exec -ti (container name or id) psql -Ublog`

Replace `(container name or id)` with your container name or id.

