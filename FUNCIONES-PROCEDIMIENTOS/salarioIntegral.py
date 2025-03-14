'''
Programa que me permita pagar el salario de un empleado que devenga por horas.

ANALISIS: QUÉ
    ENTRADAS : horasTrabajadas, valorHora
    PROCESOS : pago = horasTrabajadas * valorHora
    SALIDAS  : pago
'''

#[1]. IMPORTAR LIBRERIAS - PREDEFINIDAS DE PYTHON O PROPIAS
import os
import libreria

#[2]. DEFINIR FUNCIONES - PROCEDIMIENTOS - PROPIAS - REGRESA A DONDE FUE LLAMADO

def calcularPago( horasTrabajadas, valorHora ):
    return horasTrabajadas * valorHora

def mostrarPago ( horasTrabajadas, valorHora, pago ):
    print("*" * 50)
    print("HORAS LABORADAS  VALOR HORA   PAGO ")
    print("*" * 50)
    print(f"{horasTrabajadas} \t {valorHora} \t {pago}")


libreria.limpiarPantalla()   #invocando o llamando el procedimiento
#[3]. VARIABLES GLOBALES
pago = 0

#[4]. ENTRADAS
horasTrabajadas = int(input("HORAS TRABAJADAS: "))
valorHora       = int(input("VALOR HORA: "))

#[5]. PROCESOS
#pago = horasTrabajadas * valorHora
pago = calcularPago( horasTrabajadas, valorHora )

#[6]. SALIDAS   con variables locales
mostrarPago ( horasTrabajadas, valorHora, pago )

