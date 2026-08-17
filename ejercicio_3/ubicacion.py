from pydantic import BaseModel, Field
from typing import Annotated, Optional

CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0)]

class Ubicacion(BaseModel):
    latitud: CoordenadaGPS
    longitud: CoordenadaGPS
    etiqueta: Optional[str] = None