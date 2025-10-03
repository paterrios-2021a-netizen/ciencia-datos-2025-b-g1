# Conclusiones del Proyecto ETL - TechShop

**Autor:** Paula Andrea Terrios Ossa  
**Materia:** Ciencia de Datos  
**Tema:** Flujo ETL  
**Proyecto:** TechShop  

---

## Conclusiones 

1. El uso de un único archivo JSON permitió centralizar toda la información de clientes, productos y ventas, lo que simplificó la etapa de **extracción**.  
2. La **fase de transformación** resultó clave para mejorar la calidad de los datos, ya que se eliminaron valores nulos, duplicados y se unificaron formatos de fechas.  
3. La normalización de los nombres de clientes y la validación de los correos electrónicos aumentaron la consistencia de la información, haciéndola más confiable para análisis futuros.  
4. La creación del campo calculado `monto = cantidad * precio` aportó valor agregado al dataset final, permitiendo un análisis directo de las ventas.  
5. La carga en la tabla `ventas_limpias` de SQLite evidenció la importancia de definir un **modelo de datos destino** bien estructurado para integrar diversas entidades.  
6. El proceso demostró que, aunque se parta de un único archivo JSON, sigue siendo necesario un **flujo ETL completo** para garantizar la calidad, integridad y utilidad de los datos.  

---

## Reflexión Crítica

Trabajar con un único archivo JSON simplificó la extracción, ya que toda la información se encontraba centralizada.  
El reto principal fue la **normalización de formatos**, especialmente en las fechas que venían con estilos distintos (YYYY-MM-DD, YYYY/MM/DD y DD-MM-YYYY).  

Otro reto fue la **limpieza de duplicados** en la tabla de clientes y el manejo de valores nulos.  
La integración de clientes, ventas y productos requirió definir una clave común y validar la consistencia de los datos.  

Este ejercicio mostró que incluso con una sola fuente de datos, es necesario aplicar un proceso ETL completo para garantizar la calidad y utilidad de la información.
