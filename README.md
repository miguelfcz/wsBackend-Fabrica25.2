# 🎵 Music Streaming API & Web

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15-red?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)

Este projeto é uma aplicação web e API REST construída com Django para gerenciar uma coleção de músicas, artistas, álbuns e playlists. Sua principal funcionalidade é a capacidade de, ao cadastrar um novo artista através da API, consumir a API externa do **MusicBrainz** para popular automaticamente todos os álbuns e músicas daquele artista no banco de dados.

O projeto também conta com uma interface web simples e interativa para visualizar os dados cadastrados.

---

## ✨ Funcionalidades Principais

-   **API REST Funcional:** Gerenciamento de Artistas (Adicionar, Ler, Deletar) e Playlists (CRUD completo).
-   **Integração com MusicBrainz:** Ao criar um novo artista via API, o sistema busca e cadastra automaticamente seus álbuns e músicas.
-   **Consulta de Dados:** Endpoints `ReadOnly` para consulta de Álbuns e Músicas.
-   **Interface Web Dinâmica:** Páginas para visualizar artistas e álbuns com um sistema interativo para expandir e ver os conteúdos relacionados.
-   **Modelos Relacionados:** Estrutura de dados bem definida com Artistas, Álbuns, Músicas e Playlists.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:**
    -   Python
    -   Django
    -   Django REST Framework
-   **Banco de Dados:**
    -   SQLite3 (padrão)
    -   Psycopg2 (pronto para integração com PostgreSQL)
-   **Requisições Externas:**
    -   Requests
-   **Frontend:**
    -   HTML5
    -   CSS3
    -   JavaScript (vanilla)
    -   Django Templates (Jinja)

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### 1. Pré-requisitos

-   Python 3.8 ou superior
-   Git

### 2. Clonando o Repositório

```bash
git clone https://github.com/miguelfcz/wsbackend-fabrica25.2.git
cd wsbackend-fabrica25.2
```

### 3. Configuração do Ambiente

É altamente recomendado o uso de um ambiente virtual (venv).

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
.\venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

### 4. Instalação das Dependências

Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt.

```bash
pip install -r requirements.txt
```

### 5. Configuração do Banco de Dados

Navegue até a pasta do projeto e aplique as migrações para criar as tabelas no banco de dados.

```bash
cd project
python manage.py migrate
```

### 6. Crie um Superusuário

Para acessar o painel de administração do Django (/admin), crie um superusuário.

```bash
python manage.py createsuperuser
```
Siga as instruções no terminal para definir um nome de usuário, email e senha.

### 7. Rodando o Servidor

Inicie o servidor de desenvolvimento do Django.

```bash
python manage.py runserver
```

O projeto estará disponível em http://localhost:8000/streaming/.

## 🌐 Endpoints

O projeto expõe dois conjuntos de endpoints: uma API REST para gerenciamento de dados e uma Interface Web para visualização.

### 🤖 API REST

A base da API é http://localhost:8000/. Os endpoints estão registrados no urls.py e sempre começam com **/STREAMING/**

### 🎤Artista

| Método | Endpoint | Ação | Payload (Exemplo) |
| :--- | :--- | :--- | :--- |
| `POST` | `/artista/` | Cria um artista e busca seus dados no MusicBrainz. | `{ "nome": "Coldplay", "pais": "UK" }` |
| `GET` | `/artista/` | Lista todos os artistas. | - |
| `GET` | `/artista/{id}/` | Retorna os detalhes de um artista. | - |
| `DELETE` | `/artista/{id}/` | Deleta um artista. | - |

### 🎶Álbum (Somente Leitura)

| Método | Endpoint | Ação |
| :--- | :--- | :--- |
| `GET` | `/album/` | Lista todos os álbuns. |
| `GET` | `/album/{id}/` | Retorna os detalhes de um álbum. |

### 🎵Música (Somente Leitura)

| Método | Endpoint | Ação |
| :--- | :--- | :--- |
| `GET` | `/musica/` | Lista todas as músicas. |
| `GET` | `/musica/{id}/` | Retorna os detalhes de uma música. |

### 🕺Playlist

| Método | Endpoint | Ação | Payload (Exemplo) |
| :--- | :--- | :--- | :--- |
| `POST` | `/playlist/` | Cria uma nova playlist com músicas. | `{ "nome": "Rock Clássico", "musicas_ids": [1, 5, 12] }` |
| `GET` | `/playlist/` | Lista todas as playlists. | - |
| `GET` | `/playlist/{id}/` | Retorna os detalhes de uma playlist. | - |
| `PUT` | `/playlist/{id}/` | Atualiza o nome e adiciona músicas a uma playlist. | `{ "nome": "Rock BR", "musicas_ids": [2, 3] }` |
| `DELETE` | `/playlist/{id}/` | Deleta uma playlist. | - |

### 🖥️ Interface Web (Templates)

A base da interface web é http://localhost:8000/. Os endpoints estão registrados no urls.py e sempre começam com **/STREAMING/**

| Path | Ação | Descrição |
| :--- | :--- | :--- |
| `/artistas/` | Lista de Artistas | Exibe todos os artistas. Clique na seta para expandir e ver os álbuns. |
| `/albuns/` | Lista de Álbuns | Exibe todos os álbuns. Clique na seta para expandir e ver as músicas. |
| `/musicas/` | Lista de Múscias | Exibe uma lista simples de todas as músicas. |
| `/playlists/` | Lista de Playlists | Exibe uma lista simples de todas as playlists. |
| `/musicas/{id}/` | Detalhes da Música | Mostra os detalhes de uma música específica. |
| `/playlists/{id}/` | Detalhes da Playlist | Mostra as músicas contidas em uma playlist específica. |

Autor: [Miguel Fonsêca]
