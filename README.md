# Computación en la Nube - Actividad: Predicción de Fecha de Modificación

Este repositorio contiene el trabajo realizado para la clase de Computación en la Nube, con el objetivo de crear un modelo predictivo utilizando servicios de Azure. La tarea consiste en desarrollar un modelo de regresión que prediga la fecha de modificación (`ModifiedDate`) de los registros en la tabla `SalesLT.customer`.

## Requisitos

- Python 3.10 o superior
- Librerías definidas en `requirements.txt`
- Acceso a Azure para el despliegue

## Datos Utilizados

- **Fuente**: Base de datos SQL con la tabla `SalesLT.customer`

Para descargar y usar los datos, ejecuta el siguiente código en tu entorno:

```python
import pyodbc

# Configuración de la cadena de conexión para SQL Server
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=tu_servidor;'
                            'DATABASE=tu_base_de_datos;'
                            'UID=tu_usuario;'
                            'PWD=tu_contraseña')

query = "SELECT * FROM SalesLT.customer"
data = pd.read_sql(query, connection)
