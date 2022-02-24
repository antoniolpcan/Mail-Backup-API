import os

def check_files(site,email):
    """
    Checa os arquivos das pastas e retorna eles em indice 0 e seus caminhos em indice 1 da lista.
    """
    lista_arq_old = []
    lista_dir = []
    if os.path.isdir(f"imap/Emails/{site}/{email}/Deleted"):
        for f in os.listdir(f"imap/Emails/{site}/{email}/Deleted"):
            os.remove(os.path.join(f"imap/Emails/{site}/{email}/Deleted", f))
        os.rmdir(f"imap/Emails/{site}/{email}/Deleted")

    if os.path.isdir(f"imap/Emails/{site}/{email}"):
        dir_email = os.listdir(f"imap/Emails/{site}/{email}")
        for anos in dir_email:
            meses = os.listdir(f"imap/Emails/{site}/{email}/{anos}")
            for mes in meses:
                files = os.listdir(f"imap/Emails/{site}/{email}/{anos}/{mes}")
                for f in files:
                    lista_arq_old.append(f)
                    lista_dir.append(f"imap/Emails/{site}/{email}/{anos}/{mes}/{f}")
        return [lista_arq_old,lista_dir]
    else:
        print(f"Primeiro backup para o email: '{email}'")
        return [lista_arq_old,lista_dir]
