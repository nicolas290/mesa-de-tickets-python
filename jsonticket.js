
use('BddTickets');

// Create a new document in the collection.
db.getCollection('GestionTickets').insertOne({
"id":1,
"Ejecutivo":{
"id":"E01",
"Nombre":"Anita Acebedo"
},
"DatosCliente":{
"Nombre":"Juan Bustos",
"NumeroTelefono":12345678-9,
"Correo":"juan@gmail.com"
},
"Tipo de ticket":"Reclamo",
"Criticidad":"Media",
"Detalle servicio":"Servicio de telefonia",
"Detalle del problema":"Cliente con Problemas de señal",
"Fecha  creacion":new Date("2024-05-17T00:00:00Z"),
"Area Derivar":"Quiebres"
});

db.GestionTickets.insertOne({
"id":2,
"Ejecutivo":{
    "id":"E02",
    "Nombre":"Carmen Loyola"
},
"Datos Cliente":{
"Nombre":"Jhon Wick",
"Rut":"18345678-6",
"Numero Telefono":"+561123987",
"Correo":"Jwick@gmail.com"
},
"TipoTicket":"Reclamo",
"Criticidad":"Alta",
"Detalle Servicio":"Servicio Internet",
"Detalle Problema":"Intermitencia en el servicio",
"Fecha Creacion":new Date("2024-05-17T00:00:00Z"),
"Area Derivar":"Conectividad y Redes "
});

db.GestionTickets.insertOne({
    "id":3,
    "Ejecutivo":{
    "Id":"E03",
    "Nombre":"Bastian Rojas"
    },
    "DatosCliente":{
    "Nombre":"Camila Salgado",
    "Rut":"18945678-2",
    "NumeroTelefono":"123456780",
    "Correo":"Camilas@gmail.com"
    },
    "TipoTicket":"Consulta",
    "Criticidad":"Baja",
    "DetalleServicio":"ServicioTelefonia",
    "Detalle Problema":"Cliente consulta por planes moviles",
    "FechaCreacion": new Date("2022-05-16T00:00:00Z"),
    "AreaDerivar":"Planes de Telefonia"
});


