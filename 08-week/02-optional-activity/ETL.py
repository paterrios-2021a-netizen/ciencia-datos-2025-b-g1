import pandas as pd
import sqlite3
import json

# 1. Extracción
with open("datasets_origen/techshop.json", "r") as f:
    data = json.load(f)

clientes = pd.DataFrame(data["clientes"])
productos = pd.DataFrame(data["productos"])
ventas = pd.DataFrame(data["ventas"])

# 2. Transformación
# Limpieza de clientes: eliminar nulos y duplicados
clientes = clientes.dropna().drop_duplicates()

# Normalizar nombres de clientes
clientes["nombre"] = clientes["nombre"].str.upper()

# Normalizar formato de fechas en ventas
ventas["fecha"] = pd.to_datetime(ventas["fecha"], errors="coerce")

# Integración
df = ventas.merge(clientes, on="id_cliente", how="inner")
df = df.merge(productos, on="id_producto", how="inner")

# Calcular monto
df["monto"] = df["cantidad"] * df["precio"]

# 3. Carga
conn = sqlite3.connect("techshop.db")
df.to_sql("ventas_limpias", conn, if_exists="replace", index=False)
conn.close()

print("Proceso ETL completado. Datos cargados en 'ventas_limpias'")
