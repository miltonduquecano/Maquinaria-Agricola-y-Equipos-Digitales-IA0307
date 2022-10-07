def maquinaria():
    import math
    from nis import match
    from typing import final
    import csv
    import os
    continuar = True
    while continuar:
        menu = (input('''\n
        ===============================================
        Trabajo final selección de maquinaria agrícola


        Milton Duque Cano


        Ingenieria Agronomica, Escuela de Ingenieria, Universidad EAFIT
        Maquinaria Agricola y Equipos Digitales - IA0307
        Prof. Juan Felipe Restrepo Arias
        07 de junio de 2022


        ===============================================

        0.- salir.
        1.- Seleccion maquinaria agricola.
        2.- Mostrar base de datos guardada.

        Seleccione la opcion que desea:\n\n\n'''))

        def openinread():
            miarchivo = open('/Users/miltonduquecano/pycharmandvscode/implementos.txt');
            return (miarchivo)

        def openinwrite():
            miarchivo = open('/Users/miltonduquecano/pycharmandvscode/implementos.txt', 'w');
            return (miarchivo)

        def notaseparadasf():
            miarchivo = openinread()
            notasjuntas = miarchivo.read()
            notaseparadas = notasjuntas.split(',')
            return (notaseparadas)

        def notasjuntasf():
            try:
                miarchivo = openinread()
                notasjuntas = miarchivo.read()
                return (notasjuntas)
            except:
                print('BASE DE DATOS NO ENCONTRADA DEBE CREARLA CON LA OPCION 2 AL FINAL DE: Costos totales de propiedad-costo total vida $ vida/ha vida.')

        def guardar_datos_txt(final, limpiar):
            if limpiar == '1':
                miarchivo = openinread()
                notasjuntas = miarchivo.read()
                notasjuntas = notasjuntas + final
                miarchivo = openinwrite()
                miarchivo.write(notasjuntas)  # +',\n'
                miarchivo.close()

            elif limpiar == '2':
                miarchivo = openinwrite()
                miarchivo = openinread()
                notasjuntas = miarchivo.read()
                notasjuntas = notasjuntas + final
                miarchivo = openinwrite()
                miarchivo.write(notasjuntas)  # +',\n'
                miarchivo.close()
            elif limpiar == '0':
                print('DATOS NO GUARDADOS')

        def limpiar(final):
            while True:
                limpiar = (input
                           ('DEBE LIMPIAR BASE DE DATOS O CREARLA SI ES SU PRIMERA ENTRADA DE INFORMACION DE UN IMPLEMENTO NUEVO \nSI LIMPIAR O CREAR = 2, \nSOLO GUARDAR DATOS\n SI = 1  NO = 0\nINGRESE RESPUESTA:\n\n\n'))
                if limpiar == '1' or limpiar == '2' or limpiar == '0':
                    guardar_datos_txt(final, limpiar)
                    break
                else:
                    print('OPCION INGRESADA NO VALIDA INTENTE DE NUEVO')

        def concatenarstr(resultados):
            j = len(resultados)
            final = ''
            while j != 0:
                final = final + ',;,'
                k = len(resultados[j - 1])
                while k != 0:
                    final = final + ','
                    final = final + str(resultados[j - 1][k - 1])
                    k -= 1
                j -= 1
            limpiar(final)

        def esperar():
            limpiar = (input('\nOK SALIR\nINGRESE CUALQUIER VALOR DEL TECLADO PARA SALIR\nINGRESE RESPUESTA:\n\n\n'))
            if type(limpiar) == type('str'):
                print('OKK')

        # CALCULOS
        if menu == '1':
            def convertir():

                eleccion = (input('''\n
                ===============================================
                OPERACIONES DISPONIBLES
                ===============================================

                0.- salir.
                1.- Costos totales de propiedad-costo total vida $ vida/ha vida.////ESTE APARTADO ES EL PRIMERO QUE SE DEBE INGRESAR SIEMPRE
                2.- Costos de operacion-mano de obra.
                3.- Costos de operacion-Conbustible y aceite.
                4.- Costos de operacion-reparaciones y mantenimiento.
                5.- Costos totales de propiedad y operacion.////SOLO SI INTRODUJO LOS VALORES ANTERIORES PARA EL CALCULO DE LOS DIFERENTES COSTOS

                Seleccione la opcion que desea:\n\n\n'''))
                if eleccion == '1':
                    def costospropiedad():
                        print("Costos totales de propiedad, costo total vida $ vida/ha vida")
                        nombre = [input('Ingrese nombre del implemento =  ')]
                        lista = []
                        resultados = []
                        i = 8
                        while i != 0:
                            data = (input('''
                            Ingrese los valores en orden:
                            Pu= Precio de compra.
                            Sv= Valor de salvamento como porcentaje del precio de compra.
                            Ip= tasa de interés anual, decimal
                            Ig= tasa de inflación general, decimal
                            L= Vida económica en años.
                            Ktis= costo anual de impuestos, seguro y alojamiento como porcentaje del precio de compra.
                            t = uso acumulado, h
                            Ca=capacidad de campo efectiva durante la operación, ha/h

                            EJM. SEGADORA
                            [7000000.0, 0.1, 0.06, 0.03, 10.0, 2.0, 2500.0, 0.89]


                            Ingrese valor:\n\n\n'''))
                            try:
                                data = float(data)
                                lista.append(data)
                                print(lista)
                                if len(lista) == 8:
                                    Ir = (lista[2] - lista[3]) / (1 + lista[2])  # Tasa anual de interés (decimal).
                                    Cos = (1 - lista[1]) * ((Ir * (1 + Ir) ** lista[4]) / ((1 + Ir) ** lista[4] - 1)) + (lista[5] / 100)  # costos de propiedad anuales específicos, decimal.
                                    Coa = Cos * lista[0]  # costos anuales totales de propiedad $/año
                                    Ctv = Coa * lista[4]  # costo total vida implemento
                                    Tiv = lista[6] * lista[7]  # hectareas que trabaja el implemento en toda su vida util ha/vida
                                    Ctvf = Ctv / Tiv  # costo total vida $ vida/ha vida (Ctv)
                                    Ctvf = ['#' + str(Ctvf) + '#']
                                    lista1 = [Ir, Cos, Coa, Ctv, Tiv]
                                    resultados = [nombre, lista, lista1, Ctvf]
                                    print('costo total vida $ vida/ha vida (Ctvf):\n\n\n', Ctvf)

                                    concatenarstr(resultados)

                                i -= 1
                            except:
                                print('# No valido, intente de nuevo con el mismo orden de datos')
                                esperar()

                    costospropiedad()

                elif eleccion == '2':
                    def comanoobra():
                        print("Costos de operacion-mano de obra, costo total vida $ vida/ha vida")
                        lista = []
                        resultados = []
                        i = 1
                        while i != 0:
                            data = (input('''
                            Ingrese los valores en orden:
                            S= salario por mes del empleado.


                            EJM. SEGADORA
                            [1500000]


                            Ingrese valor:\n\n\n'''))
                            try:
                                data = float(data)
                                lista.append(data)
                                print(lista)
                                if len(lista) == 1:
                                    notaseparadas = notaseparadasf()
                                    nombre = [notaseparadas[23]]
                                    Ig = float(notaseparadas[17])  # tasa de inflación general, decimal
                                    l = float(notaseparadas[16])  # Vida económica en años.
                                    Tiv = float(notaseparadas[6])  # hectareas que trabaja el implemento en toda su vida util ha/vida
                                    # OPERACIONES
                                    stmanobra = lista[0] * 1.52 * 12 * l  # gasto en mano de obra en la vida del implemento
                                    Puc = stmanobra * (1 + Ig) ** l  # precio corregida la inflacion
                                    costoha = Puc / Tiv  # costo por hectarea en la vida del implemento
                                    costoha = ['#' + str(costoha) + '#']
                                    lista1 = [stmanobra, Puc]
                                    resultados = [nombre, lista, lista1, costoha]
                                    print('costo total por hectarea para pagar operario:\n\n\n', costoha)

                                    concatenarstr(resultados)
                                i -= 1
                            except:
                                print('# No valido, intente de nuevo con el mismo orden de datos')
                                esperar()

                    comanoobra()

                elif eleccion == '3':
                    def costoscombustibleaceite():
                        print("Costos de operacion-combustible y aceite")
                        lista = []
                        resultados = []
                        i = 11
                        while i != 0:
                            data = (input('''
                            Ingrese los valores en orden:
                            Plf= precio del combustible(DISEL)/L.
                            Plo= Precio del combustible(ACEITE)/L.
                            Tabla 15.3 ASAE costantes
                            A=Costante
                            B=Costante
                            C=Costante
                            W=ancho de trabajo (m)
                            V=velocidad km/h
                            Pro=profundidad de trabajo cm
                            Pnt=Potencia nominal del tractor
                            Rr=Resistencia a la rodadura
                            Pe=peso del tractor en Kg

                            EJM. SEGADORA
                            [2300.0, 15000.0, 0.0, 5.0, 0.0, 2.5, 4.83, 0.0, 82.0, 0.05, 4800.0]

                            Ingrese valor:\n\n\n'''))
                            try:
                                data = float(data)
                                lista.append(data)
                                print(lista)
                                if len(lista) == 11:
                                    notaseparadas = notaseparadasf()
                                    nombre = [notaseparadas[23]]
                                    Ca = float(notaseparadas[13])  # capacidad de campo efectiva durante la operación, ha/h
                                    g = 9.807  # aceleracion de la gravedad
                                    # OPERACIONES
                                    verificar=input('SU IMPLEMETO ES SOLO DE TIRO O USA EL TDF: USA TDF=1 ES DE TIRO=2\n\n\n')
                                    try:
                                        if verificar=='1':
                                            Ppto = (lista[2] + lista[3] * lista[5] + lista[4] * lista[7]) * 1.3  # Potencia en el PTO KW
                                        elif verificar=='2':
                                            Pbt=float(input('INGRESE VALOR DE POTENCIA EN LA BARRA TIRO REQUERIDA EN KW = ')) #potencia en la barra de tiro
                                            Cov=float(input('INGRESE EL FALTOR DE CONVERCION PARA TRASFORMAR LA PBT A TDF O PTO = ')) # faltor de convercion que depende del tipo de tractor y tipo de suelo, se encuentra en el diagrama donde esta la informacion ASAE
                                            Ppto = Pbt/Cov  # Potencia en el PTO O TDF KW
                                    except:
                                        print('VALOR INGRESADO NO VALIDO')
                                        esperar()
                                    traccion = ((lista[10] * g) * lista[9]) / 1000  # traccion del tractor KN
                                    Pt = (traccion * lista[6]) / 3.6  # Potencia de traccion
                                    Pot = Ppto + Pt  # Potencia total
                                    x = Pot / lista[8]  # cuanto consume la maquina de la potencia del tractor, relacion
                                    SFCv = 3.91 + (2.64 * x) - 0.203 * (math.sqrt(173 + 738 * x))  # consumo específico de combustible, base volumétrica, L/kW·h---ifX>0.856, SFCv=0.411 L/kw h
                                    Qifuel = SFCv * Pot  # Combustible consumido por el motor, L/h PARA DISEL
                                    Qioil = (21.69 + 0.59 * lista[8]) / 1000  # Combustible consumido por el motor, L/h PARA aceite
                                    Csfuel = (lista[0] * Qifuel) / Ca  # costos de combustible (o aceite) por hectárea, $/ha PARA DISEL
                                    Csoil = (lista[1] * Qioil) / Ca  # costos de combustible (o aceite) por hectárea, $/ha PARA ACEITE
                                    Cst = Csfuel + Csoil  # Costos totales de combustible y aceite por ha
                                    Cst = ['#' + str(Cst) + '#']
                                    lista1 = [Ppto, traccion, Pt, Pot, x, SFCv, Qifuel, Qioil]
                                    resultados = [nombre, lista, lista1, Cst]
                                    print('costo total por hectarea de combustible:\n\n\n', Cst)

                                    concatenarstr(resultados)

                                i -= 1
                            except:
                                print('# No valido, intente de nuevo con el mismo orden de datos')
                                esperar()

                    costoscombustibleaceite()


                elif eleccion == '4':
                    def reparacionesmantenimiento():
                        print("Costos de operacion-reparaciones y mantenimiento")
                        lista = []
                        resultados = []
                        i = 2
                        while i != 0:
                            data = (input('''
                            Ingrese los valores en orden:
                            factores de reparacion TABLA 15.1 ASAE
                            RF1=factor
                            RF2=factor

                            EJM. SEGADORA
                            [0.16, 2]


                            Ingrese valor:\n\n\n'''))
                            try:
                                data = float(data)
                                lista.append(data)
                                print(lista)
                                if len(lista) == 2:
                                    notaseparadas = notaseparadasf()
                                    nombre = [notaseparadas[23]]
                                    ti = float(notaseparadas[14])  # uso acumulado, h  tabla ASAE
                                    Ig = float(notaseparadas[17])  # tasa de inflación general, decimal
                                    l = float(notaseparadas[16])  # Vida económica en años.
                                    Pu = float(notaseparadas[20])  #[:-1])   Precio de compra del implemento.
                                    Tiv = float(notaseparadas[6])  # hectareas que trabaja el implemento en toda su vida util ha/vida
                                    # OPERACIONES
                                    Puc = Pu * (1 + Ig) ** l  # Precio de compra, $ , corregida la inflacion
                                    Cm = (Puc * lista[0] * (ti / 1000)) ** lista[1]  # costos acumulados de reparación y mantenimiento, $
                                    costoha = Puc / Tiv
                                    costoha = ['#' + str(costoha) + '#']
                                    lista1 = [Puc, Cm]
                                    resultados = [nombre, lista, lista1, costoha]
                                    print('costo total por hectarea de combustible:\n\n\n', costoha)

                                    concatenarstr(resultados)

                                i -= 1
                            except:
                                print('# No valido, intente de nuevo con el mismo orden de datos')
                                esperar()

                    reparacionesmantenimiento()
                elif eleccion == '5':
                    def costosfinal():
                        print(
                            "Costos totales de propiedad y operacion./// SOLO SI INTRODUJO LOS VALORES ANTERIORES DE CALCULO DE LOS DIFERENTES COSTOS")
                        notasjuntas = notasjuntasf()
                        notaseparadas = notaseparadasf()
                        nombre = [notaseparadas[23]]
                        i = len(notaseparadas)
                        lz = []
                        while i != 0:
                            if nombre[0] == notaseparadas[i - 1]:  # se examina la cantidad de datos finales que tiene la base de datos, dependiendo de este valor es la cantidad de iteraciones de la funcion siguiente de suma
                                lz.append(notaseparadas[i - 1])
                            i -= 1

                        try:

                            j = len(lz)
                            ln = []
                            n = 0
                            while j != 0:
                                Pini = (notasjuntas.find(',;,,#')) + 5
                                Pfin = notasjuntas.find("#,;,,", Pini)
                                valor = (notasjuntas[Pini:Pfin])
                                n += float(valor)
                                notasjuntas = notasjuntas.replace(',;,,#' + valor + "#,;,,", 'extraido')
                                if j == 1:
                                    ln.append(n)
                                j -= 1
                            print('Costos totales de propiedad y operacion pesos/ha son:\n\n\n', ln)
                            final = (',/' + str(ln[0]) + '/,')
                            limpiar(final)

                        except:
                            print('ERROR, EN LA BASE DE DATOS EXISTE UN VALOR REPETIDO, INGRESO EN DOS OCACIONES EL MISMO ITEM, DEBE LIMPIAR LA BASE DE DATOS EMPIECE DE NUEVO')
                            esperar()
                            convertir()

                    costosfinal()

                elif eleccion == '6':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '7':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '8':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '9':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '10':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '11':
                    print("EN PREPARACION")
                    convertir()

                elif eleccion == '0':
                    print("\nGracias por usar el seleccionador de maquinaria agricola.")
                    continuar = False

                else:
                    print('NO VALIDO ELIJA DE NUEVO')
                    convertir()

            convertir()

        elif menu == '2':
            print(notasjuntasf())
            esperar()

        # SALIR
        elif menu == '0':
            print("\nGracias por usar el seleccionador de maquinaria agricola.")
            continuar = False

        # OTROS
        else:
            print("\nOPCION NO ENCONTRADA REDIRIGIENDO AL INICIO.")

maquinaria()