# Bookstore API

API REST desenvolvida com Django Rest Framework para gerenciamento de uma livraria.

## Sobre o Projeto

Este projeto é uma API REST para um sistema de livraria, permitindo o gerenciamento de produtos (livros), categorias e pedidos.

## Requisitos

- Python 3.12+
- Poetry (gerenciador de dependências)

## Configuração do Ambiente

1. **Instalar o Python 3.12+**
   - Baixe e instale o Python 3.12 ou superior do [site oficial](https://www.python.org/downloads/)
   - Verifique a instalação:
     ```powershell
     python --version
     ```

2. **Instalar o Poetry**
   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
   ```

3. **Configurar o Poetry no PATH**
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\[SEU_USUARIO]\AppData\Roaming\Python\Scripts", "User")
   ```
   - Substitua [SEU_USUARIO] pelo seu nome de usuário do Windows
   - Feche e reabra o terminal após este comando

## Clonando e Configurando o Projeto

1. **Clonar o repositório**
   ```powershell
   git clone [URL_DO_REPOSITÓRIO]
   cd Django-Rest-Framework
   ```

2. **Instalar dependências**
   ```powershell
   poetry install
   ```

3. **Ativar o ambiente virtual**
   ```powershell
   poetry shell
   ```

4. **Aplicar as migrações**
   ```powershell
   python manage.py migrate
   ```

5. **Criar superusuário (opcional)**
   ```powershell
   python manage.py createsuperuser
   ```

## Executando o Projeto

1. **Iniciar o servidor de desenvolvimento**
   ```powershell
   python manage.py runserver
   ```
   O servidor estará disponível em `http://127.0.0.1:8000/`

## Estrutura do Projeto

O projeto está organizado em duas principais apps:

- `product/`: Gerenciamento de produtos e categorias
- `order/`: Gerenciamento de pedidos

## Endpoints da API

- `/admin/`: Interface administrativa do Django
- `/api/`: Endpoints da API REST (documentação em desenvolvimento)

## Desenvolvimento

Para continuar o desenvolvimento, certifique-se de:

1. Sempre ativar o ambiente virtual com `poetry shell`
2. Aplicar novas migrações após alterações nos modelos:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Manter o `requirements.txt` atualizado (opcional, já que usamos Poetry):
   ```powershell
   pip freeze > requirements.txt
   ```
