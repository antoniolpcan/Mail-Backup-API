from functions.treat_values.__init__ import format_date
from shutil import make_archive
from datetime import datetime

def get_zip(site,email):
    data = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
    tdata = format_date(data)
    make_archive(f'imap/imap_compact/{email}_{tdata}', 'zip', f'imap/Emails/{site}/{email}')
    print(f"Arquivo '{email}_{tdata}.zip' foi retornado.")
    return tdata