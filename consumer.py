import json
from datetime import datetime
import psycopg2
from confluent_kafka import Consumer

from settings import DSL


def save_msg(gp_con, msg, count):
	data = [value for value in json.loads(msg.value()).values()]

	cur = gp_con.cursor()
	cur.execute('INSERT INTO raw_data (sensor_id, longitude, latitude, controller_id, datetime, temperature) VALUES(%s, %s, %s, %s, %s, %s)', data)
	print('Saved!')

	print(count)
	data_log = datetime.now()
	with open('logs.txt', 'w') as file:
		file.write(str(count) + ' - count of data')


def consume_loop(consumer, topics, gp_con,count):
	try:
		consumer.subscribe(topics)

		while True:
			msg = consumer.poll(timeout=1.0)
			if msg is None: 
				continue
			count = count + 1
			save_msg(gp_con, msg, count)

	finally:	
		consumer.close()


def run_consumer(gp_con,count):
	conf = {
		'bootstrap.servers': "localhost:9092",
        'group.id': "1",
        'auto.offset.reset': 'smallest'
    }
	consumer = Consumer(conf)

	consume_loop(consumer, ['generated-data'], gp_con, count)



def main():
	count = 0
	print(count)
	gp_con = psycopg2.connect(**DSL)
	gp_con.autocommit = True

	query = """CREATE TABLE IF NOT EXISTS raw_data (
	id SERIAL,
	sensor_id BIGINT,
	longitude FLOAT,
	latitude FLOAT,
	controller_id BIGINT,
	datetime TIMESTAMP WITH TIME ZONE,
	temperature INTEGER
);"""
	cur = gp_con.cursor()
	cur.execute(query)


	run_consumer(gp_con, count)


if __name__ == '__main__':
	main()
