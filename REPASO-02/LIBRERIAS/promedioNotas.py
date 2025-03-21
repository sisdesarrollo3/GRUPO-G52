'''
HALLAR EL PROMEDIO DE TRES NOTAS, de un estudiante
ANALISIS  R                                  D                      S
    QUE ME DAN - QUE NECESITO  <=> ENTRADAS: nota1, nota2, nota3
    FORMULAS                   <=> PROCESOS: promedio = (nota1 + nota2 + nota3) / 3
    QUE ME PIDEN - QUE MUESTRO <=> SALIDAS : promedio
'''
import libreria

#DEFINICION O CUERPO O CONSTRUCJCION DE FUNCIONES PROPIAS
def calcularPromedio ( nota1, nota2, nota3 ):    
    #pueden haber mas instrucciones
    return (nota1 + nota2 + nota3) / 3

#PROCEDIMIENTO - NO RETORNA NINGUN VALOR
def generarSalidas (nombreEstudiante, nota1, nota2, nota3, promedio):
    print("ESTUDIANTE NOTA1 NOTA2 NOTA3 PROMEDIO")
    print("_" * 40)
    #print(nombreEstudiante, '\t', nota1,'\t', nota2, '\t', nota3, '\t', promedio)
    print(f"{nombreEstudiante} \t {nota1} \t {nota2} \t {nota3} \t {promedio:.2f}")


#P  EL PROGRAMA
#[1].  VARIABLES INICIALIZADAS EN UN VALOR DE ACUERDO AL TIPO
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
promedio = 0.0
nombreEstudiante = ""

#[2]. ENTRADAS 
nombreEstudiante = libreria.leerCadena ( "NOMBRE: ") #nombreEstudiante = input("ESTUDIANTE: ")
nota1 = libreria.leerFlotante( "NOTA 1: " )         #nota1 = float(input("NOTA 1:"))
nota2 = libreria.leerFlotante( "NOTA 2: " )         #nota2 = float(input("NOTA 2:"))
nota3 = libreria.leerFlotante( "NOTA 3: " )         #nota3 = float(input("NOTA 3:"))

#[3]. PROCESOS O FORMULAS
#promedio = (nota1 + nota2 + nota3) / 3
promedio = calcularPromedio ( nota1, nota2, nota3 )  #invocamos o llamamos la funcion

#[4]. SALIDAS - PROCEDIMIENTOS
generarSalidas (nombreEstudiante, nota1, nota2, nota3, promedio)
