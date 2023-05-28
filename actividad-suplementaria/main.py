def proceso_bancario(banco, accion, cantidad):
    if accion == "depositar":
        banco.depositar(cantidad)
        print(f"Se depositaron {cantidad} en {banco.nombre}")
    


# Crear objetos de la clase Banco
banco1 = Banco("Banco A", 1000)
banco2 = Banco("Banco B", 500)

# Realizar procesos bancarios en paralelo
proceso1 = proceso_bancario(banco1, "depositar", 200)
proceso2 = proceso_bancario(banco2, "retirar", 300)