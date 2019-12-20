# bonificacion para los empleados
import libreria
import os

# si el empleado es contratado o auxiliar
cliente=os.sys.argv[1]
horas_extra=int(os.sys.argv[2])
bonificacion_total=libreria.bonificacion(cliente,horas_extra)
print("su bonificacion es:",bonificacion_total)