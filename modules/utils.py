from pathlib import Path
import platform

def get_chromedriver_path() -> Path:
    base_dir = Path("src") / "drivers"
    system = platform.system()

    driver_path = None
    if system == "Windows":
        driver_path = base_dir / "chromedriver.exe"
    elif system in {"Linux", "Darwin"}:  # Darwin = macOS
        driver_path = base_dir / "chromedriver"
    return driver_path.resolve()
