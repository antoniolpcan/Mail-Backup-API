from vars import email_dir
from .check.__init__ import check_host,validate_date
from fastapi import HTTPException,Body
from imap_tools import MailBox,MailMessage
import os 

def send_to_email(email:str = Body(...),senha:str = Body(...),site:str = Body(...),mes:str = Body(...),ano:str = Body(...)):
    """
    Retorna os emails para a pasta "backup" no email.
    """
    server = check_host(site)[0]
    caixa = check_host(site)[2]
    validate_date(mes,ano)
    try:
        with MailBox(f"{server}").login(email, senha) as mailbox:
            if os.path.isdir(f"{email_dir}{site}/{email}/{ano}/{mes}"):
                lista_file = os.listdir(f"{email_dir}{site}/{email}/{ano}/{mes}")
                for i in lista_file:
                    with open(f'{email_dir}{site}/{email}/{ano}/{mes}/{i}', 'rb') as f:
                        msg = MailMessage.from_bytes(f.read())
                    mailbox.append(msg, f'{caixa}')
                return "Seus emails foram restaurados."
            else:
                print(f"Caminho de backup: '{email_dir}{site}/{email}/{ano}/{mes}' não encontrado.")
                return f"Backup não existente em: {mes}/{ano}"
    except BaseException as e:
        print(e)
        print('Erro no login.')
        raise HTTPException(401,f"Falha ao recuperar emails de {mes}/{ano} do email: '{email}' no site {site}. Verifique se o site, seu endereço de email e sua senha estão corretos.")
