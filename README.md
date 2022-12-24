# Overview
Big Data project

The python service simulates an iOS device that generates events from hardware once every 1 second. The service must write data to Kafka Producer in real time. The Kafka Consumer service must connect to the topic, read all messages and write to the database. The Airflow DAG will subtract all accumulated data in the stg layer, filter the data with negative temperature and write it to the dds layer.


# Hardware requirements
- RAM >= 4000 MB;
- Ubuntu not older than 3.10

# System requirements
- OS Ubuntu (64-bit);
- Python interpreter installed;
- Docker tool installed;
- Docker Compose intsalled;
- Python packages installed: json, psycopg2, confluent_kafka, airflow, requests, logging, threading, time, dataclasses, datetime.

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
4. The `docker-compose up -d` will up docker containers and then display the following logs in terminal.

5. After building docker containers (We kindly draw your attention to the fact that all containers must run. Otherwise, for example, if the kafka container does not run, further scripts won't be able to work), create additional window in terminal and run there next command:
   ```
	python3 producer.py
	```

6. Then create one more window in terminal and run there next command:
   ```
	python3 consumer.py
	```

7. Tap on your web browser link:
   ```
	https://localhost:8080
	```
	You will see the main page of the airflow.

8. Enter username = gpadmin and password = pivotal into the authorization form on the main page of the airflow

9. Add connection to airflow: Go to Admin and click on the button "Connection". Write connection id = postgres_default, login = test, password = test, host = db, port = 5432 and click "Save"!

10. Activate Dag "prepare_data" (move the toggle switch "prepare_data" to the on position)

11. Run Dag "prepare_data"

11. Success!)


P.S. If you want to assure that everything works, you can go to SQL app (whatever you prefer to use), then connect to the table "prepared_data" and run command "select count(*) from prepared_data" twice. If returned numbers will be different, it means that scripts works and data is inserted into the database

P.P.S. If you want to find out about structure of this project and so on, we highly recommend you to visit file "presentation_big_data.pptx", where you can find a lot of interesting information (slide № 3 tells about the architecture)
