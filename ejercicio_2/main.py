from dispositivo import Dispositivo, tipoDispositivo

dispositivo1 = Dispositivo(id_dispositivo=1, tipo=tipoDispositivo.SENSOR)

dispositivo2 = Dispositivo(id_dispositivo="123", tipo="gateway")

#dispositivo1 = Dispositivo(id_dispositivo=12, tipo="incorrecto")

print(dispositivo1.id_dispositivo)
print(dispositivo2.id_dispositivo)
print(dispositivo1.tipo)
print(dispositivo2.tipo)