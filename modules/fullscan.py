#!/usr/bin/env python3

import conf as conf


def full_scan():
    print("===========================================================")
    print(conf.colored(conf.text2art("Tous les scans", "small"), "cyan"))
    print("===========================================================")

    full_host = input(conf.colored("\nSaisir l'URL cible (ex: opensource.com) : ", "green", attrs=["bold"]))
    full_host_clean = full_host.replace('https://', '').replace('http://', '')
    full_output = input(conf.colored(f"Saisir le dossier de sortie - [default: reports/All/{full_host_clean}/]: ", "green", attrs=["bold"],))

    conf.not_valid(full_scan, full_host)
    full_output = conf.dir_output(full_output, "reports/All", full_host_clean)

    conf.create_dir(full_output)

    full_ip = conf.socket.gethostbyname(full_host_clean)

    print("___________________________________________________________________________")

    conf.create_dir(full_output)

    # gnome_installed = True if conf.os.path.exists("/usr/bin/gnome-terminal") else False

    # if len(full_host) == 0:
    #     conf.clear()

    #     print("Choix non valide Réessayez")
    #     conf.re_open()

    #     conf.full_host = None
    # elif gnome_installed:
    #     conf.os.system(
    #         f"gnome-terminal -- bash -c 'nmap -A {full_ip} -o \"{full_output}/nmap.txt\" && bash'"
    #     )
    #     conf.clear()

    #     conf.os.system(
    #         f"gnome-terminal -- bash -c 'dirb {full_host} /usr/share/wordlists/dirb/common.txt -o \"{full_output}/dirb.txt\" && bash'"
    #     )
    #     conf.clear()

    #     conf.os.system(
    #         f"gnome-terminal -- bash -c 'nikto -h {full_host} -output \"{full_output}/nikto.txt\" && bash'"
    #     )
    #     conf.clear()

    # else:
    conf.os.system(f"nmap -v -A {full_ip} -o {full_output}/nmap.txt")

    conf.os.system(f"dirb {full_host} /usr/share/wordlists/dirb/common.txt -o \"{full_output}/dirb.txt")

    conf.os.system(f"nikto -h {full_host_clean} -output {full_output}/nikto.txt")
