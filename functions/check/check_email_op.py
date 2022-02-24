from fastapi import HTTPException

def check_host(site):
    """
    Recebe o nome do site e retorna o server em indice 0, a lista das caixas padrão do email em indice 1 e da caixa backup em indice 2.
    """
    #lista de imaps: https://www.systoolsgroup.com/imap/

    if site == "locaweb":
        server = "imap.email-ssl.com.br"
        lista_email = ['INBOX','INBOX.enviadas','INBOX.Mala_Direta','INBOX.lixo']
        caixa_backup = 'INBOX.backup'
    elif site == "gmail":
        server = "imap.gmail.com"
        lista_email = ['INBOX','all','trash','junk']
        caixa_backup = 'backup'
    elif site == "outlook":
        server = "outlook.office365.com"
        lista_email = ['INBOX','sent','deleted','junk']
        caixa_backup = 'backup'
    else:
        raise HTTPException(406,detail = "Site não encontrado.")
    return [server,lista_email,caixa_backup]
