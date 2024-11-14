from .system import collect_system_metrics
import asyncio
import time
# Just to make sure that modules are imported
collectors = [
    collect_system_metrics,
]

def run_collectors():

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    while True:
        try:
            event_loop.run_until_complete(asyncio.gather(*collectors))
            
        except Exception as e:
            print(f"Error in collectors: {str(e)}")
            time.sleep(5)  # Wait before retry on error
