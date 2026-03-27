from datetime import datetime

class Paciente:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.historial = []

    def calcularIMC(self):
        return self.peso / (self.altura ** 2)

    def clasificarIMC(self, imc):
        if imc < 18.5: return "Bajo peso"
        if imc < 25.0: return "Normal"
        if imc < 30.0: return "Sobrepeso"
        return "Obesidad"

    def registrarMedicion(self):
        imc_actual = self.calcularIMC()
        clasificacion = self.clasificarIMC(imc_actual)
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        registro = {
            "fecha": fecha_actual,
            "peso": self.peso,
            "imc": round(imc_actual, 2),
            "estado": clasificacion
        }
        self.historial.append(registro)
        print(f"\n✅ Medición registrada con éxito para {self.nombre}.")

    def generarHistorial(self):
        print(f"\n--- Historial de {self.nombre} ---")
        if not self.historial:
            print("No hay mediciones registradas.")
        for m in self.historial:
            print(f"[{m['fecha']}] Peso: {m['peso']}kg | IMC: {m['imc']} | Estado: {m['estado']}")

# --- Lógica del Menú ---
pacientes = []

def seleccionar_paciente():
    if not pacientes:
        print("\n❌ No hay pacientes registrados.")
        return None
    
    print("\nSeleccione un paciente:")
    for i, p in enumerate(pacientes):
        print(f"{i + 1}. {p.nombre}")
    
    opcion = int(input("Seleccione el número: ")) - 1
    if 0 <= opcion < len(pacientes):
        return pacientes[opcion]
    return None

while True:
    print("\n==== CONSULTORIO MÉDICO - SISTEMA IMC ====")
    print("1. Registrar paciente")
    print("2. Calcular IMC (Clasificar y Registrar)")
    print("3. Generar Historial")
    print("4. Salir")
    
    opcion = input("\nElija una opción: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad: "))
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        nuevo_paciente = Paciente(nombre, edad, peso, altura)
        pacientes.append(nuevo_paciente)
        print(f"✅ Paciente {nombre} registrado.")

    elif opcion == "2":
        p = seleccionar_paciente()
        if p:
            # 2.1 Calcular y clasificar
            imc = p.calcularIMC()
            clase = p.clasificarIMC(imc)
            print(f"\nResultado para {p.nombre}:")
            print(f"IMC: {round(imc, 2)} | Clasificación: {clase}")
            
            # 2.1.1 ¿Registrar medición?
            confirmar = input("¿Desea registrar esta medición en el historial? (s/n): ")
            if confirmar.lower() == 's':
                p.registrarMedicion()

    elif opcion == "3":
        print("\n--- 3. Generar Historial ---")
        print("1. Historial General (último estado)")
        print("2. Por Paciente (historial completo)")
        sub_opcion = input("Elija sub-opción: ")

        if sub_opcion == "1":
            print("\n--- RESUMEN GENERAL ---")
            for p in pacientes:
                print(f"Paciente: {p.nombre} | Peso Actual: {p.peso}kg | IMC: {round(p.calcularIMC(), 2)}")
        
        elif sub_opcion == "2":
            p = seleccionar_paciente()
            if p:
                p.generarHistorial()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")