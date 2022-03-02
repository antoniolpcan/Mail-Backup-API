from vars import deleted,email_dir
import os

def check_files(site,email):
    """
    Checa os arquivos das pastas retornando uma lista onde, em índice 0, retorna seus nomes e, em índice 1, seus caminhos.
    """
    lista_arq_old = []
    lista_dir = []
    if os.path.isdir(f"{email_dir}{site}/{email}{deleted}"):
        for f in os.listdir(f"{email_dir}{site}/{email}{deleted}"):
            os.remove(os.path.join(f"{email_dir}{site}/{email}{deleted}", f))
        os.rmdir(f"{email_dir}{site}/{email}{deleted}")

    if os.path.isdir(f"{email_dir}{site}/{email}"):
        dir_email = os.listdir(f"{email_dir}{site}/{email}")
        for anos in dir_email:
            meses = os.listdir(f"{email_dir}{site}/{email}/{anos}")
            for mes in meses:
                files = os.listdir(f"{email_dir}{site}/{email}/{anos}/{mes}")
                for f in files:
                    lista_arq_old.append(f)
                    lista_dir.append(f"{email_dir}{site}/{email}/{anos}/{mes}/{f}")
        return [lista_arq_old,lista_dir]
    else:
        print(f"Primeiro backup para o email: '{email}'")
        return [lista_arq_old,lista_dir]
