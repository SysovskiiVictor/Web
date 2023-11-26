import sys
import http.server
import socketserver

standart_port = 8888

if len(sys.argv) > 1:
    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Неверный порт", standart_port)
        port = standart_port
else:
    port = standart_port

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Сервер запущен, порт: {port}")
    httpd.serve_forever()