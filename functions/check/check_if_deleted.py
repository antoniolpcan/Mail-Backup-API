from vars import email_dir,deleted,in_deleted,mail_file
import shutil
import os

def check_deleted(list_old,lista_dir,list_new,site,email):
    """
    Checa emails que foram deletados da caixa em relação aos armazenados no backup.
    """

    deleted_mails = []
    for i in list_old:
        if i not in list_new:
            deleted_mails.append(i)

    if deleted_mails not in ['',[],['']]:
        os.makedirs(f"{email_dir}{site}/{email}{deleted}")
        for deleted_file in deleted_mails:
            for dirs in lista_dir:
                if deleted_file in dirs:
                    shutil.copyfile(f"{dirs}", f"{email_dir}{site}/{email}{in_deleted}{deleted_file}{mail_file}")
        