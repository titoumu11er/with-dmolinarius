# coding:utf-8

import http.server
import socketserver
port = int(input("Sur quel numéro de port voulez-vous démmarrer le serveur ? "))
address = ("", port)
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré au port {port}")
httpd.serve_forever()