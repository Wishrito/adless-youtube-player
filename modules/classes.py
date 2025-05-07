import os
import time
from pathlib import Path

from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from modules.utils import get_chromedriver_path


class AdlessYTBPlayer(Flask):
    def __init__(self, import_name, static_url_path = None, static_folder = "static", static_host = None, host_matching = False, subdomain_matching = False, template_folder = "templates", instance_path = None, instance_relative_config = False, root_path = None):
        super().__init__(
            import_name,
            static_url_path,
            static_folder,
            static_host,
            host_matching,
            subdomain_matching,
            template_folder,
            instance_path,
            instance_relative_config,
            root_path,
        )
        self.vercel_project_production_url = os.getenv("VERCEL_PROJECT_PRODUCTION_URL")
        self.template_folder = Path(__file__).parent.parent / "templates"
        self.static_folder = Path(__file__).parent.parent / "src"
        self.webCookies: str = ""

    def get_cookies(self):
        service = Service(executable_path=get_chromedriver_path())
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options, service=service)
        driver.get("https://www.youtube.com/")
        time.sleep(5)  # Wait for the page to load
        selenium_cookies = driver.get_cookies()
        cookies_dict = {cookie["name"]: cookie["value"] for cookie in selenium_cookies}
        # Convertir en string formaté pour l'en-tête HTTP
        cookie_header = "; ".join([f"{k}={v}" for k, v in cookies_dict.items()])

        driver.quit()
        # Enregistrer les cookies dans une variable
        self.webCookies = cookie_header
        return cookie_header


app = AdlessYTBPlayer(__name__)
