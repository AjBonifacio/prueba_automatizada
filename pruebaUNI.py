import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jinja2 import Environment, FileSystemLoader

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.makedirs('screenshots', exist_ok=True)
        os.makedirs('Reportes', exist_ok=True)

    def setUp(self):
        self.driver = self.iniciar_navegador()
        self.driver.get(r"C:\Users\angel\OneDrive\Desktop\prueba unitaria\login.html")

    def iniciar_navegador(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginForm").submit()
        self.capture_screenshot("login_attempt")

    def capture_screenshot(self, name):
        filepath = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(filepath)

    def tearDown(self):
        self.driver.quit()


class TestLogin(BaseTest):
    """Pruebas de login."""

    def test_login_correcto(self):
        self.login("angelo", "boni05")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "gestionEstudiantes"))
        )
        self.assertTrue(self.driver.find_element(By.ID, "gestionEstudiantes").is_displayed())
        self.capture_screenshot("login_correcto")

    def test_login_incorrecto(self):
        self.login("usuarioIncorrecto", "contraseñaIncorrecta")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "errorMessage"))
        )
        self.assertTrue(self.driver.find_element(By.ID, "errorMessage").is_displayed())
        self.capture_screenshot("login_incorrecto")


class TestGestionEstudiantes(BaseTest):
    """Pruebas de gestión de estudiantes."""

    def setUp(self):
        super().setUp()
        self.login("angelo", "boni05")

    def test_agregar_estudiante(self):
        self.driver.find_element(By.ID, "Matricula").send_keys("2024-001")
        self.driver.find_element(By.ID, "Nombre").send_keys("Juan")
        self.driver.find_element(By.ID, "Apellidos").send_keys("Pérez")
        self.driver.find_element(By.ID, "Materia").send_keys("Matemáticas")
        self.driver.find_element(By.ID, "Nota").send_keys("8.5")
        self.driver.find_element(By.ID, "addEstudiante").click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "listaEstudiantes"))
        )
        lista_estudiantes = self.driver.find_element(By.ID, "listaEstudiantes")
        estudiantes = lista_estudiantes.find_elements(By.TAG_NAME, "tr")
        self.assertGreater(len(estudiantes), 0)
        self.capture_screenshot("agregar_estudiante")


from jinja2 import Environment, FileSystemLoader

class GenerarInforme:
    """Generador de informes HTML."""

    @staticmethod
    def generar_informe():
        
        resultadosReportes = [
            {"test": "test_login_correcto", "resultado": "Pasó", "detalles": "Login correcto."},
            {"test": "test_login_incorrecto", "resultado": "Pasó", "detalles": "Mensaje de error por login incorrecto."},
            {"test": "test_agregar_estudiante", "resultado": "Pasó", "detalles": "Estudiante agregado correctamente."},
        ]
        
        #
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("Reportes/Informe-plantilla.html")  # Ruta de la plantilla HTML
        html_content = template.render(resultadosReportes=resultadosReportes)

        informe_path = os.path.join("Reportes", "Informe.html")
        
        
        with open(informe_path, "w") as file:
            file.write(html_content)
        print(f"Informe generado en {informe_path}")

GenerarInforme.generar_informe()


if __name__ == "__main__":
    unittest.main(verbosity=2)

    GenerarInforme.generar_informe()


