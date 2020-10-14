# Программа - сервер
import socket
import sys
import json

from helper.variables import (
    ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE,
    TIME, USER, ERROR, DEFAULT_PORT, MAX_PACKAGE_LENGTH, ENCODING
)


class ServerSocket:
    def __init__(self, af_inet, sock_stream):
        self.inet = af_inet
        self.stream = sock_stream

    def create_socket(self):
        return socket.socket(self.inet, self.stream)

    def get_message(self, client):
        """
         Утилита приёма и декодирования сообщения
        принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
        """
        encoded_response = client.recv(MAX_PACKAGE_LENGTH)
        if isinstance(encoded_response, bytes):
            json_response = encoded_response.decode(ENCODING)
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError

    def send_message(self, sock, message):
        # Утилита кодирования и отправки сообщения принимает словарь и отправляет его
        js_message = json.dumps(message)
        encoded_message = js_message.encode(ENCODING)
        sock.send(encoded_message)

    def process_client_message(self, message):
        """
        Обработчик сообщений от клиентов, принимает словарь -
        сообщение от клинта, проверяет корректность,
        возвращает словарь-ответ для клиента
        """
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            return {RESPONSE: 200}
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.1.2
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(
            'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет
    ss = ServerSocket(socket.AF_INET, socket.SOCK_STREAM)
    sock = ss.create_socket()
    sock.bind((listen_address, listen_port))
    # Слушаем порт
    sock.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = sock.accept()
        try:
            message_from_cient = ss.get_message(client)
            print(message_from_cient)
            # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
            response = ss.process_client_message(message_from_cient)
            ss.send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print(f'Принято некорретное сообщение от клиента -> {client_address}')
            client.close()


if __name__ == '__main__':
    main()
