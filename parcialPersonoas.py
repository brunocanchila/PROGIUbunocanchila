class Personas:
    def __init__(self):
        self.personas = []

    def crear_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        self.personas.append(nombre)
        print(f"Se ha creado la persona: {nombre}")

    def listar_personas(self):
        if not self.personas:
            print("No hay personas registradas.")
        else:
            print("Listado de personas:")
            for persona in self.personas:
                print(f"- {persona}")

    def eliminar_persona(self):
        if not self.personas:
            print("No hay personas registradas.")
        else:
            print("Listado de personas:")
            for i, persona in enumerate(self.personas):
                print(f"{i+1}. {persona}")
            indice = int(input("Ingrese el número de la persona a eliminar: "))
            if 1 <= indice <= len(self.personas):
                nombre_eliminado = self.personas.pop(indice - 1)
                print(f"Se ha eliminado a la persona: {nombre_eliminado}")
            else:
                print("Opción inválida.")

class Universidades:
    def __init__(self):
        self.universidades = []

    def crear_universidad(self):
        nombre = input("Ingrese el nombre de la universidad: ")
        self.universidades.append(nombre)
        print(f"Se ha creado la universidad: {nombre}")

    def listar_universidades(self):
        if not self.universidades:
            print("No hay universidades registradas.")
        else:
            print("Listado de universidades:")
            for universidad in self.universidades:
                print(f"- {universidad}")

    def eliminar_universidad(self):
        if not self.universidades:
            print("No hay universidades registradas.")
        else:
            print("Listado de universidades:")
            for i, universidad in enumerate(self.universidades):
                print(f"{i+1}. {universidad}")
            indice = int(input("Ingrese el número de la universidad a eliminar: "))
            if 1 <= indice <= len(self.universidades):
                nombre_eliminado = self.universidades.pop(indice - 1)
                print(f"Se ha eliminado la universidad: {nombre_eliminado}")
            else:
                print("Opción inválida.")

class Notas:
    def __init__(self):
        self.notas = []

    def crear_nota(self):
        titulo = input("Ingrese el título de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")
        self.notas.append({"titulo": titulo, "contenido": contenido})
        print(f"Se ha creado la nota: {titulo}")

    def listar_notas(self):
        if not self.notas:
            print("No hay notas registradas.")
        else:
            print("Listado de notas:")
            for nota in self.notas:
                print(f"- {nota['titulo']}")

    def eliminar_nota(self):
        if not self.notas:
            print("No hay notas registradas.")
        else:
            print("Listado de notas:")
            for i, nota in enumerate(self.notas):
                print(f"{i+1}. {nota['titulo']}")
            indice = int(input("Ingrese el número de la nota a eliminar: "))
            if 1 <= indice <= len(self.notas):
                nota_eliminada = self.notas.pop(indice - 1)
                print(f"Se ha eliminado la nota: {nota_eliminada['titulo']}")
            else:
                print("Opción inválida.")

class Asignaturas:
    def __init__(self):
        self.asignaturas = []

    def crear_asignatura(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        self.asignaturas.append(nombre)
        print(f"Se ha creado la asignatura: {nombre}")

    def listar_asignaturas(self):
        if not self.asignaturas:
            print("No hay asignaturas registradas.")
        else:
            print("Listado de asignaturas:")
            for asignatura in self.asignaturas:
                print(f"- {asignatura}")

    def eliminar_asignatura(self):
        if not self.asignaturas:
            print("No hay asignaturas registradas.")
        else:
            print("Listado de asignaturas:")
            for i, asignatura in enumerate(self.asignaturas):
                print(f"{i+1}. {asignatura}")
            indice = int(input("Ingrese el número de la asignatura a eliminar: "))
            if 1 <= indice <= len(self.asignaturas):
                nombre_eliminado = self.asignaturas.pop(indice - 1)
                print(f"Se ha eliminado la asignatura: {nombre_eliminado}")
            else:
                print("Opción inválida.")

def menu_principal():
    personas = Personas()
    universidades = Universidades()
    notas = Notas()
    asignaturas = Asignaturas()

    while True:
        print("MENU PRINCIPAL")
        print("1. PERSONAS")
        print("2. UNIVERSIDADES")
        print("3. NOTAS")
        print("4. ASIGNATURAS")
        print("5. SALIR")

        seleccion = input("Ingrese la opción deseada: ")

        if seleccion == "1":
            menu_personas(personas)
        elif seleccion == "2":
            menu_universidades(universidades)
        elif seleccion == "3":
            menu_notas(notas)
        elif seleccion == "4":
            menu_asignaturas(asignaturas)
        elif seleccion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_personas(personas):
    while True:
        print("SUBMENU PERSONAS")
        print("1. CREAR PERSONA")
        print("2. LISTAR PERSONAS")
        print("3. ELIMINAR PERSONA")
        print("4. ATRAS")

        seleccion = input("Ingrese la opción deseada: ")

        if seleccion == "1":
            personas.crear_persona()
        elif seleccion == "2":
            personas.listar_personas()
        elif seleccion == "3":
            personas.eliminar_persona()
        elif seleccion == "4":
            print("Volviendo al menú principal...")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_universidades(universidades):
    while True:
        print("SUBMENU UNIVERSIDADES")
        print("1. CREAR UNIVERSIDAD")
        print("2. LISTAR UNIVERSIDADES")
        print("3. ELIMINAR UNIVERSIDAD")
        print("4. ATRAS")

        seleccion = input("Ingrese la opción deseada: ")

        if seleccion == "1":
            universidades.crear_universidad()
        elif seleccion == "2":
            universidades.listar_universidades()
        elif seleccion == "3":
            universidades.eliminar_universidad()
        elif seleccion == "4":
            print("Volviendo al menú principal...")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_notas(notas):
    while True:
        print("SUBMENU NOTAS")
        print("1. CREAR NOTA")
        print("2. LISTAR NOTAS")
        print("3. ELIMINAR NOTA")
        print("4. ATRAS")

        seleccion = input("Ingrese la opción deseada: ")

        if seleccion == "1":
            notas.crear_nota()
        elif seleccion == "2":
            notas.listar_notas()
        elif seleccion == "3":
            notas.eliminar_nota()
        elif seleccion == "4":
            print("Volviendo al menú principal...")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def menu_asignaturas(asignaturas):
    while True:
        print("SUBMENU ASIGNATURAS")
        print("1. CREAR ASIGNATURA")
        print("2. LISTAR ASIGNATURAS")
        print("3. ELIMINAR ASIGNATURA")
        print("4. ATRAS")

        seleccion = input("Ingrese la opción deseada: ")

        if seleccion == "1":
            asignaturas.crear_asignatura()
        elif seleccion == "2":
            asignaturas.listar_asignaturas()
        elif seleccion == "3":
            asignaturas.eliminar_asignatura()
        elif seleccion == "4":
            print("Volviendo al menú principal...")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
    
# yajaira rodriguez, bruno canchila 