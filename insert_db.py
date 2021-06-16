import sqlite3

conn = sqlite3.connect('speedtest-collector.db')
cursor = conn.cursor()
cursor.execute("""
  INSERT INTO collector (data_hora, server_url, server_host, server_latitude, server_longitude, 
                         download, upload, ping, bytes_enviados, bytes_recebidos, 
                         evidencia, pais, sponsor, latencia, cliente_ip,
                         cliente_latitude, cliente_longitude, provedor)
                         
  VALUES ('2021-06-16T12:11:02.199677Z', 'http://imudspeedtest.velocidadenet.com.br:8080/speedtest/upload.php', 'imudspeedtest.velocidadenet.com.br:8080', -23.6270, -46.6350, 
          22670107.88667441, 24387936.09454667, 10.131, 30605312, 28610032, 
          'http://www.speedtest.net/result/11585689623.png', 'Brazil', 'IMUNIDADE DIGITAL', 10.131, '177.38.46.24', -23.6283, -46.6409, 'Space Network Informatica Ltda');
  """)
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()

