from functions.treat_values.__init__ import file_name_format
from vars import email_dir,mail_file,year,month
from functions.directory.create_directory import cria_pasta
from functions.check.__init__ import check_host
from fastapi import HTTPException
from imap_tools import MailBox
from email import generator
import os

def bup(site,email,senha,lista_arq_old):
    """
    Realiza backup dos emails.
    """
    
    n = 0
    new_emails = []
    new_titles = []
    server = check_host(site)[0]
    lista_inbox = check_host(site)[1]
    for i in lista_inbox:
        try:
            with MailBox(f"{server}").login(email, senha,f'{i}') as mailbox:    
                for msg in mailbox.fetch(mark_seen=False): 
                    ano = msg.date.strftime(year)
                    mes = msg.date.strftime(month)
                    date = f"{msg.date}"
                    title = f"{msg.subject}"
                    title_file = file_name_format(date,title,n)
                    title_file_eml = f"{title_file}{mail_file}"
                    new_titles.append(title_file_eml)
                    if title_file_eml not in lista_arq_old:
                        new_emails.append(title_file_eml)
                        cria_pasta(site,email,ano,mes)
                        outfile_name = os.path.join(f"{email_dir}{site}/{email}/{ano}/{mes}/{title_file}{mail_file}")
                        with open(outfile_name, 'w') as outfile:
                            gen = generator.Generator(outfile)
                            gen.flatten(msg.obj)  
        except BaseException as e:
            print(e)
            print('Erro no login.')
            raise HTTPException(401,f"Falha ao fazer backup do email: '{email}' no site {site}. Verifique se o site, seu endereço de email e sua senha estão corretos.")
        
    return new_titles