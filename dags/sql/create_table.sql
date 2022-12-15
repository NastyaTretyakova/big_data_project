CREATE TABLE IF NOT EXISTS prepared_data (
	id SERIAL,
	sensor_id BIGINT,
	longitude FLOAT,
	latitude FLOAT,
	controller_id BIGINT,
	datetime TIMESTAMP WITH TIME ZONE,
	temperature INTEGER
);