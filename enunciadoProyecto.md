# Proyecto de Evaluación Comparativa de Rendimiento: VM vs Docker

Este proyecto compara el uso de recursos y las métricas de rendimiento entre una máquina virtual completa (VirtualBox) y un contenedor Docker.

---

## 📚 Estructura Sugerida para la Presentación del Proyecto

### 1. Introducción
- ¿Qué son las máquinas virtuales?
- ¿Qué son los contenedores?
- Conceptos clave: hipervisor, contenedor, imagen, kernel, etc.

### 2. Configuración del Entorno de Prueba
- Especificaciones de la máquina host
- Sistema operativo de la máquina virtual
- Imagen base utilizada en Docker

### 3. Métricas y Herramientas Utilizadas
- Uso de CPU y memoria
- Tiempo de arranque
- Pruebas de rendimiento
- Rendimiento de una aplicación real
- Aislamiento y seguridad
- Portabilidad y flexibilidad

### 4. Resultados
- Tablas comparativas
- Gráficos de barras o líneas
- Gráfico de radar (araña) para resumen visual

### 5. Análisis
- Fortalezas y debilidades de cada enfoque
- Interpretación de métricas cuantitativas y cualitativas

### 6. Conclusión
- ¿Cuándo usar VM?
- ¿Cuándo usar Docker?

---

## ✅ Métricas de Comparación Sugeridas

### 🔧 1. Uso de Recursos
- **CPU**: carga durante inactividad y bajo estrés
- **Memoria RAM**: uso al ejecutar la misma aplicación
- **Espacio en disco**: instalación base + app + dependencias

**📌 Herramientas sugeridas:**
- `htop`, `top`, `docker stats`, `VBoxManage metrics`, `vmstat`

---

### ⚡ 2. Tiempo de Arranque / Inicio
- Medir el tiempo necesario para iniciar una VM vs iniciar un contenedor Docker

**📌 Herramientas sugeridas:**
- Scripts con `time`, `systemd-analyze`, diferencia de timestamps

---

### 🚀 3. Pruebas de Rendimiento

#### CPU
- Herramientas: `sysbench`, `stress-ng`, `Geekbench`

#### Disco (E/S)
- Herramientas: `fio`, `dd if=/dev/zero of=testfile bs=1G count=1 oflag=dsync`

#### Red
- Herramientas: `iperf3` (dentro de contenedor/VM y desde el host)

---

### 📦 4. Caso de Prueba de Aplicación

**Aplicación sugerida:** servidor MySQL o app Node.js

Métricas:
- Tiempo de despliegue
- Rendimiento (req/s)
- Latencia (tiempo de respuesta)
- Uso de recursos bajo carga

---

### 🔒 5. Aislamiento y Seguridad

**Comparación cualitativa:**
- Separación del kernel (VM tiene mayor aislamiento)
- Docker comparte kernel: más eficiente, menor aislamiento
- Capas de seguridad: AppArmor, SELinux, etc.

---

### ♻️ 6. Portabilidad y Flexibilidad

**Evaluación cualitativa:**
- Facilidad para exportar/importar imágenes (VM vs Docker)
- Soporte multiplataforma (Windows/macOS/Linux)
- Compatibilidad con herramientas DevOps (CI/CD)

---

