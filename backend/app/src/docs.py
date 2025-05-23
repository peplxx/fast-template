from pydantic import BaseModel
from app.src.modules import modules


class ProjectDocs(BaseModel):
    # Info for OpenAPI specification
    class OpenAPI:
        VERSION = "0.1.3"
        WEBSITE_URL = "https://example.com"
        TITLE = "Project Title"
        DESCRIPTION = """Project Description"""

        @property
        def CONTACT_INFO(self) -> dict:
            return {
                "name": "Contact Name",
                "url": self.WEBSITE_URL,
                "email": "contact@gmail.com",
            }

        LICENSE_INFO = {
            "name": "MIT License",
        }

        TAGS_INFO = [
            # {
            #  Here you can define tags for your API explicitly
            #     "name": "Example Tag",
            #     "description": "Example Tag Description",
            # },
            # Here you can define tags for your API automatically from modules
            *[
                tag
                for module in modules
                if hasattr(module, "TAGS")
                for tag in module.TAGS
            ]
        ]

        @property
        def specification(self) -> dict:
            return {
                "title": self.TITLE,
                "description": self.DESCRIPTION,
                "version": self.VERSION,
                "contact": self.CONTACT_INFO,
                "license_info": self.LICENSE_INFO,
                "openapi_tags": self.TAGS_INFO,
            }

    @property
    def specification(self) -> dict:
        return {**self.OpenAPI().specification}


project = ProjectDocs()
