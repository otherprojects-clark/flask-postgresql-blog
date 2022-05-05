# pgAdmin
pgAdmin is just like the GUI version of **psql**. 

### Getting Started
If you run pgAdmin for the first time, it will prompt you to set the master password for it. So please remember it after you set the master password.

After that, pgAdmin will automatically prompt you to type the password for user _postgres_.

Password: postgres

After connection to the server, it should show up all databases, login/group rules, and tablespaces.

##### Creating a User/Role
- Step 1: Right click  "Login/Group Roles", hover "Create", and "Login/Group Role"
![](./img/pgadmin_createuser.png)
- Step 2: Name the user as "**blog**"

![](./img/pgadmin_name.png)

- Step 3: Set the password for "blog" as "blog"
![](./img/pgadmin_pw.png)

- Step 4: Set the following privileges for "blog" below:

![](./img/pgadmin_privileges.png)

- Step 5: Click **Save** to create the user.

##### Creating the Database

- Step 1: Right click  "Databases", hover "Create", and "Database"
![](./img/pgadmin_db.png)

- Step 2: Enter the name of your database as "**blog**", and switch the owner of this database to previously created user named "**blog**"

![](./img/pgadmin_dbname.png)

- Step 3: Skip other tabs, and click **Save** to create the database.

After doing all these steps, now Flask is ready to connect to the server and "blog" database.