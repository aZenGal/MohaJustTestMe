# #!/usr/bin/env python3

# import conf as conf

# def Dirb_scan():
#     print("===================================================================")
#     print(conf.colored(conf.text2art("Dirb Scan", "small"), "cyan"))
#     print("===================================================================")

#     dir_host = input(conf.colored("\nEntrez une URL (https://www.ec-council.org): ", "green", attrs=["bold"]))
#     dir_output = input(conf.colored(f"Saisir le dossier de sortie - [defaut: reports/Dirb/{dir_host}/]: ", "green", attrs=["bold"],))

#     conf.not_valid(Dirb_scan, dir_host)
#     dir_output = conf.dir_output(dir_output, "reports/Dirb", dir_host)
#     conf.create_dir(dir_output)

#     conf.os.system(f"dirb {dir_host} /usr/share/wordlists/dirb/common.txt -o {dir_output}/Dirb.txt")

#     print("______________________________________________________________________")

import conf as conf

def Dirb_scan():
    print("===================================================================")
    print(conf.colored(conf.text2art("Dirb Scan", "small"), "cyan"))
    print("===================================================================")

    dir_host = input(conf.colored("\nEntrez une URL (https://www.ec-council.org): ", "green", attrs=["bold"]))
    # Nettoyage de l'URL pour le dossier de sortie
    dir_host_clean = dir_host.replace('https://', '').replace('http://', '')

    default_output_path = f"reports/Dirb/{dir_host_clean}/"
    dir_output = input(conf.colored(f"Saisir le dossier de sortie - [defaut: {default_output_path}]: ", "green", attrs=["bold"]))
    dir_output = dir_output if dir_output else default_output_path

    # Correction de l'appel à dir_output
    conf.create_dir(dir_output)
    dir_output = conf.dir_output(dir_output, dir_host_clean)  # Ajuster selon les paramètres attendus

    conf.os.system(f"dirb {dir_host} /usr/share/wordlists/dirb/common.txt -o {dir_output}/Dirb.txt")

    print("______________________________________________________________________")
