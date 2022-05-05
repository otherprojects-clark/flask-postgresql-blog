# psql
psql is a PostgreSQL interactive terminal. Often used for server administration.
### Getting Started
To get started, type this on your terminal: `psql -U postgres`. And it will prompt for password which is _postgres_. (Make sure your PostgreSQL Server is running!) After connection it should look like this: 
![](./img/psql.png) 
Now copy and paste this to psql:
```sql
create user blog with
  superuser
  nocreatedb
  nocreaterole
  noinherit
  login
  replication
  connection limit -1
  password 'blog';
```
This will create user/role named **blog**.

And also copy and paste this:

```sql
create database blog with
  owner = blog
  encoding = 'utf8'
  allow_connections = true
  connection_limit = -1
  is_template = false;
```
This will create a database named **blog**.

And that's it. No need to copy paste the contents inside **schema.sql**
Flask will automatically create that table.