import requests
import json



dados_usuario = {
    "username":"Rodrigo Paiva",
    "email":"rodrigo_paiva3@example.com",
    "password":"12345678",
    "phone":"12345678905",
    "address":"358 Dom Henrique,Ilhabela, Brasil",
    "cpf":"123.456.789-90"
}
criar_usuario= requests.post("https://desafiopython.jogajuntoinstituto.org/api/users/",json=dados_usuario)






