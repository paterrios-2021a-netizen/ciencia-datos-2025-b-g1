# Reglas de Transformación con Historias de Usuario

## 1. Clientes
**Descripción:**  
El conjunto de datos de clientes representa la base de usuarios de TechShop. Para garantizar la calidad de la información, es necesario limpiar, estandarizar y asegurar la unicidad de cada cliente.  

- **Reglas de transformación:**
  - Eliminación de valores nulos en nombres y correos electrónicos.  
  - Eliminación de registros duplicados (ej. clientes registrados más de una vez).  
  - Normalización de nombres a **mayúsculas** para evitar inconsistencias.  

- **Historia de usuario:**  
  *“Como analista de marketing de TechShop, quiero que los datos de los clientes estén limpios y normalizados, para evitar enviar promociones duplicadas y asegurarme de que la información sea consistente al generar reportes de fidelización.”*

---

## 2. Ventas
**Descripción:**  
Los registros de ventas son el corazón del negocio, ya que reflejan los ingresos y la actividad de los clientes. La validación y estandarización de fechas y cantidades aseguran que los análisis financieros sean confiables.  

- **Reglas de transformación:**
  - Conversión de fechas al formato **ISO (YYYY-MM-DD)** para mantener consistencia temporal.  
  - Validación de cantidades como valores numéricos **positivos**, evitando registros con valores negativos o inválidos.  

- **Historia de usuario:**  
  *“Como jefe financiero de TechShop, necesito que las fechas y las cantidades de ventas estén correctamente validadas y en un formato estándar, para poder integrar fácilmente esta información en reportes contables y evitar errores en la proyección de ingresos.”*

---

## 3. Productos
**Descripción:**  
El catálogo de productos es un insumo clave para cruzar la información de ventas y clientes. Los precios deben estar completos y ser válidos, ya que afectan directamente el cálculo de ingresos.  

- **Reglas de transformación:**
  - Validación de precios como valores **no nulos y mayores a cero**.  
  - Eliminación de productos sin información clave (precio o nombre).  

- **Historia de usuario:**  
  *“Como gerente de inventario de TechShop, quiero que los precios de los productos estén siempre completos y correctos, para poder calcular el valor real de las ventas y evitar que los reportes se distorsionen por datos incompletos.”*

---

## 4. Integración
**Descripción:**  
Una vez validados los datos de clientes, ventas y productos, se realiza la integración para obtener una vista consolidada del negocio. Aquí se generan campos calculados que enriquecen los análisis.  

- **Reglas de transformación:**
  - Unión de clientes, ventas y productos por sus identificadores.  
  - Creación de un campo calculado **`monto = cantidad * precio`**, que representa el valor económico de cada transacción.  

- **Historia de usuario:**  
  *“Como analista de datos de TechShop, necesito integrar clientes, ventas y productos en una sola tabla, con un campo que calcule el monto de cada venta, para poder medir el rendimiento de las campañas de marketing y generar informes de rentabilidad más precisos.”*
