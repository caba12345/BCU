from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import smtplib
from email.message import EmailMessage

def rezerva_loc():
    MAX_RETRIES = 10

    options = Options()
    options.add_experimental_option("detach", True)

    retry_count = 0
    driver = None
    while retry_count < MAX_RETRIES:
        try:
            driver = webdriver.Chrome(service=Service("E:\\chromedriver-win64\\chromedriver.exe"), options=options)
            driver.get("http://aleph.bcucluj.ro:8991/F/?func=file&file_name=login-session")
            driver.maximize_window()

            txtBarcod = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "bor_id")))
            txtBarcod.send_keys("BCU202313295")

            txtParola = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "bor_verification")))
            txtParola.send_keys("BCU202313295")

            btnLogin = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[4]/td/input")
            btnLogin.click()

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/table[2]/tbody/tr/td[2]/a"))).click()

            rezervari = driver.find_elements(By.LINK_TEXT, "rezervare")

            # Cautam Locul
            loc_element = rezervari[0].find_element(By.XPATH, "../following-sibling::td[@class='td1']")
            loc_text = loc_element.text

            # Trimitem email cu locul
            send_email(loc_text)

            rezervari[0].click()

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/table/tbody/tr[6]/td/input"))).click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/ html / body / form / table / tbody / tr[5] / td / input"))).click()
            # Dacă totul merge bine, ieși din buclă
            break

        except TimeoutException:
            print("Timeout: Pagina nu s-a încărcat într-un timp rezonabil. Se încearcă din nou...")
        except NoSuchElementException as e:
            print("Elementul nu a fost găsit:", e)
        except Exception as e:
            print("A apărut o eroare:", e)
        finally:
            retry_count += 1
            print("Gata")
            if driver:
                driver.quit()  # Închidem driverul pentru a pregăti o nouă încercare

    if retry_count == MAX_RETRIES:
        print("Nu s-a putut încărca pagina după", MAX_RETRIES, "încercări.")


def send_email(loc_text):
    # Adresa și parola pentru trimiterea email-ului
    SENDER_EMAIL = "..." # Adresa de email de unde se trimite email-ul
    SENDER_PASSWORD = "..." # Parola pentru adresa de email de unde se trimite email-ul

    # Adresa de email a destinatarului
    RECIPIENT_EMAIL = "..."  # Adresa ta de email

    # Crează mesajul email
    msg = EmailMessage()
    msg.set_content(f"Ai rezervat urmatorul loc: {loc_text}")

    msg['Subject'] = 'REZERVARE LOC BCU'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    # Trimite email-ul
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.send_message(msg)

rezerva_loc()