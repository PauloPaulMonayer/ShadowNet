# 👁️ ShadowNet - Advanced C2 Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Red%20Team-red?style=for-the-badge)
![Encryption](https://img.shields.io/badge/Encryption-TLS%2FSSL-success?style=for-the-badge)

**ShadowNet** is a powerful Command & Control (C2) framework designed for educational purposes and authorized red-teaming. It features a secure, encrypted communication channel (TLS), a multi-threaded server, and a dynamic payload builder that compiles custom agents on the fly.

---

## 🚀 Key Features

* **🔒 End-to-End Encryption:** Uses TLS (SSL) to encrypt all traffic between the Agent and Server, bypassing standard traffic analysis.
* **🏭 Dynamic Payload Builder:** Automated script to configure and compile `EXE` payloads with custom C2 IP addresses.
* **👻 Stealth Mode:** Agents run silently in the background (no console window) using a custom process handler.
* **🔄 Persistence:** The agent includes auto-reconnection logic to handle network drops and server restarts.
* **🛠️ Remote Shell:** Full command-line access to the target machine.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your attacker machine (Windows/Linux).

### 2. Install Dependencies
Run the following command to install the required libraries:

```bash
pip install pyinstaller pillow pyopenssl
pyinstaller: For compiling the agent into an EXE.

pillow: For generating the custom application icon.

pyopenssl: For generating SSL certificates.

3. Initialize the Environment
Before running the server, you must generate the security certificates and assets. Run these scripts once:

Bash

# Generate the SSL Certificate and Private Key
python generate_cert.py

# Generate the Application Icon
python create_icon.py
You should now see server.crt, server.key, and shadownet.ico in your folder.

💻 Usage Guide
Step 1: Build the Payload 🏭
Create a custom agent executable pointing to your server.

Run the builder:

Bash

python builder.py
Enter your Server IP Address (Your local LAN IP, e.g., 192.168.1.15).

Wait for the compilation to finish.

The output file will be at: dist/ShadowAgent.exe.

Step 2: Start the C2 Server 📡
Start the listener to wait for incoming connections.

Bash

python c2_server.py
The server will start listening on port 5555 (0.0.0.0).

Step 3: Execute on Target 🎯
Transfer ShadowAgent.exe to the target machine (or run it on a second PC for testing).

Execute the file. Note: No window will open (Stealth Mode).

Check your Server terminal. You should see:

[+] Encrypted connection from <TARGET_IP>

Step 4: Control the Target 💀
Once a session is established, you have full shell access. Try these commands:

whoami - Check current user.

systeminfo - Get OS details.

dir - List files.

cd <path> - Change directory.

To close the connection, type exit.

⚠️ Troubleshooting
Connection Failed?

Ensure both machines are on the same network.

Check if Windows Firewall is blocking port 5555 on the server. You may need to create an Inbound Rule to allow TCP port 5555.

"Missing server.crt"?

Make sure you ran generate_cert.py before starting the server.

⚖️ Legal Disclaimer
This tool is for educational purposes and authorized security testing only. Using this tool on networks or devices without explicit permission is illegal. The developer assumes no responsibility for misuse.


---