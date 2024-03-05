import logging
import time
import random
import socket

# Configuración básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# Dirección IP y puerto del servidor rsyslog
RSYSLOG_SERVER = '127.0.0.1'
RSYSLOG_PORT = 514

# Función para enviar logs al servidor rsyslog
def send_syslog(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(message.encode(), (RSYSLOG_SERVER, RSYSLOG_PORT))
        logging.info("Log enviado al servidor rsyslog: %s", message)
    except Exception as e:
        logging.error("Error al enviar el log al servidor rsyslog: %s", e)

# Función para simular eventos similares a los de Cisco ASA
def simulate_logs():
    while True:
        timestamp = time.strftime('%b %d %H:%M:%S')
        hostname = "ASA-1"
        severity = random.choice(['%ASA-1-105010:', '%ASA-4-105023:', '%ASA-6-302013:'])
        event_code = random.choice(['302013', '105010', '105023'])
        src_ip = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        dst_ip = f"10.0.{random.randint(1, 255)}.{random.randint(1, 255)}"
        message = random.choice(['Built inbound TCP connection', 'Teardown TCP connection', 'Deny UDP'])
        log_message = f'{timestamp} {hostname} {severity}{event_code}: {message} src={src_ip} dst={dst_ip}'
        
        # Imprimir el mensaje de log antes de enviarlo
        print("Mensaje de log:", log_message)
        
        # Envía el log al servidor rsyslog
        send_syslog(log_message)
        
        time.sleep(random.uniform(0.1, 2))  # Simula intervalos de tiempo aleatorios

if __name__ == "__main__":
    simulate_logs()




