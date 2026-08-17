from pydantic import BaseModel, Field
from typing import Union
from enum import Enum

class tipoDispositivo(Enum):
    SENSOR = "sensor"
    ACTUADOR = "actuador"
    GATEWAY = "gateway"

class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: tipoDispositivo

