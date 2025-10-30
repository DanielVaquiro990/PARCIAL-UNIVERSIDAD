# 🎓 Sistema de Gestión de Estudiantes y Cursos

## 🧩 Descripción General

Este sistema fue desarrollado con **FastAPI**, **SQLAlchemy** y **Pydantic**, simulando una aplicación universitaria para la **gestión académica**.

Permite:

- Registrar **estudiantes** con cédula única.  
- Registrar **cursos** con fecha y horario.  
- **Matricular estudiantes** evitando conflictos de horario.  
- Consultar qué estudiantes están matriculados en cada curso.  
- Mostrar mensajes claros cuando un curso **no tiene estudiantes matriculados**.  

---

## ⚙️ Tecnologías Utilizadas

| Tecnología | Descripción |
|-------------|-------------|
| **Python 3.13** | Lenguaje de programación base |
| **FastAPI** | Framework web moderno para construir APIs rápidas |
| **SQLAlchemy** | ORM que permite manejar la base de datos usando clases |
| **Pydantic** | Librería para validar datos entrantes y salientes |
| **Uvicorn** | Servidor que ejecuta la aplicación FastAPI |

---

## 📂 Estructura del Proyecto

El proyecto **PARCIAL-UNIVERSIDAD** está organizado de la siguiente manera:

* **`main.py`**: 🚀 Archivo principal del sistema, responsable de inicializar y exponer la **API**.
* **`models.py`**: 🧱 Define las tablas de la base de datos utilizando **clases ORM** (Object-Relational Mapping).
* **`schemas.py`**: 📝 Define los modelos de validación de datos utilizando **Pydantic**.
* **`database.py`**: 🔗 Contiene la lógica para conectar y configurar la **base de datos**.
* **`requirements.txt`**: 📦 Lista de **librerías** y dependencias necesarias para ejecutar el proyecto.
* **`README.md`**: 📑 **Documentación** general del proyecto.

---

## 🧭 Instrucciones del Proyecto

A continuación se explican los pasos necesarios para **configurar, ejecutar y probar** el sistema de gestión universitaria.

---

### 🧩 1️⃣ Requisitos previos

Antes de iniciar, asegúrate de tener instalado:

- **Python 3.10 o superior**
- **pip** (administrador de paquetes de Python)
- Un editor como **VS Code** o **PyCharm**


# 🚀 Guía de Inicio Rápido

## 🐍 Activación del Entorno Virtual

Sigue estos pasos para configurar y activar el entorno virtual del proyecto:

1.  **Verifica tu versión de Python:**
    Asegúrate de tener instalada una versión compatible de Python ejecutando el siguiente comando:

    ```bash
    python3 --version
    ```

2.  **Crea el Entorno Virtual:**
    Crea un entorno virtual llamado `.venv` en la raíz del proyecto:

    ```bash
    python3 -m venv .venv
    ```

3.  **Activa el Entorno Virtual:**
    Activa el entorno virtual con el siguiente comando:

    ```bash
    source .venv/bin/activate
    ```

---

## 🛠 Instalación de Requerimientos

Con el entorno virtual activado, instala todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```
## ▶️ Ejecución del Sistema

Ya con los requerimientos ejecutados y el entorno activado, podrás iniciar el sistema de la siguiente manera:

```bash
uvicorn main:app --reload
```

## 🎉 ¡Disfrutalo!


Si sale error al activarlo
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Para activarlo en Windows
.\.venv\Scripts\Activate






