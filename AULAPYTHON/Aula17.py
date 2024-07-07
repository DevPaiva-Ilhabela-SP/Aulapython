def verificar_email(email):
    if '@jogajuntoinstituto.org' in email:
        return True
    else:
        return False


email_usuario = input("Por favor, insira seu email: ")

if verificar_email(email_usuario):
    print("Email válido para o Instituto Joga Junto.")
else:
    print("Email inválido para o Instituto Joga Junto.")


