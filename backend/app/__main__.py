import os
import sys
from pathlib import Path
import uvicorn
from app.src.settings import settings

# Change dir to project root (two levels up from this file)
os.chdir(Path(__file__).parents[2])

# Get arguments from command
args = sys.argv[1:]

if __name__ == "__main__":
    uvicorn.run(
        "app.src.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        use_colors=True,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )
