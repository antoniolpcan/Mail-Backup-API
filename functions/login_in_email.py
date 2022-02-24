from .check.__init__ import check_host
from imap_tools import MailBox
from fastapi import HTTPException

def login_email(email,password,site):
    """
    Realiza o login.
    """
    site = site.strip()
    email = email.strip()
    password = password.strip()
    try:
        server = check_host(site)[0]
        with MailBox(f"{server}").login(email, password,f'INBOX') as mailbox:
            login = "logado"
            return login
    except:
        raise HTTPException(401,'Login inválido.')
    