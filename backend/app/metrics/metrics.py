from prometheus_client import Counter, Gauge, Summary

class Metrics:

    class System:
        cpu_usage = Gauge('system_cpu_usage', 'CPU usage')

        mem_used_gb = Gauge('system_mem_used_gb', 'Memory used in GB')
        mem_total_gb = Gauge('system_mem_total_gb', 'Memory total in GB')
        mem_free_gb = Gauge('system_mem_free_gb', 'Memory free in GB')
    
    class General:
        responses = Counter('responses', 'Responses', labelnames=['code', 'path', 'method'])
        request_latency_ms = Summary('request_latency_ms', 'Time spent processing request')

    system: System = System()
    general: General = General()

metrics: Metrics = Metrics()

__all__ = ['metrics']

