import asyncio
import psutil

from ..metrics import metrics


async def system_collector():
    """Collect and update system metrics periodically"""
    while True:
        # CPU metrics
        metrics.system.cpu_usage.set(psutil.cpu_percent())

        # Memory metrics
        memory = psutil.virtual_memory()
        metrics.system.mem_used_gb.set(memory.used / (1024 * 1024 * 1024))
        metrics.system.mem_free_gb.set(memory.free / (1024 * 1024 * 1024))
        metrics.system.mem_total_gb.set(memory.total / (1024 * 1024 * 1024))

        await asyncio.sleep(5)  # Update every 5 seconds
