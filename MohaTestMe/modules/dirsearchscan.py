#!/usr/bin/env python3

import conf.conf as conf

def dirsearch_scan():
    print(
        "===================================================================")
    print(conf.colored(conf.text2art("Dirsearch Scan", "small"), "cyan"))
    print(
        "===================================================================")

    dir_host = input(conf.colored("\nEntrez une cible: ", "green", attrs=["bold"]))
    dir_output = input(
        conf.colored(
            f"Saisir le dossier de sortie - [defaut: reports/Dirsearch/{dir_host}/]: ",
            "green",
            attrs=["bold"],
        ))

    conf.not_valid(dirsearch_scan, dir_host)
    dir_output = conf.dir_output(dir_output, "reports/Dirsearch", dir_host)
    conf.create_dir(dir_output)

    conf.os.system(
        f"python3 {conf.home}/.local/share/dirsearch/dirsearch.py -u {dir_host} --format plain -o {dir_output}/dirsearch.txt"
    )

    print(
        "______________________________________________________________________"
    )
