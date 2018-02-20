# Edcamp_camp

Sistema com dados dinâmicos para a criação de campeonatos, edições de campeonato e suas tabelas de classificação.

## Começando a brincadeira
 
Antes de clonar esse repositório, certifique-se de que já tem todos os pré-requisitos descritos abaixo.
Essas instruções te ajudarão a rodar o projeto em sua máquina para desenvolvimento e testes.

### Pré-requisitos

Vamos precisar das seguintes ferramentas:
- Brew;
- PIP;
- Virtualenv (Virtualenvwrapper);
- Python (foi usado o Python 2.7);
- MySQL.


### Instalação

1. Clone o repositório e abra o diretório;
2. Crie uma virtualenv e inicie-a;

### Executando o arquivo pela linha de comando

1. Digite o conteudo abaixo no terminal, isso fará com que sejam instalados os requisitos minimos para rodar o projeto:

```
make setup
```

A saída esperada será algo assim:

```
Successfully installed Django-1.9 mysqlclient-1.3.12
```

2. Depois disso, vamos criar o banco de dados para o projeto:

```
make create-db
```


3. Criando um usuário para o admin:

```
make superuser
```

Escolha um nome de usuário, um e-mail e senha.


4. Agora vamos rodar o projeto no servidor, digitando o seguinte conteudo na linha de comando:

```
make run
```

A saída esperada será algo assim:

```
System check identified no issues (0 silenced).
January 17, 2018 - 11:07:59
Django version 1.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Para ter acesso ao admin, copie e cole http://127.0.0.1:8000/admin na URL. Senão, http://127.0.0.1:8000/
