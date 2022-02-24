import os

def cria_pasta(site,email,ano,mes):
    """
    Cria pasta para guardar arquivo.
    """
    if not os.path.isdir(f"imap/Emails/{site}/{email}/{ano}/{mes}"):
        os.makedirs(f"imap/Emails/{site}/{email}/{ano}/{mes}")
