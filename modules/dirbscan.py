import conf as conf
import requests  # Assurez-vous d'installer ce paquet si nécessaire

def dirb_scan(dir_host=None, dir_output=None):
    print("===================================================================")
    print(conf.colored(conf.text2art("Dirb Enumeration Scan", "small"), "cyan"))
    print("===================================================================")

    if dir_host is None:
        dir_host = input(conf.colored("\nSaisissez une cible IP ou URL:", "green", attrs=["bold"]))
        # Ajouter https si aucune schéma n'est spécifié
        if not (dir_host.startswith('http://') or dir_host.startswith('https://')):
            dir_host = f"https://{dir_host}"

    # Essayer avec HTTPS, puis avec HTTP si HTTPS échoue
    try:
        response = requests.get(dir_host)
        if response.status_code != 200:
            raise Exception("HTTPS failed")
    except:
        print(conf.colored("Échec de HTTPS, essai avec HTTP...", "yellow"))
        if dir_host.startswith('https://'):
            dir_host = 'http://' + dir_host[8:]  # Remplace https par http
        try:
            response = requests.get(dir_host)
            if response.status_code != 200:
                raise Exception("HTTP also failed")
        except:
            print(conf.colored("Échec également avec HTTP.", "red", attrs=["bold"]))
            return  # Sortir de la fonction si les deux échouent

    # Nettoyage de l'URL pour le dossier de sortie
    dir_host_clean = dir_host.replace('https://', '').replace('http://', '').replace('/', '')

    if dir_output is None or dir_output.strip() == '':
        default_output = f"reports/Dirb/{dir_host_clean}/"
        dir_output = input(conf.colored(f"Saisir le dossier de sortie - [défaut: {default_output}]: ", "green", attrs=["bold"]))
        if dir_output.strip() == '':
            dir_output = default_output

    # Création du répertoire s'il n'existe pas
    conf.create_dir(dir_output)

    # Exécution de dirb
    conf.os.system(f"dirb {dir_host} /usr/share/wordlists/dirb/common.txt -o {dir_output}dirb.txt")

    print("______________________________________________________________________")
