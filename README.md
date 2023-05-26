# API | EMPRESTIMO BIBLIOTECA

Projeto criado para controle de emprestimo de livro dos usuários na biblioteca.

Equipe desenvolvimento do sistema: GEDAI.

> Esse projeto foi desenvolvido usando Python 3.10, Django 4.2.1 e Django Ninja 0.21.0

Passo a passo para rodar o projeto na sua máquina:

- Primeiramente, você vai precisar criar um ambiente isolado.

- Vamos na sua máquina instalar os gerenciador de ambientes virtuais: `virtualenv` e `virtualenvwrapper`:

Instalação no Linux Ubuntu:

- No terminal, realize as instalações desses pacotes:
  
  ```shell
  $ sudo apt install python3-pip python-dev build-essential
  $ sudo pip3 install virtualenv virtualenvwrapper
  ```

- Edite o arquivo .bashrc caso for o shell bash ou .zshrc caso for zsh
  
  ```shell
  $ sudo gedit ~/.bashrc
  ```
  
  ```shell
  $ sudo gedit ~/.zshrc
  ```

- Agora faça a inserção no final da linha do arquivo os seguintes comandos e depois salve as mudanças:
  
  ```shell
  # virtualenvwrapper
  export VIRTUALENVWRAPPER_PYTHON=$(which python3)
  # Diretório onde os ambientes virtuais serão armazenados
  export WORKON_HOME=$HOME/.virtualenvs
  # Diretório onde ficarão os projetos
  export PROJECT_HOME=$HOME/MyProjects
  # Adicionamos os comandos virtualenvwrapper
  source ~/.local/bin/virtualenvwrapper.sh
  ```

- Aplicar a atualização do arquivo .bashrc ou .zshrc:
  
  ```shell
  source ~/.bashrc
  ```
  
  Se estiver usando o zsh:
  
  ```shell
  source ~/.zshrc
  ```

- Vamos criar o ambiente virtual:
  
  ```shell
  $ mkvirtualenv emprestimo_api -p python3
  ```

O nome da env (por exemplo: nucepe_fuapi) pode ser escolhido outro nome de sua preferência.

- Agora ative sua env:
  
  ```shell
  $ workon emprestimo_api
  ```

- Dentro do seu diretório de desenvolvimento, faça um clone do projeto com o comando abaixo, e logo após acesse o diretório:
  
  ```shell
  $ git clone git@github.com:joiltonrsilva/emprestimo_biblioteca_api.git
  ```

- Vamos instalar as dependências do projeto.
  
  ```shell
  $ pip install -r requirements.txt
  ```

- Finalizada a instalação, basta agora executar as migrações e rodar o servidor para poder acessar a aplicação no navegador.
  
  ```shell
  $ python3 manage.py makemigrations
  $ python3 manage.py migrate
  $ python3 manage.py runserver
  ```

- Por fim, no seu navegador web acesse esse endereço: http://127.0.0.1:8000/api/v1/docs#/

- Para o acesso a área administrativa, acesse esse link: http://127.0.0.1:8000/admin/

- Para instalação no Windows, segue esse tutorial: http://www.rafaelzottesso.com.br/2019/02/instalacao-e-utilizacao-de-ambientes-virtuais-no-windows/


OBS: Ficou pendente criar a DDL do BD; autenticação de Usuários e finalizar o endpoints.