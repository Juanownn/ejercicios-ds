from usuarioSistema import UsuarioSistema
from pydantic import ValidationError

try:
    usuario1 = UsuarioSistema(email="juano@gmail.com", nivel_acceso=6)
except ValidationError as e:
    print("Error de validacion")
    print(e)