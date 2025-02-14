import os
from gerenciamiento_tareas import AdministradorTareas

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    administrador_tareas = AdministradorTareas()

    while True:
        limpiar_terminal()
        print("===== Administrador de Tareas =====")
        print("1.- Crear tarea")
        print("2.- Leer tareas")
        print("3.- Actualizar tarea")
        print("4.- Borrar tarea")
        print("5.- Finalizar tarea")
        print("6.- Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                limpiar_terminal()
                tarea = input("Ingrese la descripción de la tarea: ").capitalize()
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD/MM/YYYY): ")
                descripcion = input("Ingrese una descripción detallada (opcional): ").capitalize()
                administrador_tareas.crear_tarea(tarea, fecha_vencimiento, descripcion)
                print("Tarea creada exitosamente.")

            elif opcion == '2':
                limpiar_terminal()
                tareas = administrador_tareas.leer_tarea()
                if tareas:
                    for tarea in tareas:
                        print(tarea, end="\n\n")
                else:
                    print("No hay tareas registradas.")
                input("Presione Enter para continuar...")
                limpiar_terminal()


            elif opcion == '3':
                limpiar_terminal()
                tareas = administrador_tareas.leer_tarea()
                if tareas:
                    if isinstance(tareas, list):
                        for tarea in tareas:
                            print(tarea, end="\n\n")
                    else: 
                        print(tareas)
                    nombre_tarea = input("Ingrese el nombre de la tarea que desea actualizar: ").capitalize()
                    tarea_encontrada = None
                    for tarea_obj in tareas:
                        if tarea_obj.tarea == nombre_tarea:
                            tarea_encontrada = tarea_obj
                            break
                    if tarea_encontrada:
                        nueva_tarea = input("Ingrese la nueva descripción de la tarea (o presione Enter para omitir): ").capitalize() or None
                        nueva_fecha_vencimiento = input("Ingrese la nueva fecha de vencimiento (YYYY-MM-DD) (o presione Enter para omitir): ") or None
                        nueva_descripcion = input("Ingrese la nueva descripción detallada (o presione Enter para omitir): ").capitalize() or None
                        administrador_tareas.actualizar_tarea(tarea_encontrada.id, nueva_tarea, nueva_fecha_vencimiento, nueva_descripcion)
                        print("Tarea actualizada exitosamente.")
                    else:
                        print("No se encontró ninguna tarea con ese nombre.")
                else:
                    print("No hay tareas registradas.")
                input("Presione Enter para continuar...")
            elif opcion == '4':
                limpiar_terminal()
                tareas = administrador_tareas.leer_tarea()
                if tareas:
                    if isinstance(tareas, list): 
                        for tarea in tareas:
                            print(tarea, end="\n\n")
                    else: 
                        print(tareas)
                    nombre_tarea = input("Ingrese el nombre de la tarea que desea borrar: ").capitalize()
                    tarea_encontrada = None
                    for tarea_obj in tareas:
                        if tarea_obj.tarea == nombre_tarea:
                            tarea_encontrada = tarea_obj
                            break
                    if tarea_encontrada:
                        administrador_tareas.borrar_tarea(tarea_encontrada.id)
                        print("Tarea borrada exitosamente.")
                    else:
                        print("No se encontró ninguna tarea con ese nombre.")
                else:
                    print("No hay tareas registradas.")
                input("Presione Enter para continuar...")

            elif opcion == '5':  
                limpiar_terminal()
                tareas = administrador_tareas.leer_tarea()
                if tareas:
                    if isinstance(tareas, list):
                        for tarea in tareas:
                            print(tarea)
                    else:
                        print(tareas, end="\n\n")
                    nombre_tarea = input("Ingrese el nombre de la tarea que desea finalizar: ").capitalize()
                    tarea_encontrada = None
                    for tarea_obj in tareas:
                        if tarea_obj.tarea == nombre_tarea:
                            tarea_encontrada = tarea_obj
                            break
                    if tarea_encontrada:
                        administrador_tareas.finalizar_tarea(tarea_encontrada.id)
                        print("Tarea finalizada exitosamente.")
                    else:
                        print("No se encontró ninguna tarea con ese nombre.")
                else:
                    print("No hay tareas registradas.")
                input("Presione Enter para continuar...")
            elif opcion == '6':
                break
            else:
                print("Opción inválida. Intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            input("Presione Enter para continuar...")

    administrador_tareas.cerrar()

if __name__ == "__main__":
    main()