from selenium import webdriver
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Instalação automática do ChromeDriver
chromedriver_autoinstaller.install()

# Configuração das opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")

# Inicialização do Display Virtual (Xvfb)
display = Display(visible=0, size=(1920, 1080))
display.start()


class FullScreenScreenshot:
    """Class to take a screenshot of an entire page"""

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)

    def take_screenshot(self, filename="screenshot.png") -> None:
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.get_screenshot_as_file(filename)
            print(f"Captura de tela da página '{self.url}' salva como '{filename}'")
            self.close_browser()
        except Exception as e:
            self.close_browser()
            print(f"Erro ao tirar a captura de tela: {str(e)}")

    def close_browser(self) -> None:
        self.driver.quit()
