from vars import email_dir
from .check.__init__ import check_host
from fastapi import HTTPException,Body
from imap_tools import MailBox,MailMessage
import os 

def send_to_email(email:str = Body(...),senha:str = Body(...),site:str = Body(...),mes:str = Body(...),ano:str = Body(...)):
    """
    Retorna os emails para a pasta "backup" no email.
    """
    server = check_host(site)[0]
    caixa = check_host(site)[2]
    with MailBox(f"{server}").login(email, senha) as mailbox:
        if os.path.isdir(f"{email_dir}{site}/{email}/{ano}/{mes}"):
            lista_file = os.listdir(f"{email_dir}{site}/{email}/{ano}/{mes}")
            for i in lista_file:
                with open(f'{email_dir}{site}/{email}/{ano}/{mes}/{i}', 'rb') as f:
                    msg = MailMessage.from_bytes(f.read())
                mailbox.append(msg, f'{caixa}')
            return "Seus emails foram restaurados."
        else:
            raise HTTPException(406,detail=f"Backup não existente em: {mes}/{ano}")  
        
