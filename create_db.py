import sqlite3

# Criando Banco de dados
conn = sqlite3.connect('speedtest-collector.db')
cursor = conn.cursor()

# Criando a tabela (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS "collector" (
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"data_hora"	DATETIME NOT NULL UNIQUE,
	"server_url"	VARCHAR NOT NULL,
	"server_host"	VARCHAR NOT NULL,
	"server_latitude"	FLOAT NOT NULL,
	"server_longitude"	FLOAT NOT NULL,
	"download"	FLOAT NOT NULL,
	"upload"	FLOAT NOT NULL,
	"ping"	FLOAT NOT NULL,
	"bytes_enviados"	FLOAT NOT NULL,
	"bytes_recebidos"	FLOAT NOT NULL,
	"evidencia"	VARCHAR NOT NULL,
	"pais"	VARCHAR NOT NULL,
	"sponsor"	VARCHAR NOT NULL,
	"latencia"	FLOAT NOT NULL,
	"cliente_ip"	VARCHAR NOT NULL,
	"cliente_latitude"	FLOAT NOT NULL,
	"cliente_longitude"	FLOAT NOT NULL,
	"provedor"	VARCHAR NOT NULL
	);
""")
print('Tabela criada com sucesso.')
conn.close()



# conn = sqlite3.connect('speedtest-collector.db')
# cursor = conn.cursor()
# cursor.execute("""
# INSERT INTO bandwidth (serverid, sponsor, servername, times, distance, ping, download, upload)
# VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '98765-4322', 'Porto Alegre', 'RS', '2014-06-09')
# """)
# conn.commit()

# print('Dados inseridos com sucesso.')

# conn.close()
