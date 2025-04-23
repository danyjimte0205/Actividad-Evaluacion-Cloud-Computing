# Computación en la Nube - ACTIVIDAD DE EVALUACIÓN: Despliegue de un servicio entrenado a partir de una base de datos SQL - Actividad: Predicción de Fecha de Modificación

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


## Instrucciones para el Uso
- **1. Clonar el repositorio**

Clona este repositorio a tu máquina local:

git clone https://github.com/tuusuario/Cloud-Computing-Prediction.git
cd Cloud-Computing-Prediction

- **2. Instalar dependencias**

Instala las librerías requeridas:

pip install -r requirements.txt

- **3. Preprocesamiento de los datos**

Preprocesa los datos utilizando el script score.py:

from score import preprocess_data
data_preprocessed = preprocess_data(data)


- **4. Entrenamiento del modelo**

Usa el notebook Model.ipynb para entrenar el modelo de regresión con los datos preprocesados. El modelo predirá la ModifiedDate.

- **5. Desplegar el modelo en Azure**

Despliega el modelo entrenado en Azure utilizando el script deployment.ipynb. Este notebook contiene los pasos para configurar el servicio web en Azure para el despliegue del modelo.

- **6. Uso de la API para hacer inferencias**

Usa el notebook API.ipynb para enviar datos al servicio web desplegado y recibir predicciones de la ModifiedDate para cada cliente:

from api import get_predictions
predictions = get_predictions(input_data)





