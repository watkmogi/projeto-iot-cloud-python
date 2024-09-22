import random
import time
import requests

# Função para simular a leitura de um sensor de temperatura
def ler_temperatura():
    # Gera um valor de temperatura aleatório entre 20 e 30 graus
    return round(random.uniform(20.0, 30.0), 2)

# Função para enviar os dados do sensor para um servidor em nuvem (API)
def enviar_dados_para_cloud(temperatura):
    url = "https://api.exemplo.com/dados"  # Endpoint fictício da API na nuvem
    dados = {
        'sensor': 'sensor_de_temperatura_001',
        'temperatura': temperatura,
        'unidade': 'Celsius'
    }
    
    # Envia os dados usando o método POST
    try:
        resposta = requests.post(url, json=dados)
        if resposta.status_code == 200:
            print(f"Dados enviados com sucesso! Temperatura: {temperatura}°C")
        else:
            print(f"Falha ao enviar dados. Status: {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

# Função principal que simula o dispositivo IoT
def dispositivo_iot():
    while True:
        # Ler a temperatura do sensor
        temperatura = ler_temperatura()
        
        # Exibir a leitura da temperatura
        print(f"Temperatura lida: {temperatura}°C")
        
        # Enviar os dados para a nuvem
        enviar_dados_para_cloud(temperatura)
        
        # Aguardar 5 segundos antes de realizar nova leitura
        time.sleep(5)

# Executar o dispositivo IoT
if __name__ == "__main__":
    dispositivo_iot()
