def main():
    print("Bem-vindo ao sistema de gerenciamento de eventos!")

    participantes = [{
        "id": 1,
        "nome": "Ana Clara",
        "email": "ana@gmail.com"
    }, {
        "id": 2,
        "nome": "Bruno Silva",
        "email": "bruno@gmail.com"
    }, {
        "id": 3,
        "nome": "Carlos Souza",
        "email": "carlos.souza@gmail.com"
    }, {
        "id": 4,
        "nome": "Diana Costa",
        "email": "diana@gmail.com"
    }, {
        "id": 5,
        "nome": "Eduardo Lima",
        "email": "eduardo@gmail.com"
    }]

    eventos = [{
        "id": 1,
        "nome": "Conferência de Tecnologia",
        "data": "2023-10-15",
        "local": "Centro de Convenções",
        "participantes": [1, 2, 3]
    }, {
        "id": 2,
        "nome": "Workshop de Programação",
        "data": "2023-11-20",
        "local": "Auditório Municipal",
        "participantes": [2, 4, 5]
    }, {
        "id": 3,
        "nome": "Fórum de Inovação",
        "data": "2023-12-05",
        "local": "Teatro Municipal",
        "participantes": [1, 3, 5]
    }]

    def listar_eventos(eventos):
        print("\nEventos disponíveis:")
        for evento in eventos:
            print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']}")

    def listar_participantes_do_evento(eventos, participantes, id_evento):
        for evento in eventos:
            if evento['id'] == id_evento:
                print(evento['participantes'])
                for participante in participantes:
                    for i in evento['participantes']:
                        if participante['id'] == i:
                            print(participante['nome'])

    listar_eventos(eventos)
    listar_participantes_do_evento(eventos, participantes, 3)


if __name__ == "__main__":
    main()
