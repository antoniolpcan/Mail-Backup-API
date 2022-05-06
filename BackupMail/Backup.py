from pydantic import BaseModel
from fastapi import HTTPException
from shutil import make_archive
from datetime import datetime
from imap_tools import MailBox,MailMessage
from email import generator
import unicodedata
import re
import os
import shutil

from vars import *

class BackupMail(BaseModel):
    site: str = "locaweb"
    email: str
    password: str
    mes: str = mes_default
    ano: str = ano_default

    def check_host(self) -> list:
        """
        Recebe o nome do site e retorna o server em indice 0, a lista das caixas padrão do email em indice 1 e da caixa backup em indice 2.
        - lista de imaps: https://www.systoolsgroup.com/imap/ (locaweb = imap.email-ssl.com.br)
        """
        
        if self.site in ["locaweb","webmail","locamail","Locaweb","Webmail","Locamail","LOCAWEB","WEBMAIL","LOCAMAIL"]:
            server = "imap.email-ssl.com.br"
            lista_email = ['INBOX','INBOX.enviadas','INBOX.Mala_Direta','INBOX.lixo']
            caixa_backup = 'INBOX.backup'
        elif self.site == ["gmail","GMAIL","Gmail"]:
            server = "imap.gmail.com"
            lista_email = ['INBOX','all','trash','junk']
            caixa_backup = 'backup'
        elif self.site == ["outlook","Outlook","OUTLOOK"]:
            server = "outlook.office365.com"
            lista_email = ['INBOX','sent','deleted','junk']
            caixa_backup = 'backup'
        else:
            raise HTTPException(406,detail = f"Site '{self.site}' não encontrado.")
        return [server,lista_email,caixa_backup]
        
    def check_files(self) -> list:
        """
        Checa os arquivos das pastas retornando uma lista onde, em índice 0, retorna seus nomes e, em índice 1, seus caminhos.
        """
        lista_arq_old = []
        lista_dir = []
        if os.path.isdir(f"{email_dir}{self.site}/{self.email}{deleted}"):
            for f in os.listdir(f"{email_dir}{self.site}/{self.email}{deleted}"):
                os.remove(os.path.join(f"{email_dir}{self.site}/{self.email}{deleted}", f))
            os.rmdir(f"{email_dir}{self.site}/{self.email}{deleted}")

        if os.path.isdir(f"{email_dir}{self.site}/{self.email}"):
            dir_email = os.listdir(f"{email_dir}{self.site}/{self.email}")
            for anos in dir_email:
                meses = os.listdir(f"{email_dir}{self.site}/{self.email}/{anos}")
                for mes in meses:
                    files = os.listdir(f"{email_dir}{self.site}/{self.email}/{anos}/{mes}")
                    for f in files:
                        lista_arq_old.append(f)
                        lista_dir.append(f"{email_dir}{self.site}/{self.email}/{anos}/{mes}/{f}")
            return [lista_arq_old,lista_dir]
        else:
            print(f"Primeiro backup para o email: '{self.email}'")
            return [lista_arq_old,lista_dir]

    def validate_date(self) -> None:
        """
        Verifica se a data é valida, sendo uma string de 01 (01 a 09 terão zeros à esquerda) a 12.
        """
        if self.mes in ['01','02','03','04','05','06','07','08','09','10','11','12']:
            print(f'O mês {self.mes} é válido.')
        else:
            raise HTTPException(406,detail = f'O mês {self.mes} é inválido')

        if len(self.ano) != 4 or 2000>int(self.ano) or int(self.ano)>2100:
            raise HTTPException(406,detail = f'O ano {self.ano} é inválido')

    def check_deleted(self,list_old: list,lista_dir: list,list_new: list) -> list or str:
        """
        Checa emails que foram deletados da caixa em relação aos armazenados no backup.
        """

        deleted_mails = []

        for i in list_old:
            if i not in list_new:
                deleted_mails.append(i)

        if deleted_mails not in ['',[],['']]:
            os.makedirs(f"{email_dir}{self.site}/{self.email}{deleted}")
            for deleted_file in deleted_mails:
                for dirs in lista_dir:
                    if deleted_file in dirs:
                        shutil.copyfile(f"{dirs}", f"{email_dir}{self.site}/{self.email}{in_deleted}{deleted_file}{mail_file}")
            return deleted_mails
            
        else:
            return "Nenhum email foi deletado."

    def cria_pasta(self,ano: int,mes: int) -> None:
        """
        Cria pasta para guardar arquivo.
        """
        if not os.path.isdir(f"{email_dir}{self.site}/{self.email}/{ano}/{mes}"):
            os.makedirs(f"{email_dir}{self.site}/{self.email}/{ano}/{mes}")

    def remove_dir(self, dir: str) -> None:
        """
        Apaga pasta
        """
        for f in os.listdir(f'{dir}'):
            os.remove(os.path.join(f'{dir}', f))
        os.rmdir(f'{dir}')

    def remove_dir_and_files(self) -> None:
        """
        Apaga pasta com tudo dentro
        """
        try:
            shutil.rmtree(f"imap/Emails/{self.site}/{self.email}")
            return "Backup apagado com sucesso."
        except:
            raise HTTPException(404, "Backup não encontrado.")

    def get_zip(self) -> str:
        """
        Compacta a pasta backup.
        """
        data = datetime.today().strftime(date_time)
        tdata = self.format_date(data)
        
        try:
            self.remove_dir(ziped_dir)
        except:
            print(f"Diretorio '{ziped_dir}' será criado")

        make_archive(f'{ziped_dir}{self.email}_{tdata}', f'{zip_format}', f'{email_dir}{self.site}/{self.email}')
        print(f"Arquivo '{self.email}_{tdata}.{zip_format}' foi retornado.")
        name = f"{self.email}_{tdata}.{zip_format}"
        return name

    def format_date(self,date: datetime) -> str: 
        """
        Formata a data, substituindo espaços, traços e dois pontos por underline('_').
        """
        date = date.replace(' ','_').replace('-','_').replace(':','_')
        return date

    def file_name_format(self,date: datetime,string: str,n: int) -> str:
        """
        Formata o nome do arquivo, retirando caracteres especiais e espaços e inserindo a data.
        """
        date = self.format_date(date)

        if string in ['',None,[]]:
            n = n + 1
            string = f"EmailSemTitulo_{n}_"

        string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', string)
        processamento_2 = unicodedata.normalize("NFD", string_nova)
        processamento_3 = processamento_2.encode("ascii", "ignore")
        processamento_4 = processamento_3.decode("utf-8")
        treat_ch = processamento_4.replace(' ','_')
        treat_ch = f"{treat_ch}_{date}"
        return treat_ch

    def backup_function(self,lista_arq_old: list) -> list:
        """
        Realiza backup dos emails.
        """

        n = 0
        new_emails = []
        new_titles = []
        server = self.check_host()[0]
        lista_inbox = self.check_host()[1]
        for i in lista_inbox:
            try:
                with MailBox(f"{server}").login(self.email, self.password,f'{i}') as mailbox:    
                    for msg in mailbox.fetch(mark_seen=False): 
                        ano = msg.date.strftime(year)
                        mes = msg.date.strftime(month)
                        date = f"{msg.date}"
                        title = f"{msg.subject}"
                        title_file = self.file_name_format(date,title,n)
                        title_file_eml = f"{title_file}{mail_file}"
                        new_titles.append(title_file_eml)
                        if title_file_eml not in lista_arq_old:
                            new_emails.append(title_file_eml)
                            self.cria_pasta(ano,mes)
                            outfile_name = os.path.join(f"{email_dir}{self.site}/{self.email}/{ano}/{mes}/{title_file}{mail_file}")
                            with open(outfile_name, 'w') as outfile:
                                gen = generator.Generator(outfile)
                                gen.flatten(msg.obj)  

            except BaseException as e:
                print(e)
                print('Erro no login.')
                raise HTTPException(401,f"Falha ao fazer backup do email: '{self.email}' no site {self.site}. Verifique se o site, seu endereço de email e sua senha estão corretos.")
            
        return [new_titles,new_emails]

    def get_mail(self) -> dict:
        """
        Faz o backup e retorna um arquivo zipado
        """
        lista_arq_old = self.check_files()[0]
        lista_dir = self.check_files()[1]
        lista_new = self.backup_function(lista_arq_old)
        new_titles = lista_new[0]
        new_mails = lista_new[1]
        deleted = self.check_deleted(lista_arq_old,lista_dir,new_titles)
        #name = get_zip(site,email)
        return {"Email":self.email, "New_mails":new_mails, "Deleted":deleted}

    def send_to_email(self) -> str:
        """
        Retorna os emails para a pasta "backup" no email.
        """
        server = self.check_host()[0]
        caixa = self.check_host()[2]
        self.validate_date()
        try:
            with MailBox(f"{server}").login(self.email, self.password) as mailbox:
                if os.path.isdir(f"{email_dir}{self.site}/{self.email}/{self.ano}/{self.mes}"):
                    lista_file = os.listdir(f"{email_dir}{self.site}/{self.email}/{self.ano}/{self.mes}")
                    for i in lista_file:
                        with open(f'{email_dir}{self.site}/{self.email}/{self.ano}/{self.mes}/{i}', 'rb') as f:
                            msg = MailMessage.from_bytes(f.read())
                        mailbox.append(msg, f'{caixa}')
                    return "Seus emails foram restaurados."
                else:
                    print(f"Caminho de backup: '{email_dir}{self.site}/{self.email}/{self.ano}/{self.mes}' não encontrado.")
                    return f"Backup não existente em: {self.mes}/{self.ano}"

        except BaseException as e:
            print(e)
            print('Erro no login.')
            raise HTTPException(401,f"Falha ao recuperar emails de {self.mes}/{self.ano} do email: '{self.email}' no site {self.site}. Verifique se o site, seu endereço de email e sua senha estão corretos.")

    def login_email(self) -> str:
        """
        Realiza o login.
        """
        site = self.site.strip()
        email = self.email.strip()
        password = self.password.strip()
        try:
            server = self.check_host()[0]
            with MailBox(f"{server}").login(email, password,f'INBOX') as mailbox:
                login = "Logado."
                return login
        except BaseException as e:
            print(e)
            raise HTTPException(401,'Login inválido.')
    
    def send_deleted_to_email(self) -> str:
        server = self.check_host()[0]
        caixa = self.check_host()[2]
        self.validate_date()
        try:
            with MailBox(f"{server}").login(self.email, self.password) as mailbox:
                if os.path.isdir(f"{email_dir}{self.site}/{self.email}{deleted}"):
                    lista_file = os.listdir(f"{email_dir}{self.site}/{self.email}{deleted}")
                    for i in lista_file:
                        with open(f'{email_dir}{self.site}/{self.email}{deleted}/{i}', 'rb') as f:
                            msg = MailMessage.from_bytes(f.read())
                        mailbox.append(msg, f'{caixa}')
                    return "Seus emails deletados foram restaurados."
                else:
                    print(f"Caminho de backup: '{email_dir}{self.site}/{self.email}{deleted}' não encontrado.")
                    return (f"Nenhum email deletado foi encontrado.")

        except BaseException as e:
            print(e)
            print('Erro no login.')
            raise HTTPException(401,f"Falha ao recuperar emails deletados do email: '{self.email}' no site {self.site}. Verifique se o site, seu endereço de email e sua senha estão corretos.")
