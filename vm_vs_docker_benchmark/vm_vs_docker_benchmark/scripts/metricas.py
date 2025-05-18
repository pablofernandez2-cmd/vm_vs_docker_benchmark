import time
import csv
import psutil
import os
import threading
from tkinter import Tk
import random
from functools import partial
import tkinter as tk

results = []
running = True
iteration_count = 0

def monitor(duration=60):
    global iteration_count
    end_time = time.time() + duration
    print("⏳ Ejecutando benchmark por 60 segundos...")

    while running and time.time() < end_time:
        start = time.time()
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        latency = time.time() - start
        results.append([latency, cpu, mem])
        iteration_count += 1
        time.sleep(0.3)

    # Guardar CSV
    os.makedirs("results", exist_ok=True)
    filepath = "results/benchmark_memoria.csv"
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["latency", "cpu_percent", "memory_percent"])
        writer.writerows(results)

    # Calcular estadísticas
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

    # Tamaño total del entorno
    base_path = os.path.abspath(os.path.dirname(__file__))
    total_size = 0
    for dirpath, _, filenames in os.walk(base_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    disk_mb = total_size / (1024 * 1024)

    # Mostrar resumen
    print(f"\n📊 RESUMEN DEL BENCHMARK")
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