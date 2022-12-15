# Overview
Big Data project 

# Installation steps

1. Simply clone the repository
	```
	git clone https://github.com/NastyaTretyakova/big_data_project.git
	```
2. In the repo, Navigate to dags and logs locations as needed.

3. Run in the Terminal following command  to up containers.
	```
	sudo docker-compose up
	```
4. The `docker-compose up` will up docker containers and then display the following logs in terminal.

5. After building docker containers, create additional window in terminal and run there next command:
   ```
	python3 producer.py
	```

5. Then create one more window in terminal and run there next command:
   ```
	python3 consumer.py
	```

5. Tap on your web browser link:
   ```
	https://localhost:8080
	```
	You will see the main page of the airflow.

6. Enter username = gpadmin and password = pivotal

7. Add connection to airflow: Go to Admin and click on the button "Connection". Write connection id = postgres_default, login = test, password = test, host = db, port = 5432 and click "Save"!

8. Run Dag "prepare_data"

9. Success!)
