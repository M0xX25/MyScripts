import requests
import sys

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Ver estado de mis numeros")
    print("2. Ver estado de numeros vecinos")
    print("3. Obtener y sumar numero del nodo1")
    print("4. Obtener y sumar sumatoria actual nodo1")
    print("5. Obtener y sumar numero del nodo3")
    print("6. Obtener y sumar sumatoria actual nodo3")
    print("7. Salir")

def ver_estado_numeros_nodo2():
    try:
        response = requests.get("http://172.18.0.12:5002/ofrecer_numeros_nodo2")
        if response.status_code == 200:
            datos = response.json()
            print(f"Numero del nodo2: {datos['numero_nodo2']}")
            print(f"Sumatoria actual del nodo2: {datos['sumatoria_actual_del_nodo2']}")
        else:
            print("Error al obtener el estado de los numeros del nodo2")
    except Exception as e:
        print(f"Error: {e}")

def ver_estado_numeros_vecinos():
    nodos_vecinos = ["nodo1", "nodo3"]
    for nodo in nodos_vecinos:
        try:
            response = requests.get(f"http://172.18.0.12:5002/obtener_nodo{nodo[-1]}/sumatoria_actual")
            if response.status_code == 200:
                datos = response.json()
                print(f"Sumatoria actual del {nodo}: {datos[f'sumatoria_actual_del_{nodo}']}")
            else:
                print(f"Error al obtener el estado de los numeros del {nodo}")
        except Exception as e:
            print(f"Error: {e}")

def obtener_y_sumar_numero(nodo):
    try:
        response = requests.get(f"http://172.18.0.12:5002/obtener_nodo{nodo[-1]}/sumar_su_numero")
        if response.status_code == 200:
            datos = response.json()
            print(datos["mensaje"])
            print(f"Sumatoria actual del nodo2: {datos['sumatoria_actual_del_nodo2']}")
        else:
            print(f"Error al obtener y sumar el numero del {nodo}")
    except Exception as e:
        print(f"Error: {e}")

def obtener_y_sumar_sumatoria_actual(nodo):
    try:
        response = requests.get(f"http://172.18.0.12:5002/obtener_nodo{nodo[-1]}/sumatoria_actual")
        if response.status_code == 200:
            datos = response.json()
            print(f"Sumatoria actual del {nodo}: {datos[f'sumatoria_actual_del_{nodo}']}")
            print(f"Sumatoria actual del nodo2: {datos['sumatoria_actual_del_nodo2']}")
        else:
            print(f"Error al obtener la sumatoria actual del {nodo}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un numero valido.")
            continue

        if opcion == 1:
            ver_estado_numeros_nodo2()
        elif opcion == 2:
            ver_estado_numeros_vecinos()
        elif opcion == 3:
            obtener_y_sumar_numero("nodo1")
        elif opcion == 4:
            obtener_y_sumar_sumatoria_actual("nodo1")
        elif opcion == 5:
            obtener_y_sumar_numero("nodo3")
        elif opcion == 6:
            obtener_y_sumar_sumatoria_actual("nodo3")
        elif opcion == 7:
            print("Saliendo del programa.")
            sys.exit(0)
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 7.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVolviendo al menu principal...")

