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
