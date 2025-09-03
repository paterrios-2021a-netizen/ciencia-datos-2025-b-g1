# 📄 Documento e-commerce (SmartRetail)

## 1. Escenario
El escenario de análisis será **e-commerce (SmartRetail)**, una empresa de comercio electrónico que procesa:  

- Miles de transacciones por minuto.  
- Reseñas y comentarios de clientes en redes sociales.  
- Datos de sensores IoT en inventario y bodegas en tiempo real.  

Este contexto exige **altas capacidades de procesamiento, escalabilidad y analítica avanzada** para mejorar la experiencia del cliente y optimizar operaciones.  

---

## 2. Introducción  

### Propósito  
El propósito de este documento es **comparar diferentes arquitecturas Big Data** (Hadoop, Spark y arquitecturas en la nube) con el fin de evaluar sus componentes, ventajas, limitaciones y casos de uso. Esto permite seleccionar la solución más adecuada para empresas que manejan grandes volúmenes de datos como SmartRetail.  

### Alcance  
El análisis se centrará en tres arquitecturas Big Data:  

- **Hadoop:** modelo clásico basado en HDFS, YARN y MapReduce.  
- **Apache Spark:** plataforma moderna de procesamiento en memoria con APIs y librerías avanzadas.  
- **Arquitecturas en la nube (ej. AWS, GCP, Azure):** servicios administrados de Big Data con escalabilidad automática.  

### Glosario de términos clave  
- **HDFS (Hadoop Distributed File System):** Sistema de archivos distribuido de Hadoop para almacenar grandes volúmenes de datos.  
- **YARN (Yet Another Resource Negotiator):** Administrador de recursos y planificador de tareas en Hadoop.  
- **MapReduce:** Modelo de programación para procesamiento batch en Hadoop.  
- **RDD (Resilient Distributed Dataset):** Estructura de datos inmutable de Spark para procesar información en paralelo.  
- **ETL (Extract, Transform, Load):** Proceso de extracción, transformación y carga de datos.  

---

## 3. Descripción de arquitecturas  

### a) Hadoop  
**Componentes principales:**  
- **HDFS:** sistema de almacenamiento distribuido.  
- **YARN:** administrador de recursos y tareas.  
- **MapReduce:** motor de procesamiento batch.  

**Ventaja:** Procesa grandes volúmenes de datos históricos.  
**Limite:** Procesamiento lento en comparación con arquitecturas modernas.  

---

### b) Apache Spark  
**Componentes principales:**  
- **Spark Core:** núcleo de procesamiento en memoria.  
- **RDD:** dataset distribuido tolerante a fallos.  
- **Librerías:**  
  - **Spark SQL** (consultas estructuradas).  
  - **MLlib** (machine learning).  
  - **GraphX** (análisis de grafos).  
  - **Spark Streaming** (procesamiento en tiempo real).  

**Ventaja:** Velocidad, soporte batch + streaming, APIs amigables.  
**Limite:** Requiere clúster dedicado y más memoria.  

---

### c) Arquitecturas en la Nube (ej. AWS, GCP, Azure)  
**Componentes principales:**  
- **Servicios gestionados:** AWS EMR, Google BigQuery, Azure Synapse.  
- **Escalabilidad automática:** auto-scaling según carga de trabajo.  
- **Integración IoT y BI:** dashboards, machine learning y analítica en tiempo real.  

**Ventaja:** Pago por uso y administración simplificada.  
**Limite:** Dependencia del proveedor y costos variables según consumo.  
