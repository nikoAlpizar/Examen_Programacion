import random
import json
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, numero):
        
        if numero > self.numero_secreto:
            print(" El número es demasiado alto. ¡Intenta de nuevo!")
        elif numero < self.numero_secreto:
            print(" El número es muy bajo. ¡Sigue intentando!")
        else:
            print(" ¡Increíble! Adivinaste el número. ¡Buen trabajo!")
            return True
        return False

    def registrarIntento(self):
       
        self.intentos += 1
        

    def reiniciar_juego(self):
       
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registrar_partida(self, intentos, gano):
        
        self.historial.append({"intentos": intentos, "gano": gano})

    def mostrar_estadisticas(self):
       
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for partida in self.historial if partida["gano"])
        ###porcentaje_aciertos = (partidas_ganadas / partidas_jugadas) * 100 if partidas_jugadas > 0 else 0
        intentos_totales = sum(partida["intentos"] for partida in self.historial)
        porcentaje_aciertos = (partidas_ganadas / intentos_totales) * 100 if partidas_jugadas > 0 else 0
        
        
        
        print(f"\n Estadísticas de {self.nombre}:")
        print(f"- Partidas jugadas: {partidas_jugadas}")
        print(f"- Partidas ganadas: {partidas_ganadas}")    
        print(f"- Intentos totales: {intentos_totales}")      
        print(f"- Porcentaje de éxito: {porcentaje_aciertos:.2f}%")


def cargar_estadisticas(nombre_jugador):
    
    if os.path.exists("estadisticas.json"):
        try:
            with open("estadisticas.json", "r") as archivo:
                datos = json.load(archivo)
                return datos.get(nombre_jugador, [])
        except json.JSONDecodeError:
            print(" Parece que hubo un problema con el archivo de estadísticas. Se empezará desde cero.")
    return []


def guardar_estadisticas(jugador):
    
    datos = {}
    if os.path.exists("estadisticas.json"):
        try:
            with open("estadisticas.json", "r") as archivo:
                datos = json.load(archivo)
        except json.JSONDecodeError:
            print(" No se pudieron recuperar estadísticas previas.")

    datos[jugador.nombre] = jugador.historial

    with open("estadisticas.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        print(" Tus estadísticas han sido guardadas.")


def jugar(jugador):
    
    juego = JuegoAdivinanza()
    print(f"\n Hola {jugador.nombre}! El juego ha comenzado. Adivina un número entre 1 y 100.\n")

    while True:
        try:
            numero = int(input(" Ingresa tu número: "))
            juego.registrarIntento()
            if juego.validarNumero(numero):
                jugador.registrar_partida(juego.intentos, True)
                break
        except ValueError:
            print(" Eso no parece un número válido. Intenta con un número entre 1 y 100.")

    print(f"\n **¿Te gustaría jugar otra vez?**")
    eleccionSalida=input("Escribe 'menu' para regresar al menu principal, 'jugar' para volver a jugar o 'salir' para finalizar el juego: ").strip().lower()
    if  eleccionSalida == "salir":
       guardar_estadisticas(jugador)
       print(f" Gracias por jugar, {jugador.nombre}. ¡Hasta la próxima!")
       exit()
    elif eleccionSalida == "jugar":
        jugar(jugador)
    elif eleccionSalida== "menu":
        __name__
if __name__ == "__main__":
    print(" Bienvenido al juego de adivinanza ")
    nombre = input("Por favor, escribe tu nombre para empezar: ").strip()
    historial = cargar_estadisticas(nombre)

    jugador = Jugador(nombre)
    jugador.historial = historial

    while True:
        print("\n Menú Principal:")
        print("1. Iniciar una partida")
        print("2. Ver mis estadísticas")
        print("3. Salir del juego")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            jugar(jugador)
        elif opcion == "2":
            jugador.mostrar_estadisticas()
        elif opcion == "3":
            guardar_estadisticas(jugador)
            print(f" Gracias por jugar, {jugador.nombre}. ¡Hasta la próxima!")
            break
        else:
            print(" Opción inválida. Por favor elige una opción del menú.")