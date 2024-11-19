customer = []

  #  "Nome": "",
  #  "Data de nacimento": "",
  #  "CPF/CNPJ": 0,
  #  "Logradouro": "",
    # "Bairro": "",
   # "Sigla do estado" : ""



from InquirerPy import prompt

def create_account():# Função para que seja crido uma conta.
    print("Função para criar conta chamada.")
    collecting_data_costumer()# Sendo chamada.
#Tesk of 
#[]Criar uma constante que recebe os dados de cada usuário(tupla).
#[]Criar um validador número ou string.
#[]Criar um Password.
#[]Valor inicial da conta para cada usuário.
#[]Largura de numeros que CPF/CNPJ pode receber/CPF: 11 Números - CNPJ: 14 Números .


def collecting_data_costumer():# Função para que seja crido uma conta.
    customer_data = {}  # Dicionário para armazenar os dados do cliente

    questions_manual = [ # Perguntas de entrada manual
        {"name": "nome",            "message": "Digite seu nome: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"name": "data_nascimento", "message": "Digite sua data de nascimento: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"name": "cpf_cnpj",        "message": "Digite seu CPF ou CNPJ: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"name": "logradouro",      "message": "Digite seu logradouro: "}, # Nome , Chave, Menssagem referente a pergunta.
        {"name": "bairro",          "message": "Digite seu bairro: "}, # Nome , Chave, Menssagem referente a pergunta.
    ]
    
    for question in questions_manual: # Laço que percorre o questions_manual e sua posição atual.
        reply = input(question["message"]) # Reposta que será recebida pelo suário e a mensagem que será mostrada.
        customer_data[question["name"]] = reply

    # Seleção da sigla do estado usando InquirerPy
    state_question = [
        {
            "type": "list",
            "message": "Digite a sigla referente ao estado onde você vive:",
            "choices": ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"],
            "name": "estado",
        }
    ]

    state_response = prompt(state_question)  # Captura a escolha do estado
    customer_data["estado"] = state_response["estado"]
    
    # Adiciona os dados coletados ao array de clientes
    customer.append(customer_data)
    
    print("\nCliente cadastrado com sucesso!")
    print("Dados do cliente:", customer_data)

    
def enter_account():
    print("Função para entrar na conta chamada.")






questions = [
    {
        "type": "list",  # Tipo de pergunta "list" para exibir opções
        "message": "Crie ou entre em uma conta:",
        "choices": ["Entrar", "Criar conta"],  # Lista de escolhas
        "name": "option",  # Nome da variável que armazenará a resposta
    },
]

response = prompt(questions)  # Retorna um dicionário

# Comparação usando o valor da resposta
if response["option"] == "Entrar":
    enter_account()
elif response["option"] == "Criar conta":
    create_account()