from fastapi import APIRouter

router_imap = APIRouter()


#descriptions

backup_description = """

# Backup

Rota de backup, onde serão passados os parâmetros:
<font size="2">
- **site**: nome da plataforma de email desejada, de preferência a locaweb, onde a API terá melhor funcionalidade.
- **email**: email da conta que deseja fazer backup
- **password**: senha da conta que deseja fazer backup
<br>(existem os parâmetros ano e mes, mas ambos são atributos da classe para serem utilizados na rota de recuperação dos emails, sendo 
completamente dispensáveis na rota de backup.)
</font>

"""

login_description = """

# Login

Rota de login, onde serão passados os parâmetros:
<font size="2">
- **site**: nome da plataforma de email desejada, de preferência a locaweb, onde a API terá melhor funcionalidade.
- **email**: email da conta que deseja logar
- **password**: senha da conta que deseja logar
<br>(existem os parâmetros ano e mes, mas ambos são atributos da classe para serem utilizados na rota de recuperação dos emails, sendo 
completamente dispensáveis na rota de backup.)
</font>

# Utilidade 

Reaproveitamento da função de login da biblioteca do imap, sendo bem utilizado para consumo da validação do login.

"""

to_email_description = """

# Restauração

Rota de restauração, onde serão passados os parâmetros:

<font size="2">
- **site**: nome da plataforma de email desejada, de preferência a locaweb, onde a API terá melhor funcionalidade.
- **email**: email da conta que deseja restaurar backup
- **password**: senha da conta que deseja restaurar backup
- **mes**: mês em que os emails desejados foram enviados
- **ano**: ano em que os emails desejados foram enviados
</font>

# Necessário

É necessária a existência da pasta "backup" nas pastas dentro do email para que a API tenha um lugar para retornar.

"""

deleted_description = """

# Restauração de deletados

Rota de restauração de emails deletados, onde serão passados os parâmetros:

<font size="2">
- **site**: nome da plataforma de email desejada, de preferência a locaweb, onde a API terá melhor funcionalidade.
- **email**: email da conta que deseja restaurar os emails
- **password**: senha da conta que deseja restaurar os emails
<br>(existem os parâmetros ano e mes, mas ambos são atributos da classe para serem utilizados na rota de recuperação dos emails, sendo 
completamente dispensáveis na rota de backup.)
</font>

# Necessário

É necessária a existência da pasta "backup" nas pastas dentro do email para que a API tenha um lugar para retornar.

"""

delete_description = """

# Deletar Backup

Deleta o backup do servidor.

<font size="2">
- **site**: nome da plataforma de email desejada, de preferência a locaweb, onde a API terá melhor funcionalidade.
- **email**: email da conta que deseja deletar o backup
- **password**: senha da conta que deseja deletar o backup
<br>(existem os parâmetros ano e mes, mas ambos são atributos da classe para serem utilizados na rota de recuperação dos emails, sendo 
completamente dispensáveis na rota de backup.)
</font>

# Necessário

É necessária a existência da pasta "backup" nas pastas dentro do email para que a API tenha um lugar para retornar.

"""
