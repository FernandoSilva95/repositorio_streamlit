## Portfólio com Streamlit

Este projeto consiste na criação de uma página de portfólio utilizando Streamlit, um framework Python para desenvolvimento de aplicações web de forma simples e eficiente.

# Descrição do Projeto

O portfólio criado permite a navegação entre diferentes seções como: Início, Projetos, Dashboards e Contato. A estrutura foi desenvolvida com modularização e uso de um ambiente virtual(-m venv) para garantir a compatibilidade das dependências, sem trazer conflitos com os pacotes já instalados anteriormente no vscode.

# Tecnologias e Ferramentas Utilizadas

- Python

- Streamlit

- Virtual Studio Code

# Estrutura do Projeto

1. Configuração do Ambiente Virtual

- Criado um ambiente virtual venv para isolar as dependências (-m venv venv) e acessando (venv\Scripts\Activate)
  
- Instalando as bibliotecas a serem utilizadas (pip install streamlit)

2. Criação da Tela Inicial

- Desenvolvida uma página de boas-vindas (home.py) com título e descrição do portfólio.

- Implementação da Navegação

3. Criados arquivos individuais para cada página: projetos.py, videos.py, dashboards.py e contato.py.

- Utilizado importlib para carregar dinamicamente os módulos.

- Implementada a função show_page para exibição das páginas e tratamento de erros caso a página não seja encontrada.

- Criação da Sidebar para Navegação

- Adicionada uma sidebar no main.py contendo um selectbox para permitir a escolha das páginas de forma intuitiva.

4. Desenvolvimento do Conteúdo de cada página e vinculando a cada link que desejar.

5. Implementado o conteúdo individual para cada página do portfólio.

6.  Enviando projeto para o git e conectando com a página do Streamlit, ativando a página na web.
