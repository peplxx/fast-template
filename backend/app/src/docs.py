from pydantic import BaseModel


class ProjectDocs(BaseModel):
    # Info for OpenAPI specification
    class OpenAPI:
        VERSION = "0.1.0"
        WEBSITE_URL = "https://example.com"
        TITLE = "Project Title"
        SUMMARY = "Project Summary"
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
            "identifier": "MIT",
        }

        TAGS_INFO = [
            {
                "name": "System",
                "description": "Endpoints related to system operations and health checks.",
            },
            {
                "name": "Static Files",
                "description": "Endpoints for working with static files.",
            },

        ]

        @property
        def specification(self) -> dict:
            return {
                "title": self.TITLE,
                "summary": self.SUMMARY,
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
