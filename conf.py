#!/usr/bin/env python3

import os
import socket
import sys

import requests
from art import *
from termcolor import colored

from modules.dirbscan import Dirb_scan
from modules.exit import exit
from modules.fullscan import full_scan
from modules.niktoscan import nikto_scan
from modules.nmapscan import nmap_scan
from modules.bruteforce import menu_bruteforce

ans = True
version = "1.0"
home = os.path.expanduser("~")


def re_open():
    installed = True if os.path.exists("/usr/local/bin/MohaJustTestMe") else False

    if installed:
        os.system("sudo MohaJustTestMe")
        sys.exit()

    else:
        os.system("sudo python3 MohaJustTestMe.py")
        sys.exit(())


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def not_valid(func, var, num=1):
    num = True
    if num == True:
        if len(var) <= 5:
            clear()

            print(
                colored("\nChoix non valide Réessayez\n",
                        "red",
                        attrs=["reverse"]))
            func()
    else:
        clear()

        print(
            colored("\nChoix non valide Réessayez\n", "red",
                    attrs=["reverse"]))
        func()


def dir_output(var, path, url):
    if len(var) == 0:
        var = path + "/" + url
        return var


def call_def(func, num=1):
    if num == True:
        clear()
        ans = True
        while ans:
            func()
    else:
        clear()
        func()


# def ver_check():
#     ver_url = "https://github.com/aZenGal/MohaJustTestMe/blob/main/conf/version.txt"
#     try:
#         ver_rqst = requests.get(ver_url)
#         ver_sc = ver_rqst.status_code
#         if ver_sc == 200:
#             github_ver = ver_rqst.text
#             github_ver = github_ver.strip()
#             if version == github_ver:
#                 print(
#                     colored(
#                         "Votre version de MohaJustTestMe est à jour\n",
#                         "yellow",
#                         attrs=["reverse"],
#                     ))
#             else:
#                 print(
#                     colored(
#                         f"Votre version de MohaJustTestMe est obsolète, nouvelle version disponible: {format(github_ver)} \n",
#                         "red",
#                         attrs=["reverse"],
#                     ))
#         else:
#             print("[ Status : {} ".format(ver_sc) + "]" + "\n")
#     except Exception as e:
#         print("\n" + "[-] Exception : " + str(e))
