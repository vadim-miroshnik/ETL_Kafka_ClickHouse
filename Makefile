run_click_house :
	docker-compose -f docker-compose.yml -f docker-compose_clickhouse.yml up -d \
		zookeeper_ch \
		clickhouse-node1 \
		clickhouse-node2 \
		clickhouse-node3 \
		clickhouse-node4

run_kafka:
	docker-compose -f docker-compose.yml -f docker-compose_kafka.yml up -d \
		zookeeper \
		broker \
		schema-registry \
		connect \
		control-center \
		ksqldb-server \
		ksqldb-cli \
		ksql-datagen \
		rest-proxy

run_environment: run_click_house run_kafka

down:
	docker-compose -f docker-compose.yml -f docker-compose_kafka.yml -f docker-compose_clickhouse.yml down

logs:
	docker-compose -f docker-compose.yml -f docker-compose_kafka.yml -f docker-compose_clickhouse.yml logs -f

prepare:
	cp .env.example .env