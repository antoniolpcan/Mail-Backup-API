from fastapi import HTTPException

def check_host(site):
    """
    Recebe o nome do site e retorna o server em indice 0, a lista das caixas padrão do email em indice 1 e da caixa backup em indice 2.
    - lista de imaps: https://www.systoolsgroup.com/imap/ (locaweb = imap.email-ssl.com.br)
    """
    
    if site in ["locaweb","webmail","locamail","Locaweb","Webmail","Locamail","LOCAWEB","WEBMAIL","LOCAMAIL"]:
        server = "imap.email-ssl.com.br"
        lista_email = ['INBOX','INBOX.enviadas','INBOX.Mala_Direta','INBOX.lixo']
        caixa_backup = 'INBOX.backup'
    elif site == ["gmail","GMAIL","Gmail"]:
        server = "imap.gmail.com"
        lista_email = ['INBOX','all','trash','junk']
        caixa_backup = 'backup'
    elif site == ["outlook","Outlook","OUTLOOK"]:
        server = "outlook.office365.com"
        lista_email = ['INBOX','sent','deleted','junk']
        caixa_backup = 'backup'
    else:
        raise HTTPException(406,detail = f"Site '{site}' não encontrado.")
    return [server,lista_email,caixa_backup]
