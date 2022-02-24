from .check.__init__ import check_files,check_deleted,check_host
from .directory.__init__ import get_zip,cria_pasta
from .treat_values.__init__ import file_name_format
from imap_tools import MailBox
from email import generator
import os

def get_mail(site,email,senha):
    """
    Faz o backup e retorna um arquivo zipado
    """
    n = 0
    
    lista_inbox = check_host(site)[1]
    
    new_emails = []
    new_titles = []
    lista_arq_old = check_files(site,email)[0]
    lista_dir = check_files(site,email)[1]
    server = check_host(site)[0]

    for i in lista_inbox:
        with MailBox(f"{server}").login(email, senha,f'{i}') as mailbox:    
            for msg in mailbox.fetch(mark_seen=False): 
                ano = msg.date.strftime("%Y")
                mes = msg.date.strftime("%m")
                date = f"{msg.date}"
                title = f"{msg.subject}"
                title_file = file_name_format(date,title,n)
                title_file_eml = f"{title_file}.eml"
                new_titles.append(title_file_eml)
                if title_file_eml not in lista_arq_old:
                    new_emails.append(title_file_eml)
                    cria_pasta(site,email,ano,mes)
                    outfile_name = os.path.join(f"imap/Emails/{site}/{email}/{ano}/{mes}/{title_file}.eml")
                    with open(outfile_name, 'w') as outfile:
                        gen = generator.Generator(outfile)
                        gen.flatten(msg.obj)  
            
    check_deleted(lista_arq_old,lista_dir,new_titles,site,email)
    tdata = get_zip(site,email)
    name = f"{email}_{tdata}.zip"
    return name
    
    

                    
    
    
                