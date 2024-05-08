#!/usr/bin/env python3

import conf as conf

def menu():
    conf.clear()
    conf.re_open()

def nikto_scan():
    print("==============================================")
    print(conf.colored(conf.text2art("Nikto Scan", "small"), "cyan"))
    print("==============================================")

    nikto_host = input(
        conf.colored("\nEntrez la cible: ", "green", attrs=["bold"]))
    nikto_output = input(
        conf.colored(f"Saisir le dossier de sortie - [defaut: reports/Nikto/{nikto_host}/]: ",
            "green", attrs=["bold"],))

    conf.not_valid(nikto_scan, nikto_host)
    nikto_output = conf.dir_output(nikto_output, "reports/Nikto", nikto_host)

    conf.create_dir(nikto_output)

    conf.os.system(f"nikto -h {nikto_host} -output {nikto_output}/nikto.txt")

    print("______________________________________________________________________")
    conf.call_def(menu, 0)