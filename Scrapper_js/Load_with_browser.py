from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
def setUpFirefoxProfile():
    profile = webdriver.FirefoxProfile('C:/Users/Rubens/AppData/Roaming/Mozilla/Firefox/Profiles/evernmfu.default')
    profile.set_preference("browser.download.folderList", 2);
    profile.set_preference("browser.download.dir", "C:\Users\Rubens\Downloads\smsniff");
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip"); #Se puede ver en el Network
    driver = webdriver.Firefox(profile)
    return driver
driver = setUpFirefoxProfile()
driver.get('http://eportal.mapama.gob.es/websiar/SeleccionParametrosMap.aspx?dst=1')
#for value_ccaa in range(2,53):
value_ccaa=11
value_ccaa_string = str(value_ccaa)
string_ccaa = 'select[name="ctl00$ContentPlaceHolder1$DropDownListProvincia"] option[value="'+value_ccaa_string+'"]'
desplegable_ccaa = driver.find_element_by_css_selector(string_ccaa)
click_desplegable_ccaa = desplegable_ccaa.click()
time.sleep(0.3)
agregar_estacion = driver.find_element_by_css_selector('input[name="ctl00$ContentPlaceHolder1$ButtonAgregar"]')
click_agregar_estacion=agregar_estacion.click()
time.sleep(0.3)
consultar_datos_button = driver.find_element_by_css_selector('input[name="ctl00$ContentPlaceHolder1$btnConsultar"]')
consultar_datos = consultar_datos_button.click()
time.sleep(2)
driver.switch_to_window(driver.window_handles[1])
exportar_csv_link = driver.find_element_by_css_selector('a[id="ContentPlaceHolder1_ExportarCSV"]')
descargar_csv = exportar_csv_link.click()
driver.close()

#Pre-requsitos. Meter en anaconda2, geckodriver.exe