#Desarrollo practica Asincrona

#Crear Datos
#Humanos 10 (Países, Gentilicios) Ej: (EL Salvador, salvadoreño) Animales 10 (Especie, tipo) Ej (Canina, Lobo)

#variables de Humanos
país1 = "Dinamarca, Danés"
país2 = "Mexico, Mexicano"
país3 = "Alemania, Alemán"
país4 = "Guatemala, Guatemaltco"
país5 = "Bolivia, Boliviano"
país6 = "Argentina, Argentino"
país7 = "Japón, Japones"
país8 = "Brasil, Brasileño"
país9 = "El salvador, Salvadoreño"
país10 = "Venezuela, Venezolano"

#Variables animales.
especie1 = "Felino, Gato"
especie2 = "Canino, Perro"
especie3 = "Roedor, Ratón"
especie4 = "Ave, Pato"
especie5 = "Reptil, Rana"
especie6 = "Felino, Tigre"
especie7 = "Canino, Lobo"
especie8 = "Roedor, Hamster"
especie9 = "Ave, Pingüino"
especie10 = "Reptil, Serpiente"

#Captura de datos desde teclado. Nombre de usuario


usuario = input("Ingrese su nombre: ")
#Estructura IF ELSE, Mostrar un menú de opciones, Las opciones son Humanos y Animales.


Menu = input('''
             \tMenu
             1- Humanos
             2- Animales
             
             Elegir una opción del menu: ''').lower()

#Estructura IF ELIF
'''Comparar los datos almacenados con los datos capturados al usuario
Al ejecutarse la estructura mostrar un mensaje del gentilicio de ese país
o los tipos de animales pertenecientes a esa especie según la opción seleccionada.'''

if Menu == "humanos" or Menu == "1":
    Menu2 = input(f'''
                  \tListado
                  1- {país1}
                  2- {país2}
                  3- {país3}
                  4- {país4}
                  5- {país5}
                  6- {país6}
                  7- {país7}
                  8- {país8}
                  9- {país9}
                 10- {país10}
                  \nIngrese una opcion del menú: ''')
    
    if Menu2 == país1 or Menu2 == "1":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país1)
        
    elif Menu2 == país2 or Menu2 == "2":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país2)
        
    elif Menu2 == país3 or Menu2 == "3":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país3)
        
    elif Menu2 == país4 or Menu2 == "4":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país4)
        
    elif Menu2 == país5 or Menu2 == "5":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país5)
        
    elif Menu2 == país6 or Menu2 == "6":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país6)
        
    elif Menu2 == país7 or Menu2 == "7":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país7)
        
    elif Menu2 == país8 or Menu2 == "8":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país8)
        
    elif Menu2 == país9 or Menu2 == "9":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país9)
        
    elif Menu2 == país10 or Menu2 == "10":
        print("\n",usuario,"Su nacionaidad y gentilicio es:", país10)
        
    else:
        print("La opcion descrita no está disponible. ")
    
elif Menu == "animales" or Menu == "2":
    Menu2 = input(f'''Menú de las especies
                  1- {especie1}
                  2- {especie2}
                  3- {especie3}
                  4- {especie4}
                  5- {especie5}
                  6- {especie6}
                  7- {especie7}
                  8- {especie8}
                  9- {especie9}
                  10- {especie10}
                  
                  Ingresar una opcion del menú: ''')
    
    if Menu2 == especie1 or Menu2 == "1":
        print("\n",usuario,"usted eligió 'la opción 1' la especie y animal de esta opcion es:", especie1)
        
    elif Menu2 == especie2 or Menu2 == "2":
        print("\n",usuario,"usted eligió 'la opción 2' la especie y animal de esta opcion es:", especie2)
        
    elif Menu2 == especie3 or Menu2 == "3":
        print("\n",usuario,"usted eligió 'la opción 3' la especie y animal de esta opcion es:", especie3)
        
    elif Menu2 == especie4 or Menu2 == "4":
        print("\n",usuario,"usted eligió 'la opción 4' la especie y animal de esta opcion es:", especie4)
        
    elif Menu2 == especie5 or Menu2 == "5":
        print("\n",usuario,"usted eligió 'la opción 5' la especie y animal de esta opcion es:", especie5)
        
    elif Menu2 == especie6 or Menu2 == "6":
        print("\n",usuario,"usted eligió 'la opción 6' la especie y animal de esta opcion es:", especie6)
        
    elif Menu2 == especie7 or Menu2 == "7":
        print("\n",usuario,"usted eligió 'la opción 7' la especie y animal de esta opcion es:", especie7)
        
    elif Menu2 == especie8 or Menu2 == "8":
        print("\n",usuario,"usted eligió 'la opción 8' la especie y animal de esta opcion es:", especie8)
    
    elif Menu2 == especie9 or Menu2 == "9":
        print("\n",usuario,"usted eligió 'la opción 9' la especie y animal de esta opcion es:", especie9)
        
    elif Menu2 == especie10 or Menu2 == "10":
        print("\n",usuario,"usted eligió 'la opción 10' la especie y animal de esta opcion es:", especie10)
        
    else:
        print("La opcion descrita no está disponible.")
        
#Estructuras anidadas, Se formará mediante el desarrollo de los puntos de las dos estructuras anteriores.

else:
    print("\nLa opcion descrita no está disponble.")

print("\nFin del programa.\n")