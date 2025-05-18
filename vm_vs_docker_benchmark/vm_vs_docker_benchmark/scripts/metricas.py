import psutil
import time
import os
import csv
import subprocess

# 🕒 Duración del benchmark
duration = 60  # segundos
interval = 0.5  # intervalo de medición

print("⏳ Ejecutando benchmark mientras el juego corre...")

# 🟢 Lanzar el juego en segundo plano
proc = subprocess.Popen(["python3", "juego_memoria.py"])

start_time = time.time()
end_time = start_time + duration
iteration_count = 0
results = []

# 🧪 Medición de métricas mientras el juego está activo
while time.time() < end_time and proc.poll() is None:
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory().percent
    latency_start = time.time()
    latency = time.time() - latency_start  # latencia mínima del loop
    results.append([latency, cpu, mem])
    iteration_count += 1
    time.sleep(interval)

# 📁 Crear carpeta de resultados
os.makedirs("results", exist_ok=True)
filepath = os.path.abspath("results/benchmark_juego.csv")

# 💾 Guardar resultados
with open(filepath, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

# 📊 Calcular métricas
latencias = [r[0] for r in results]
cpus = [r[1] for r in results]
mems = [r[2] for r in results]

avg_latency = sum(latencias) / len(latencias)
max_latency = max(latencias)
min_latency = min(latencias)

avg_cpu = sum(cpus) / len(cpus)
max_cpu = max(cpus)
min_cpu = min(cpus)

avg_mem = sum(mems) / len(mems)
max_mem = max(mems)
min_mem = min(mems)

# 📦 Calcular uso de disco del proyecto
base_path = os.path.abspath(".")
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for file in filenames:
        try:
            fp = os.path.join(dirpath, file)
            total_size += os.path.getsize(fp)
        except:
            pass
disk_mb = total_size / (1024 * 1024)

# 📋 Mostrar resultados
print("\n📊 RESUMEN DEL BENCHMARK")
print(f"🧠 RAM promedio: {avg_mem:.2f}%")
print(f"⚙️  CPU promedio: {avg_cpu:.2f}%")
print(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms")
print(f"🔺 Latencia máx: {max_latency*1000:.2f} ms")
print(f"🔻 Latencia mín: {min_latency*1000:.2f} ms")
print(f"🔥 CPU máx: {max_cpu:.2f}%")
print(f"🧊 CPU mín: {min_cpu:.2f}%")
print(f"📈 RAM máx: {max_mem:.2f}%")
print(f"📉 RAM mín: {min_mem:.2f}%")
print(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB")
print(f"🔁 Total de iteraciones: {iteration_count}")
print(f"✅ CSV guardado en: {filepath}")
