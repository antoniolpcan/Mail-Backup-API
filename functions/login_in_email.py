from .check.__init__ import check_host
from imap_tools import MailBox
from fastapi import HTTPException, Body

def login_email(email:str = Body(...),password:str = Body(...),site:str = Body(...)):
    """
    Realiza o login.
    """
    site = site.strip()
    email = email.strip()
    password = password.strip()
    try:
        server = check_host(site)[0]
        with MailBox(f"{server}").login(email, password,f'INBOX') as mailbox:
            login = "Logado."
            return login
    except BaseException as e:
        print(e)
        raise HTTPException(401,'Login inválido.')
    