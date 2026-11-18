def es_correo_valido(correo):
  if correo.count("@") != 1:
    return False
  usuario, dominio = correo.split("@")
  if not usuario or "." not in dominio:
    return False
  return True