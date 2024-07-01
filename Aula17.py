def verificar_email(email):
    if '@jogajuntoinstituto.org' in email:
        return True
    else:
        return False

# Solicitar email ao usuário
email_usuario = input("Por favor, insira seu email: ")

# Verificar se o email inserido contém o domínio desejado
if verificar_email(email_usuario):
    print("Email válido para o Instituto Joga Junto.")
else:
    print("Email inválido para o Instituto Joga Junto.")

    # Caso de teste para email válido
#email_valido = "usuario@jogajuntoinstituto.org"
#resultado = verificar_email(email_valido)
#assert resultado == True, f"Falhou: esperava True para '{email_valido}', mas retornou {resultado}"
#print(f"Sucesso: '{email_valido}' é válido para o Instituto Joga Junto.")

    # Caso de teste para email inválido
#email_invalido = "usuario@gmail.com"
#resultado = verificar_email(email_invalido)
#assert resultado == False, f"Falhou: esperava False para '{email_invalido}', mas retornou {resultado}"
#print(f"Sucesso: '{email_invalido}' não é válido para o Instituto Joga Junto.")

