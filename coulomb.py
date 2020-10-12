import math
import numpy as np

def convert_notacion(num):
    num_cientifico = format(num,".2E")
    return num_cientifico

def distancia_o_magnitud(x,y):
    componente = (math.pow(x,2)) + (math.pow(y,2))
    distancia = math.sqrt(componente)
    return distancia

if __name__ == "__main__":
    K = 9E9
    
    num_cargas = int(input("Ingrese el número de cargas: "))
    magnitud_cargas = []
    x_cargas = []
    y_cargas = []
    for i in range(num_cargas):
        magnitud_carga = float(input("Ingrese la magnitud de la carga: "))
        magnitud_cargas.append(magnitud_carga)
        x_carga = float(input("Ingrese la coordenada X de la carga: "))
        x_cargas.append(x_carga)
        y_carga = float(input("Ingrese la coordenada Y de la carga: "))
        y_cargas.append(y_carga)
    print("\n")
    magnitud_libre = float(input("Ingrese la magnitud de la carga libre: "))
    x_libre = float(input("Ingrese la coordenada X de la carga libre: "))
    y_libre = float(input("Ingrese la coordenada Y de la carga libre: "))
    print("\n")
    vector_d_x =[]
    vector_d_y =[]
    distancias = []
    for i in range(len(magnitud_cargas)):
        pos = i+1
        carga_x = x_cargas[i] - x_libre
        vector_d_x.append(carga_x)
        carga_y =  y_cargas[i] - y_libre
        vector_d_y.append(carga_y)
        d = distancia_o_magnitud(vector_d_x[i], vector_d_y[i])
        print(f'Distancia {pos}: {round(d,2)}')
        distancias.append(d)
    print('\n')
    for i in range(len(vector_d_x)):
        Temp_Coord = [vector_d_x[i],vector_d_y[i]]
        print(f'Vector de D: {Temp_Coord}')
    print('\n')
    fuerza_cargas = []
    signos_iguales = []
    for i in range(len(distancias)):
        pos = i+1
        temp_magintud = magnitud_cargas[i]
        temp_distancia =distancias[i]
        if temp_magintud<0 and magnitud_libre < 0:
            signos_iguales.append(True)
        elif temp_magintud >0 and magnitud_libre >0:
            signos_iguales.append(True)
        else:
            signos_iguales.append(False)
        r = math.pow(temp_distancia,2)
        fuerza = K * ((magnitud_libre*temp_magintud)/r)
        fuerza = abs(fuerza)
        fuerza_cargas.append(fuerza)
        fuerza_show = convert_notacion(fuerza)
        print(f'Fuerza {pos}: {fuerza_show}')
    print("\n")
    angulos_cargas = []
    angulos_cargas_grados = []
    for i in range(len(distancias)):
        pos = i+1
        angulo = math.atan2(vector_d_y[i],vector_d_x[i])
        if signos_iguales[i]:
            angulo = math.pi + angulo
        angulo_grados = math.degrees(angulo)
        angulos_cargas.append(angulo)
        angulos_cargas_grados.append(angulo_grados) 
        print(f'Angulo {pos}: {round(angulo_grados,2)}')
    print("\n")  
    vectores_fuerza = []    
    new_angles = []
    new_angles_show = []
    for i in range(len(distancias)):
        pos = i+1
        Fx = math.cos(angulos_cargas[i]) * fuerza_cargas[i]
        Fy = math.sin(angulos_cargas[i]) * fuerza_cargas[i]
        Fx_show = convert_notacion(Fx)
        Fy_show = convert_notacion(Fy)
        vector_fuerza_show = [Fx_show,Fy_show]
        print(f'Vector de fuerza {pos}: {vector_fuerza_show}')
        vector_fuerza = np.array([Fx,Fy])
        vectores_fuerza.append(vector_fuerza)
    print("\n")
    for i in range(len(vectores_fuerza)):
        pos = i+1
        temp_vector = vectores_fuerza[i]
        Temp_x = convert_notacion(temp_vector[0])
        Temp_y = convert_notacion(temp_vector[1])
        Temp_V = [Temp_x,Temp_y]
        print(f'Vector de fuerza {pos}: {Temp_V}')
    temp_vector = np.array([0,0])
    for vector in vectores_fuerza:
        temp_vector = np.add(temp_vector,vector)
    Temp_x = convert_notacion(temp_vector[0])
    Temp_y = convert_notacion(temp_vector[1])
    Temp_V = [Temp_x,Temp_y]
    print(f'\nVector resultante: {Temp_V}')
    Temp_Mag = distancia_o_magnitud(temp_vector[0],temp_vector[1])
    print('\nMagnitud resultante:' + convert_notacion(Temp_Mag))
    Temp_Angle = math.atan2(temp_vector[1],temp_vector[0])
    Temp_Angle = math.degrees(Temp_Angle)
    print(f'Angulo resultante: {round(Temp_Angle,2)}')