# 👁️ ShadowNet - Advanced C2 Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Security-Red%20Team-red?style=for-the-badge)
![Encryption](https://img.shields.io/badge/Encryption-TLS%2FSSL-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Educational-yellow?style=for-the-badge)

**ShadowNet** is a powerful, multi-threaded Command & Control (C2) framework designed for educational purposes and authorized red-teaming simulations. It features a secure, encrypted communication channel (TLS), a robust server capable of handling multiple connections, and a dynamic payload builder that compiles custom agents on the fly.

This project demonstrates advanced concepts in **Network Programming**, **Cryptography**, **Process Injection**, and **Software Architecture**.

---

## 🚀 Key Features

* **🔒 End-to-End Encryption:** Uses TLS (SSL) to encrypt all traffic between the Agent and Server, effectively bypassing standard traffic analysis (Sniffing).
* **🏭 Dynamic Payload Builder:** An automated Python script that configures the agent with a specific IP/Port and compiles it into a standalone `.exe` using PyInstaller.
* **👻 Stealth Mode:** Agents run silently in the background (headless mode) using custom process handling to hide the console window.
* **🔄 Persistence & Resilience:** The agent includes auto-reconnection logic to handle network drops and server restarts automatically.
* **🛠️ Remote Shell:** Full command-line access to the target machine via a reverse shell interface.
* **🎨 Custom Assets:** Includes scripts to generate self-signed certificates and custom application icons dynamically.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `c2_server.py` | The central C2 server (listener). Handles multiple threaded connections and commands. |
| `builder.py` | The "Factory". Configures `agent.py` and compiles it into an executable. |
| `agent.py` | The client-side payload template. Runs on the target machine. |
| `generate_cert.py` | Generates SSL certificates (`server.crt`, `server.key`) for encryption. |
| `create_icon.py` | Generates a custom `.ico` file for the payload to look legitimate. |

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your attacker machine (Windows/Linux).

### 2. Install Dependencies
Run the following command to install the required libraries:

```bash
pip install pyinstaller pillow pyopenssl

```

| Library | Purpose |
| --- | --- |
| `pyinstaller` | Compiles the agent into a standalone EXE |
| `pillow` | Generates the custom application icon |
| `pyopenssl` | Generates SSL certificates for encryption |

### 3. Initialize the Environment

Before running the server, generate the security certificates and assets. Run these scripts once:

```bash
# Generate the SSL Certificate and Private Key
python generate_cert.py

# Generate the Application Icon
python create_icon.py

```

> **Success:** You should now see `server.crt`, `server.key`, and `shadownet.ico` in your folder.

---

## 💻 Usage Guide

### Step 1: Build the Payload 🏭

Create a custom agent executable pointing to your server.

1. Run the builder:
```bash
python builder.py

```


2. Enter your **Server IP Address** (Your local LAN IP, e.g., `192.168.1.15`).
3. Wait for the compilation to finish.
4. **Output:** The file will be saved at `dist/ShadowAgent.exe`.

### Step 2: Start the C2 Server 📡

Start the listener to wait for incoming connections.

```bash
python c2_server.py

```

*The server will start listening on port `5555` (0.0.0.0).*

### Step 3: Execute on Target 🎯

1. Transfer `ShadowAgent.exe` to the target machine (or run it on a second PC for testing).
2. Execute the file.
> **Note:** No window will open (**Stealth Mode**).


3. Check your Server terminal. You should see:
```text
[+] Encrypted connection from <TARGET_IP>

```



### Step 4: Control the Target 💀

Once a session is established, you have full shell access. Try these commands:

* `whoami` - Check current user.
* `systeminfo` - Get OS details.
* `dir` - List files.
* `cd <path>` - Change directory.
* `exit` - Close the connection.

---

## ⚠️ Troubleshooting

**Connection Failed?**

* Ensure both machines are on the same network (LAN).
* Check if **Windows Firewall** is blocking port 5555 on the server. You may need to create an Inbound Rule to allow TCP port 5555.

**"Missing server.crt"?**

* Make sure you ran `generate_cert.py` before starting the server.

**Agent crashes immediately?**

* Ensure you built the payload using `builder.py` and provided a valid IP address.

---

## ⚖️ Legal Disclaimer

> **Warning:** This tool is developed for **educational purposes and authorized security assessments only**.
> Using this tool on networks, computers, or devices without explicit permission is illegal and unethical. The developer assumes no responsibility for any misuse of this software.

```

```
