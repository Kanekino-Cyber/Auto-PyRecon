# 🛡️ Auto-PyRecon

A lightweight, multi-threaded network reconnaissance tool written in Python.
Designed to automate the initial phase of a Penetration Test by combining Port Scanning, Service Fingerprinting, and targeted Directory Enumeration.

> **Status:** Active / Educational
> **Author:** Nicolas Faraone

## ⚡ Key Features

* **Multi-Threaded Architecture:** Fast scanning capabilities using native Python threading.
* **Smart Automation:** Automatically triggers directory enumeration (dirbusting) *only* when an open HTTP service is detected, avoiding useless requests on non-web ports.
* **Service Fingerprinting:** Performs Banner Grabbing to identify running service versions.
* **Clean Output:** Uses thread-locking mechanisms to prevent console output scrambling.
* **Protocol Awareness:** Detects connection drops and protocol mismatches (e.g., trying to talk HTTP to an SSH port) to prevent crashes.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kanekino-Cyber/Auto-PyRecon.git
    ```

2.  **Install dependencies:**
    Install the required libraries listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

Run the tool specifying the target IP and the path to your wordlist:

```bash
python scanner.py -u <TARGET_IP> -w <WORDLIST_PATH>
```
## TO-DO LIST
[ ] Add support for HTTPS scanning (SSL/TLS context).

[ ] Implement a progress bar for better visual feedback.

[ ] Add option to save results to a file (JSON/TXT).

[ ] Allow custom port ranges via command line arguments.


## ⚠️ Disclaimer

This tool is developed for educational purposes and authorized security testing only. The author is not responsible for any misuse.
