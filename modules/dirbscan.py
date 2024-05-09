import conf as conf

def dirb_scan(dir_host=None,dir_output=None):
    print("===================================================================")
    print(conf.colored(conf.text2art("Dirb enumeration Scan", "small"), "cyan"))
    print("===================================================================")

    if dir_host is None:
        dir_host = input(conf.colored("\nSaisissez une cible IP ou URL (https://www.ec-council.org):", "green", attrs=["bold"]))
    # Nettoyage de l'URL pour le dossier de sortie
    dir_host_clean = dir_host.replace('https://', '').replace('http://', '')
    
    dir_output = input(conf.colored(f"Saisir le dossier de sortie - [defaut: reports/Dirb/{dir_host}/]: ","green",attrs=["bold"],))

    conf.not_valid(dirb_scan, dir_host_clean)
    if dir_output is None:
        dir_output = conf.dir_output(dir_output, "reports/Dirb", dir_host_clean)
    conf.create_dir(dir_output)

    conf.os.system(f"dirb {dir_host} /usr/share/wordlists/dirb/common.txt -o {dir_output}/dirb.txt")

    print("______________________________________________________________________")