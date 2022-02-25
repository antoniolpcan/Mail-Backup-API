import os

def rm_dir(dir):
    for f in os.listdir(f'{dir}'):
        os.remove(os.path.join(f'{dir}', f))
    os.rmdir(f'{dir}')