# EasyCar

## Descrição

Este projeto implementa um sistema para gerenciar aluguéis de carros,
perfis de clientes e operações internas de funcionários. A aplicação será
desenvolvida em Django, utilizando SQLite como banco de dados.

## Tecnologias Utilizadas

* Python
* Django
* SQLite

## Funcionalidades Principais

* Autenticação
* Controle de acesso baseado em grupos (Funcionários e Clientes)
* CRUD para clientes, carros e aluguéis
* Consultas específicas por usuário

## Estrutura do Projeto

* usuários e perfis
* carros
* aluguéis
* autenticação e permissões
* documentação

## Preparando ambiente

### 1. Clonar o repositório

```
git clone https://github.com/IsaacLusca/projeto-integrador-easycar.git
cd projeto-integrador-easycar
```

### 2. Criar e ativar ambiente virtual

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Rodar o servidor

```
python manage.py runserver
```
