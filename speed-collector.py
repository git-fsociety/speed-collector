import speedtest
import sqlite3

server_collector = speedtest.Speedtest()
server_collector.get_servers(None)
server_collector.get_best_server()
server_collector.download(threads=None)
server_collector.upload(threads=None)
server_collector.results.share()

results_dict = server_collector.results.dict()

p_download = results_dict['download']
p_upload = results_dict['upload']
p_ping = results_dict['ping']
t_timestamp = results_dict['timestamp']
t_bytes_sent = results_dict['bytes_sent']
t_bytes_received = results_dict['bytes_received']
t_share = results_dict['share']


server = results_dict['server']
s_server_url = server['url']
s_server_host = server['host']
s_lat_server = server['lat']
s_lon_server = server['lon']
s_name = server['name']
s_country = server['country']
s_sponsor = server['sponsor']
s_latency = server['latency']


cliente = results_dict['client']
c_ip = cliente['ip']
c_lat_cliente = cliente['lat']
c_lon_cliente = cliente['lon']
c_ips = cliente['isp']

'''
print(results_dict)
print('~=' * 10)
print('Servidor')
print('~=' * 10)
print(f'Download: {p_download}')
print(f'Upload: {p_upload}')
print(f'Ping: {p_ping}')
print(f'Data Hora: {t_timestamp}')
print(f'Bytes enviados: {t_bytes_sent}')
print(f'Bytes recebidos: {t_bytes_received}')
print(f'Evidencia: {t_share}')
print(f'Server_url: {s_server_url}')
print(f'Server_host: {s_server_host}')
print(f'Server lat: {s_lat_server}')
print(f'Server lon: {s_lon_server}')
print(f'Pais: {s_country}')
print(f'Sponsor: {s_sponsor}')
print(f'Latency: {s_latency}')


print('~=' * 10)
print('Cliente')
print('~=' * 10)
print(f'Cliente IP: {c_ip}')
print(f'Cliente lat: {c_lat_cliente}')
print(f'Cliente lon: {c_lon_cliente}')
print(f'Provedor: {c_ips}')
'''

conn = sqlite3.connect('speedtest-collector.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO collector (data_hora, server_url, server_host, server_latitude, server_longitude, 
                         download, upload, ping, bytes_enviados, bytes_recebidos, 
                         evidencia, pais, sponsor, latencia, cliente_ip,
                         cliente_latitude, cliente_longitude, provedor)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", (t_timestamp, s_server_url, s_server_host, s_lat_server, s_lon_server, p_download, p_upload, p_ping, t_bytes_sent, t_bytes_received,
      t_share, s_country, s_sponsor, s_latency, c_ip, c_lat_cliente, c_lon_cliente, c_ips))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()