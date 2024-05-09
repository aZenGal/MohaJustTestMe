# 📡 MohaJustTestMe
Outil codé en Python permettant d'automatiser l'exécution des outils suivants : Nmap, Dirb, Nikto, Hydra et LinPEAS et permet aussi d'automatiser la génération de rapports lors d'un test de pénétration.<br/> 
* Effectuer un scan de réseau avec Nmap
* Effectuer un scan de vulnérabilités avec Nikto
* Effectuer une recherche de répertoires avec Dirb
* Effectuer un bruteforce en SSH, Telnet et FTP avec Hydra
* Effectuer un rapport d'élevation de privilège avec LinPEAS
* Générer un dossier avec un rapport de chaque outil
* Automatiser le test de pénétration
------------------------------------
<br/>
<a href="https://ibb.co/HV4JXZ3"><img src="https://i.ibb.co/hy9qC0w/Moha-Just-Test-Me.png" alt="Moha-Just-Test-Me" border="0"></a>
<br />

## Sommaire
    -[Systèmes d'exploitations testés](#systèmes-dexploitations-testés)
    -

# Systèmes d'exploitations testés
- Kali Linux 2024.1

## Current tools
> [!WARNING]
> Certains outils peuvent ne pas fonctionner sur les systèmes Linux autre que Kali Linux 2024.1

| Outil                 | Description                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| Nmap                  | Permet de scanner les ports ouverts et identifier les services hébergés.                                          |
| Nikto                 | Permet de scanner un hôte et d’afficher toutes les failles potentielles.                                          |
| Dirb                  | Permet effectuer un scan de contenu Web.                                                                          |
| Hydra                 | Permet de réaliser des bruteforces.                                                                               |
| LinPEAS               | permet d'analyser un système Linux à la recherche de chemins pour élever les privilèges.                          |

## 🛠 Installation
Le fichier <b>install.sh</b> codé en BASH permet d'installer les différents prérequis.

### Linux & Unix
```
$ git clone https://github.com/aZenGal/MohaJustTestMe.git
$ cd MohaJustTestMe
$ chmod +x ./install.sh && chmod +x MohaJustTestMe.py
$ ./install.sh
$ sudo python3 MohaJustTestMe.py
```
Egalement, les dépendances peuvent être installés manuellement avec `pip install -r requirements.txt`.

# ✨ Plus d'informations
Ce projet est libre et open source, codé (majoritairement) par Mohamed-Ali.

# Merci à
* Trabelsi Mohamed-Ali - Ultra Security Team Leader <br/>
* ChatGPT 4 - Ultra Security Team Helper
