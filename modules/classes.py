import os
from pathlib import Path

from flask import Flask


class AdlessYTBPlayer(Flask):
    def __init__(self, import_name, static_url_path = None, static_folder = "static", static_host = None, host_matching = False, subdomain_matching = False, template_folder = "templates", instance_path = None, instance_relative_config = False, root_path = None):
        super().__init__(import_name, static_url_path, static_folder, static_host, host_matching, subdomain_matching, template_folder, instance_path, instance_relative_config, root_path)
        self.vercel_project_production_url = os.getenv("VERCEL_PROJECT_PRODUCTION_URL")
        self.template_folder = Path(__file__).parent.parent / "templates"
        self.static_folder = Path(__file__).parent.parent / "src"
