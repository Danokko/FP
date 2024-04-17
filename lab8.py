import requests

def perform_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        return None

def process_response(response):
    if response is not None:
        return response.status_code, response.text
    else:
        return None, "Ошибка при выполнении запроса"

def display_result(status_code, response_text):
    print(f"Статус кода: {status_code}")
    print("Ответ сервера:")
    print(response_text)

def monitor_network(url):
    response = perform_request(url)
    status_code, response_text = process_response(response)
    display_result(status_code, response_text)
def main():
    url = input("Введите URL для мониторинга: ")
    monitor_network(url)

if __name__ == "__main__":
    main()
