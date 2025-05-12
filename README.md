
# 🩺 Singularity Health – Backend (Prueba Técnica)

Este proyecto es una API desarrollada en **Django** con **GraphQL (Graphene-Django)** como parte de una prueba técnica para **Singularity Health**. El objetivo principal es evaluar conocimientos en persistencia de datos, relaciones entre modelos, seguridad y estructura backend limpia.

Todo el backend corre en un entorno Dockerizado y expone una **mutación única** para registrar usuarios con su información personal, documento de identidad y datos de contacto, respetando las relaciones de base de datos definidas.

---

## 👨‍💻 Desarrollado por

**Jorge Bairon Bermudez Leon**  
📍 Armenia, Quindío  
📧 j.bayron.b@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/jorge-bairon-bermudez-leon-6242b81b5)

---

## 🛠️ Tecnologías utilizadas

- Python 3.11
- Django 4+
- GraphQL (Graphene-Django + Relay)
- PostgreSQL
- Docker & Docker Compose
- Bcrypt (`make_password`) para hashing seguro de contraseñas

---

## 📂 Estructura del proyecto

```bash
registered_users/
├── fixtures/               # Archivos de datos semilla
│   ├── countries.json
│   └── type_documents.json
├── models.py               # Modelos relacionales
├── admin.py                # Configuración para Django Admin
├── nodes.py                # GraphQL Nodes con filtros
├── mutations.py            # Mutación principal de registro
├── schema.py               # Query + Mutation exportadas
├── filtersets.py           # Filtros para nodos con relay
```

---

## 🔐 Seguridad de contraseñas

Las contraseñas son encriptadas usando `make_password` de Django, que utiliza:
- Algoritmo PBKDF2 + SHA256
- Sal única por usuario
- Compatible con `check_password` para validaciones futuras

Esto asegura que ninguna contraseña se almacene en texto plano.

---

## 🚀 ¿Qué hace esta API?

La API expone una mutación principal llamada `registerUser`, que permite registrar a un usuario con:

- Datos personales (`AppUser`)
- Documento de identidad (`UserDocument`)
- Información de contacto (`ContactInfo`)
- Relaciones con `TypeDocument` y `Country` precargadas

Todo esto en **una sola mutación**, cumpliendo los requisitos de la prueba técnica.

---

## 🐳 Cómo ejecutar el proyecto con Docker

### 1. Clonar el proyecto

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 2. Levantar los contenedores

```bash
docker-compose up --build
```

Esto levantará:

- `web`: contenedor con Django en el puerto `localhost:8000`
- `db`: contenedor PostgreSQL

---

### 3. Entrar al contenedor para ejecutar comandos

```bash
docker exec -it singularity_health_api_web bash
```

Una vez dentro del contenedor, ejecuta lo siguiente:

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

---

### 5. Crear superusuario (solo la primera vez)

```bash
python manage.py createsuperuser
```

Ingresa un `username`, `email` y `password`.  
Esto te permitirá ingresar al panel de administración en:

🔗 http://localhost:8000/admin

---

### 6. Cargar datos iniciales (fixtures)

```bash
python manage.py loaddata registered_users/fixtures/type_documents.json
python manage.py loaddata registered_users/fixtures/countries.json
```

Esto es necesario para que la mutación tenga disponibles los países y tipos de documento relacionados.

---

### 7. Acceder al playground GraphQL

Puedes probar tu API desde:

🔗 http://localhost:8000/graphql

---

## 📮 Ejemplo de mutación `registerUser`

```graphql
mutation {
  registerUser(input: {
    name: "Jorge",
    lastName: "Bermudez",
    username: "jorgeb",
    email: "jorge@example.com",
    password: "Segura123!",
    typeDocumentId: "VGlwZURvY3VtZW50Tm9kZTox",  # ID obtenido por query
    document: "123456789",
    placeExpedition: "Armenia",
    dateExpedition: "2010-04-12",
    address: "Carrera 1 #23-45",
    city: "Armenia",
    phone: "6061234567",
    celPhone: "3051234567",
    emergencyName: "Carlos Bermudez",
    emergencyPhone: "3059876543",
    countryId: "Q291bnRyeU5vZGU6MQ==",           # ID obtenido por query
    isMilitar: false,
    isTemporal: false
  }) {
    user {
      id
      name
      username
    }
  }
}
```

---

## 🔎 ¿Cómo obtener `typeDocumentId` y `countryId`?

```graphql
{
  typeDocuments {
    edges {
      node {
        id
        nameTypeDocument
      }
    }
  }
  countries {
    edges {
      node {
        id
        countryName
      }
    }
  }
}
```

---

## ✅ Validaciones implementadas

- Email único (no duplicado)
- Documento único (no duplicado)
- Contraseña encriptada antes de guardar
- Relaciones consistentes entre modelos (`OneToOne`, `ForeignKey`)
- Exclusión de campos sensibles en nodos (`password`, `verification_token`)

---

## 📬 Contacto

Si deseas revisar o extender este proyecto, puedes contactarme por cualquiera de los siguientes medios:

**Jorge Bairon Bermudez Leon**  
📧 j.bayron.b@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/jorge-bairon-bermudez-leon-6242b81b5)

---
