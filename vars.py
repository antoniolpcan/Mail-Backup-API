router_names = ['/','/backup','/email','/deleted','/delete_backup']
email_dir = "imap/Emails/"
ziped_dir = "imap/imap_compact/"
zip_format = "zip"
mail_file = ".eml"
deleted = '/Deleted'
in_deleted = '/Deleted/'
date_time = '%d-%m-%Y-%H:%M:%S'
year = "%Y"
month = "%m"
day = "%d"

from datetime import date

hoje = date.today()
hoje = str(hoje).split('-')
mes_default = hoje[1]
ano_default  = hoje[0]

