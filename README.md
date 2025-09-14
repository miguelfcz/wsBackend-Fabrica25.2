# wsBackend-Fabrica25.2

🎵 Music Streaming API & Web

Este projeto é uma aplicação web e API REST construída com Django para gerenciar uma coleção de músicas, artistas, álbuns e playlists. Sua principal funcionalidade é a capacidade de, ao cadastrar um novo artista através da API, consumir a API externa do MusicBrainz para popular automaticamente todos os álbuns e músicas daquele artista no banco de dados.

O projeto também conta com uma interface web simples e interativa para visualizar os dados cadastrados.

✨ Funcionalidades Principais

    API REST Completa: Gerenciamento de Artistas e Playlists com operações CRUD (Create, Read, Update, Delete).

    Integração com MusicBrainz: Ao criar um novo artista via API, o sistema busca e cadastra automaticamente seus álbuns e músicas.

    Consulta de Dados: Endpoints ReadOnly para consulta de Álbuns e Músicas.

    Interface Web Dinâmica: Páginas para visualizar artistas e álbuns com um sistema interativo para expandir e ver os conteúdos relacionados (álbuns de um artista, músicas de um álbum).

    Modelos Relacionados: Estrutura de dados bem definida com Artistas, Álbuns, Músicas e Playlists.

🛠️ Tecnologias Utilizadas

    Backend:

        Python

        Django

        Django REST Framework

    Banco de Dados:

        SQLite3 (padrão)

        Psycopg2 (pronto para integração com PostgreSQL)

    Requisições Externas:

        Requests

    Frontend:

        HTML5

        CSS3

        JavaScript (vanilla)

        Django Templates (Jinja)

🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

1. Pré-requisitos

    Python 3.8 ou superior

    Git

2. Clonando o Repositório

Bash

git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

3. Configuração do Ambiente

É altamente recomendado o uso de um ambiente virtual (venv).
Bash

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
