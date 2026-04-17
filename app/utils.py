import numpy as np

def prepare_features(form_data):
    try:
        return np.array([[float(x) for x in form_data]])
    except:
        return None