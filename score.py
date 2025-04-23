
import json
import pickle
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('modelo_modifieddate')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

def run(raw_data):
    try:
        # Leer los datos recibidos
        data = json.loads(raw_data)['data']
        data = pd.DataFrame(data)

        # Predecir los días desde la fecha base
        pred_days = model.predict(data).tolist()

        fecha_base = pd.to_datetime(datos["ModifiedDate"].min())
        pred_dates = (fecha_base + pd.to_timedelta(pred_days, unit='D')).astype(str).tolist()

        return json.dumps(pred_dates)

    except Exception as e:
        return json.dumps({"error": str(e)})
