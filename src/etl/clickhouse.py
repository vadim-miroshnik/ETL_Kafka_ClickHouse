from clickhouse_driver import Client

client = Client(host='localhost')

# print(client.execute('SHOW DATABASES'))
# [('_temporary_and_external_tables',), ('default',), ('system',)]

# print(client.execute('CREATE DATABASE IF NOT EXISTS example ON CLUSTER company_cluster'))
# [('clickhouse-node1', 9000, 0, '', 3, 0), ('clickhouse-node3', 9000, 0, '', 2, 0), ('clickhouse-node4', 9000, 0, '', 1, 0), ('clickhouse-node2', 9000, 0, '', 0, 0)]

# print(client.execute('CREATE TABLE example.regular_table ON CLUSTER company_cluster (id Int64, x Int32) Engine=MergeTree() ORDER BY id'))
[('clickhouse-node1', 9000, 0, '', 3, 0), ('clickhouse-node3', 9000, 0, '', 2, 0), ('clickhouse-node4', 9000, 0, '', 1, 0), ('clickhouse-node2', 9000, 0, '', 0, 0)]

# client.execute('INSERT INTO example.regular_table (id, x) VALUES (1, 10), (2, 20)')

# print(client.execute('SELECT * FROM example.regular_table'))
# [(1, 10), (2, 20)]

# client.execute('INSERT INTO default.test (id, event_time) VALUES (1, today()), (2, today()), (3, now())')

print(client.execute('SELECT * FROM default.test'))