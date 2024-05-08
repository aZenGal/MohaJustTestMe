#!/usr/bin/env python3

import conf as conf

def bruteforce():
    print("==============================================")
    print(conf.colored(conf.text2art("Bruteforce", "small"), "cyan"))
    print("==============================================")

    target_host = input(conf.colored("\nEntrez l'adresse IP de la cible: ", "green", attrs=["bold"]))
    target_port = int(input(conf.colored("Entrez le port: ", "green", attrs=["bold"])))
    user = input(conf.colored("Login : ", "green", attrs=["bold"]))

    # Mapping des ports à des services pour définir automatiquement le service cible dans Hydra
    ports_to_services = {
        21: 'ftp',  # FTP
        22: 'ssh',  # SSH
        23: 'telnet'  # Telnet
    }

    output = conf.dir_output(bruteforce, "reports/hydra/", target_host)
    conf.create_dir(output)

    service = ports_to_services.get(target_port, 'unknown')
    if service == 'unknown':
        print(f"Port {target_port} non pris en charge pour le bruteforce par ce script.")
        return

    # Lancement de la commande hydra adaptée au service détecté
    command = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {service}://{target_host} -o report/{target_host}/hydra.txt"
    print(command)
    print(f"Lancement du bruteforce sur {target_host} port {target_port} pour {service}...")
    conf.os.system(command)
    print("Bruteforce terminé pour le port ", target_port)

def read_nmap_result():
    print("==============================================")
    print(conf.colored(conf.text2art("Lire un résultat Nmap", "small"), "cyan"))
    print("==============================================")

    result_path = input(conf.colored("\nEntrez le chemin vers le fichier de résultat Nmap: ", "green", attrs=["bold"]))
    user = input(conf.colored("Login : ", "green", attrs=["bold"]))
    try:
        with open(result_path, 'r') as file:
            lines = file.readlines()
            ports_to_bruteforce = {
                21: 'ftp',  # FTP
                22: 'ssh',  # SSH
                23: 'telnet'  # Telnet
            }
            ip_address = None
            
            output = conf.dir_output(read_nmap_result, "reports/hydra/", ip_address)
            conf.create_dir(output)
            
            # Extraction de l'adresse IP à partir de la ligne "Nmap scan report for"
            for line in lines:
                if "Nmap scan report for" in line:
                    ip_address = line.split()[-1]
                    break

            if not ip_address:
                print("Adresse IP non trouvée dans le fichier de résultat Nmap.")
                return

            found_ports = []
            for line in lines:
                if '/tcp' in line and 'open' in line:
                    port = int(line.split('/')[0].strip())
                    if port in ports_to_bruteforce:
                        found_ports.append(port)
                        service = ports_to_bruteforce[port]
                        print(f"Port {port} ouvert pour {service} sur {ip_address}. Convient à un bruteforce.")
                        # Lancer le bruteforce avec Hydra
                        command = f"hydra -l {user} -P /usr/share/wordlists/rockyou.txt {service}://{ip_address} -o report/{ip_address}/hydra.txt"
                        print(f"Lancement du bruteforce sur {ip_address} port {port} pour {service}...")
                        conf.os.system(command)
                        print(f"Bruteforce terminé pour le port {port} ({service}).")
                        
            if not found_ports:
                print("Aucun port pertinent ouvert trouvé.")

    except FileNotFoundError:
        print("Le fichier de résultats Nmap n'a pas été trouvé à l'emplacement spécifié.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du fichier Nmap: {e}")

    print("______________________________________________________________________")


def menu():
    conf.clear()
    conf.re_open()

def menu_bruteforce():
    while True:
        conf.clear()
        print("================================================")
        print(conf.colored(conf.text2art("Bruteforce Hydra", "small"), "cyan"))
        print("================================================")
        print(conf.colored("1. Entrez l'IP et le port pour Bruteforce", "yellow", attrs=["bold"]))
        print(conf.colored("2. Lire le résultat d'un scan Nmap", "yellow", attrs=["bold"]))
        print(conf.colored("M. Main Menu", "yellow", attrs=["bold"]))
        print("================================================")

        conf.ans = input(conf.colored("\nQue voulez-vous faire ? Saisissez votre choix: ", "green")).upper()
        if conf.ans == "1":
            conf.call_def(bruteforce, 0)
        elif conf.ans == "2":
            conf.call_def(read_nmap_result, 0)
        elif conf.ans == "M":
            conf.call_def(menu, 0)
        else:
            conf.not_valid(menu_bruteforce, 0)

            conf.ans = None