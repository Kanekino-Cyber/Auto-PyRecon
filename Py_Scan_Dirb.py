import socket
import threading 
import requests
import argparse

# Lock per evitare che i thread scrivano uno sopra l'altro
print_lock = threading.Lock()
results = {}

# Gestione argomenti
parser = argparse.ArgumentParser(description="Tool di enumerazione")
parser.add_argument("-u", "--target", help="IP del target", required=True)
parser.add_argument("-w", "--wordlist", help="File wordlist", required=True)
args = parser.parse_args()


print("-" * 60)
print(f"[*] Target: {args.target}")
print(f"[*] Wordlist: {args.wordlist}")
# TODO: aggiungere la possibilita di scegliere il range porte
print(f"[*] Scanning range: 1-65535") 
print("-" * 60)

def scan_port(port):  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # setto il timeout basso sennò ci mette una vita
    s.settimeout(0.5)
    
    try:
        result = s.connect_ex((args.target, port))
        
        if result == 0:
            with print_lock:
                print(f"[+] Porta {port:<5} APERTA")

            # inizializzo il dizionario per questa porta
            results[port] = {
                "banner": "Nessun banner",
                "urls": []
            }

            dirbusting(args.target, port)
            
            try:
                # provo a prendere il banner
                banner_bytes = s.recv(1024)
                results[port]["banner"] = banner_bytes.decode().strip()
                
                with print_lock:
                    print(f"    [*] Banner Porta {port}: {results[port]['banner']}")
            except:
                # vabbè niente banner
                pass 
                
    except Exception as e:
        pass
    finally:
        s.close()

def dirbusting(target_ip, target_port):
    found_count = 0 
    
    try:
        with open(args.wordlist, "r") as file:
            for linea in file:
                parola = linea.strip()
                if not parola: continue 
                
                url = f"http://{target_ip}:{target_port}/{parola}"
                
                try:            
                    response = requests.get(url, timeout=3)
                    if response.status_code != 404:
                        results[target_port]["urls"].append(url)
        
                        found_count += 1 
                        
                        with print_lock:
                            print(f"    [>] Trovato: /{parola:<15} (Status: {response.status_code})")
                
                except requests.exceptions.RequestException:
                    break 
    except FileNotFoundError:
        with print_lock:
            print(f"[!] Errore: File wordlist non trovato.")

# avvio i thread
threads = []
# range completo
for port in range(1, 65535):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("-" * 60)
print("[*] Scansione completata.")