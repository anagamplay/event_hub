# Event Hub

O **Event Hub** é uma aplicação de gerenciamento de eventos desenvolvida em Python, que permite cadastrar, visualizar, atualizar e remover eventos, além de gerenciar participantes. O sistema segue princípios de organização modular e separação de responsabilidades, facilitando a manutenção e expansão do projeto.

---

## Tecnologias

- Python 3.13

---

## Estrutura de Pastas

A estrutura do projeto segue o padrão de separação de camadas, facilitando a compreensão e evolução do sistema:

```
event_hub/
│
├── main.py                 # Ponto de entrada da aplicação
│
├── controllers/            # Camada de controle (lógica de negócio e orquestração)
│   ├── event_controller.py
│   ├── menu_controller.py
│   ├── participant_controller.py
│   └── __init__.py
│
├── core/                   # Núcleo, utilidades e infraestrutura do projeto
│   ├── data/               # Possível armazenamento de dados
│   ├── exceptions/         # Exceções customizadas
│   ├── utils/              # Funções utilitárias
│   ├── validators/         # Validações de dados
│   └── __init__.py
│
├── models/                 # Definição das entidades principais
│   ├── event_model.py
│   ├── participant_model.py
│   └── __init__.py
│
├── services/               # Serviços de lógica de negócio, separados por domínio
│   ├── event/
│   └── participant/
│
├── views/                  # Camada de visualização (interface textual)
│   ├── event_view.py
│   ├── menu_view.py
│   ├── participant_view.py
│   └── __init__.py
│
└── README.md
```

---

## Como foi feito

- O projeto adota o padrão MVC (Model-View-Controller).
- O arquivo `main.py` inicializa a aplicação, apresentando um menu principal ao usuário.
- Os controllers em `controllers/` são responsáveis por receber as interações do usuário, manipular os modelos (armazenados em `models/`) e acionar as views para exibir informações.
- A pasta `core/` centraliza funcionalidades transversais como validações, tratamento de exceções e utilitários.
- Os arquivos em `views/` organizam a exibição das informações para o usuário, com foco em uma interface textual (CLI).
- A pasta `services/` pode conter lógica específica de negócio, isolando regras e operações complexas.

---

## Como usar

1. Clone este repositório:
    ```bash
    git clone https://github.com/anagamplay/event_hub.git
    ```

2. Execute a aplicação:
    ```bash
    python main.py
    ```
