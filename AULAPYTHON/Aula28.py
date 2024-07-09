from faker import Faker
import pandas as pd
import json
Faker = Faker('pt_BR')

def create_persona() -> dict:
    data = {
        'username': Faker.name(),
        'email': Faker.email(),
        'password': Faker.password(),
        'phone': Faker.phone_number(),
        'address': Faker.address(),
        'cpf': Faker.cpf()
    }
    return data
 
persona = create_persona()
print(persona)

