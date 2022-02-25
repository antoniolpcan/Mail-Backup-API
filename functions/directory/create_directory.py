from vars import email_dir
import os

def cria_pasta(site,email,ano,mes):
    """
    Cria pasta para guardar arquivo.
    """
    if not os.path.isdir(f"{email_dir}{site}/{email}/{ano}/{mes}"):
        os.makedirs(f"{email_dir}{site}/{email}/{ano}/{mes}")
