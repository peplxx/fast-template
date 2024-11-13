from typing import List, Dict
from ..base import BaseModule
from .routes import router
from .services import FileService
from .exceptions import FileNotFoundException, InvalidFileException
class StaticModule(BaseModule):
    NAME = "static"
    DESCRIPTION = "Module for handling static files and file upload s"
    VERSION = "0.1.0"
    ROUTERS = [router]
    
    
    EXPORTS = {
        "router": router,
        "exceptions": [FileNotFoundException, InvalidFileException]
    }
    
    DEPENDENCIES = []  # If you have a storage module
    
    # OpenAPI tags for documentation
    TAGS = [{
        "name": "Static Files",
        "description": "Operations with static files including upload and retrieval",
    }]
    
    # Module configuration and health checks
    def __init__(self):
        self.storage_path = FileService.STORAGE_PATH
        
    @property
    def stats(self) -> Dict:
        """Return module statistics"""
        try:
            total_files = len(list(self.storage_path.glob("*")))
            total_size = sum(f.stat().st_size for f in self.storage_path.glob("*") if f.is_file())
            
            return {
                "total_files": total_files,
                "total_size_bytes": total_size,
                "storage_path": str(self.storage_path)
            }
        except:
            return {}

__all__ = ["router"]
