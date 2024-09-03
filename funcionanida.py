def tareas():
    # Inicializamos una lista vacía para almacenar las tareas.
    tareas = []

    # Función para agregar una tarea a la lista.
    def agregartareas():
        # Solicitamos al usuario que ingrese el nombre de la tarea.
        tarea = input("Ingresa la tarea a agregar: ")
        # Agregamos la tarea ingresada a la lista de tareas.
        tareas.append(tarea)
        # Informamos al usuario que la tarea ha sido agregada con éxito.
        print(f"La tarea '{tarea}' ha sido agregada.")

    # Función para eliminar una tarea de la lista.
    def eliminartarea():
        # Solicitamos al usuario que ingrese el nombre de la tarea a eliminar.
        tarea = input("Ingresa la tarea a eliminar: ")
        # Verificamos si la tarea ingresada existe en la lista de tareas.
        if tarea in tareas:
            # Si la tarea existe, la eliminamos de la lista.
            tareas.remove(tarea)
            # Informamos al usuario que la tarea ha sido eliminada.
            print(f"La tarea '{tarea}' ha sido eliminada.")
        else:
            # Si la tarea no existe, informamos al usuario.
            print("La tarea no existe.")

    # Función para mostrar todas las tareas en la lista.
    def mostrarTareas():
        # Verificamos si hay alguna tarea en la lista.
        if len(tareas) > 0:
            # Si hay tareas, las mostramos todas.
            print(f"Las tareas a mostrar son: {tareas}")
        else:
            # Si no hay tareas, informamos al usuario.
            print("No hay tareas.")

    # Función para actualizar una tarea existente en la lista.
    def actualizarTareas():
        # Solicitamos al usuario que ingrese el nombre de la tarea que desea actualizar.
        tarea_antigua = input("Ingresa la tarea a actualizar: ")
        # Verificamos si la tarea ingresada existe en la lista de tareas.
        if tarea_antigua in tareas:
            # Si la tarea existe, solicitamos al usuario que ingrese el nuevo nombre de la tarea.
            tarea_nueva = input("Ingresa la nueva tarea: ")
            # Obtenemos el índice de la tarea antigua en la lista.
            indice = tareas.index(tarea_antigua)
            # Actualizamos la tarea antigua con el nuevo nombre en la lista.
            tareas[indice] = tarea_nueva
            # Informamos al usuario que la tarea ha sido actualizada con éxito.
            print(f"La tarea '{tarea_antigua}' ha sido actualizada a '{tarea_nueva}'.")
        else:
            # Si la tarea no existe, informamos al usuario.
            print("La tarea no existe.")

    # Bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir.
    while True:
        # Mostramos un menú de opciones para que el usuario elija qué acción desea realizar.
        print("\n¿Qué deseas realizar? \n 1. Agregar tarea \n 2. Ver tareas \n 3. Eliminar tarea \n 4. Actualizar tarea \n 5. Salir")
        # Solicitamos al usuario que ingrese el número de la opción deseada.
        opcion = input("Ingresa el número de opción que deseas realizar: ")
        # Dependiendo de la opción ingresada, llamamos a la función correspondiente.
        if opcion == "1":
            agregartareas()  # Llamamos a la función para agregar una tarea.
        elif opcion == "2":
            mostrarTareas()  # Llamamos a la función para mostrar las tareas.
        elif opcion == "3":
            eliminartarea()  # Llamamos a la función para eliminar una tarea.
        elif opcion == "4":
            actualizarTareas()  # Llamamos a la función para actualizar una tarea.
        elif opcion == "5":
            # Si el usuario elige la opción 5, informamos que el programa ha finalizado y salimos del bucle.
            print("Programa finalizado.")
            break
        else:
            # Si el usuario ingresa una opción no válida, mostramos un mensaje de error.
            print("Opción no válida.")

# Llamamos a la función principal para que el programa comience a ejecutarse.
tareas()
    