from pymongo import MongoClient

from prettytable import PrettyTable
# Función para conectar a la base de datos MongoDB local
def conectar_db():
    mongo_url = 'mongodb://localhost:27017/'
    # Establecer la conexión
    client = MongoClient(mongo_url)
    Bddtickets = client['BddTickets']
    return Bddtickets['GestionTickets']

def ingresar_ticket():
    tickets = conectar_db()

    ticket = {}
    ticket['UsuarioCreador'] = input("Ingrese su nombre (Usuario que crea el ticket): ")
    ticket['Nombre'] = input("Ingrese el nombre del solicitante: ")
    ticket['RUT'] = input("Ingrese el RUT del solicitante: ")
    ticket['Teléfono'] = input("Ingrese el teléfono del solicitante: ")
    ticket['Correo'] = input("Ingrese el correo electrónico del solicitante: ")

    print("\nTipo de Ticket:")
    print("1. Felicitación")
    print("2. Consulta")
    print("3. Reclamo")
    print("4. Problema")
    tipo_ticket = input("Seleccione el tipo de ticket (1-4): ")
    tipos = {'1': 'Felicitación', '2': 'Consulta', '3': 'Reclamo', '4': 'Problema'}
    ticket['Tipo de Ticket'] = tipos.get(tipo_ticket, "Desconocido")

    ticket['Criticidad'] = input("Ingrese la criticidad (baja, media, alta): ")
    ticket['Detalles del Servicio'] = input("Ingrese los detalles del servicio: ")
    ticket['Detalles del Problema'] = input("Ingrese los detalles del problema: ")

    derivar = input("¿Desea derivar el ticket a otra área? (s/n): ")
    if derivar.lower() == 's':
        ticket['Área para Derivar'] = input("Ingrese el área para derivar: ")
    else:
        ticket['Área para Derivar'] = "No aplica"

    ticket['EjecutivoAsignado'] = input("Ingrese el nombre del ejecutivo asignado: ")

    print("\nEstado de Resolución:")
    print("1. Abierto")
    print("2. En Progreso")
    print("3. Cerrado")
    estado_resolucion = input("Seleccione el estado de resolución (1-3): ")
    estados = {'1': 'Abierto', '2': 'En Progreso', '3': 'Cerrado'}
    ticket['EstadoResolucion'] = estados.get(estado_resolucion, "Desconocido")

    if ticket['EstadoResolucion'] == 'Cerrado':
        ticket['UsuarioCerrador'] = input("Ingrese el nombre del usuario que cerró el ticket: ")
    else:
        ticket['UsuarioCerrador'] = "N/A"

    # Insertar el ticket en la colección de MongoDB
    tickets.insert_one(ticket)
    print("\nTicket ingresado con éxito:")
    for clave, valor in ticket.items():
        print(f"{clave}: {valor}")

def mostrar_tickets():
    tickets = conectar_db()
    print("\nTickets almacenados en la base de datos:\n")
    for ticket in tickets.find():
        for clave, valor in ticket.items():
            print(f"{clave}: {valor}")
        print("-" * 20)

def filtrar_tickets():
    tickets = conectar_db()
    print("\nCriterios de filtrado:")
    print("1. Fecha Específica")
    print("2. Criticidad")
    print("3. Tipo de Ticket")
    print("4. Ejecutivo que Abre el Ticket")
    print("5. Ejecutivo que Cierra el Ticket")
    print("6. Área")
    criterio = input("Seleccione un criterio de filtrado (1-6): ")

    filtro = {}
    if criterio == '1':
        fecha = input("Ingrese la fecha específica (formato YYYY-MM-DD): ")
        filtro['Fecha'] = fecha
    elif criterio == '2':
        criticidad = input("Ingrese la criticidad (baja, media, alta): ")
        filtro['Criticidad'] = criticidad
    elif criterio == '3':
        print("\nTipo de Ticket:")
        print("1. Felicitación")
        print("2. Consulta")
        print("3. Reclamo")
        print("4. Problema")
        tipo_ticket = input("Seleccione el tipo de ticket (1-4): ")
        tipos = {'1': 'Felicitación', '2': 'Consulta', '3': 'Reclamo', '4': 'Problema'}
        filtro['Tipo de Ticket'] = tipos.get(tipo_ticket, "Desconocido")
    elif criterio == '4':
        usuario_creador = input("Ingrese el nombre del usuario que crea el ticket: ")
        filtro['UsuarioCreador'] = usuario_creador
    elif criterio == '5':
        usuario_cerrador = input("Ingrese el nombre del usuario que cierra el ticket: ")
        filtro['UsuarioCerrador'] = usuario_cerrador
    elif criterio == '6':
        area = input("Ingrese el área para derivar: ")
        filtro['Área para Derivar'] = area

    print("\nTickets que cumplen con el criterio de filtrado:\n")
    for ticket in tickets.find(filtro):
        for clave, valor in ticket.items():
            print(f"{clave}: {valor}")
        print("-" * 20)

def mostrar_menu():
    print("Menú de Ingreso de Ticket")
    print("1. Ingresar Ticket")
    print("2. Mostrar Tickets")
    print("3. Filtrar Tickets")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ingresar_ticket()
        elif opcion == '2':
            mostrar_tickets()
        elif opcion == '3':
            filtrar_tickets()
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
