#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, time
import smtplib
import urllib2
from bs4 import BeautifulSoup
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from selenium import webdriver
import os
from os import listdir
import os.path
import pdfkit

# Set the MOZ_HEADLESS environment variable which casues Firefox to start in headless mode.
#os.environ['MOZ_HEADLESS'] = '1'
hour_start= time.time()
print 'Start script: ',time.ctime(hour_start), '\n'

if os.path.exists("salida.html"):
	os.remove("salida.html")
else:
	pass



#*********
#Paloalto
#*********

print ("Ingresando a PALO ALTO NETWORKS"), '\n'

url_paloalto_sele= 'https://securityadvisories.paloaltonetworks.com/'

navegador= webdriver.Firefox()
navegador.get(url_paloalto_sele)
navegador.save_screenshot('paloalto1.png')
navegador.quit()

vulnerabilities = open('salida.html', 'a')
vulnerabilities.write("<!DOCTYPE html>")
vulnerabilities.write("<html lang='es-ES'>")
vulnerabilities.write("	<head>")
vulnerabilities.write("		<meta charset='utf-8'>")
vulnerabilities.write("	</head>")
vulnerabilities.write("	<body>")
vulnerabilities.write("		<header><h1 align='center'>REPORTE DE VULNERABILIDADES</h1></header>")
vulnerabilities.write("		<p><b>PALO ALTO NETWORKS</b><br>****************************<br></p>")
vulnerabilities.write("		<img src='paloalto1.png' alt='Paloalto'/><br><br>")
vulnerabilities.close()


if os.path.exists("fileCVE.txt" and "seclists.txt"):
	
	url_paloalto = urllib2.urlopen("https://securityadvisories.paloaltonetworks.com/")

	source_code = BeautifulSoup(url_paloalto, 'html.parser')
	

	for paloaltonum in range(0,3):

		titulo_paloalto			= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[0].text
		id_paloalto				= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[1].text
		severidad_paloalto		= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[2].text
		afectado_paloalto		= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[3].text
		publicado_paloalto		= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[4].text
		actualizado_paloalto 	= source_code('table')[1].findAll('tr')[int(paloaltonum)].findAll('td')[5].text



		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<p><b>Title</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + titulo_paloalto.strip() + '</p>')
		vulnerabilities.write('		<p><b>Id</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + id_paloalto.strip() + '</p>')
		vulnerabilities.write('		<p><b>Severity</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + severidad_paloalto.strip() + '</p>')
		vulnerabilities.write('		<p><b>Affected</b>&nbsp;&nbsp;&nbsp;&nbsp;:' + afectado_paloalto.strip().encode('utf-8') + '</p>')
		vulnerabilities.write('		<p><b>Published</b>&nbsp;:' + publicado_paloalto.strip() + '</p>')
		vulnerabilities.write('		<p><b>Update</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + actualizado_paloalto.strip() + '<br><br></p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()

		

	#***********
	# Checkpoint
	#***********

	print ("Ingresando a CHECKPOINT"), '\n'


	url_checkpoint= 'https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsecurityalerts='

	navegador= webdriver.Firefox()
	navegador.get(url_checkpoint)

	time.sleep(3)

	navegador.save_screenshot("checkpoint1.png")
	navegador.quit()

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write("		<p><b>CHECKPOINT</b><br>****************<br></p>")
	vulnerabilities.write("		<img src='checkpoint1.png' alt='Checkpoint'/><br><br>")
	vulnerabilities.close()


	for checkpointnum in range(1,4):

		url_checkpoint= 'https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsecurityalerts='

		navegador= webdriver.Firefox()
		navegador.get(url_checkpoint)

		time.sleep(3)

		campo_redireccion = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div[3]/div[3]/div[2]/div[2]/table/tbody/tr[' + str(checkpointnum) + ']/td/div/a')
		redireccion = campo_redireccion.click()

		campo_nombre = navegador.find_element_by_xpath("//*[@id='solutionTitleDiv']")
		nombre = campo_nombre.text

		campo_id = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[1]/td[2]")
		idc = campo_id.text

		campo_severidad = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[2]/td[2]")
		severidad = campo_severidad.text

		campo_producto = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[3]/td[2]")
		producto = campo_producto.text

		campo_version = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[4]/td[2]")
		version = campo_version.text

		campo_created = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[5]/td[2]")
		created = campo_created.text

		campo_modified = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div[2]/div[4]/table/tbody/tr[6]/td[2]")
		modified = campo_modified.text

		navegador.quit()

		time.sleep(3)


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<p><b>Name</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + nombre.strip() + '</p>')
		vulnerabilities.write('		<p><b>Id</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + idc.strip() + '</p>')
		vulnerabilities.write('		<p><b>Severity</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + severidad.strip() + '</p>')
		vulnerabilities.write('		<p><b>Product</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + producto.strip() + '</p>')
		vulnerabilities.write('		<p><b>Version</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + version.strip() + '</p>')
		vulnerabilities.write('		<p><b>Created</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + created.strip() + '</p>')
		vulnerabilities.write('		<p><b>Modified</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + modified.strip() + '</p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()



	#***************
	#Cisco Firepower
	#***************

	print ("Ingresando a CISCO (FIREPOWER)"), '\n'

	url_cisco_firepower= 'https://tools.cisco.com/security/center/publicationListing.x?product=Cisco&keyword=FIREPOWER&sort=-day_sir#~Vulnerabilities'

	navegador= webdriver.Firefox()
	navegador.get(url_cisco_firepower)
	time.sleep(3)
	navegador.save_screenshot("cisco_firepower1.png")
	navegador.quit()

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>CISCO (FIREPOWER)</b><br>************************<br></p>")
	vulnerabilities.write("		<img src='cisco_firepower1.png' alt='Cisco_firepower'/><br><br>")
	vulnerabilities.close()

	for cisco in range(1,4):

		url_cisco_firepower= 'https://tools.cisco.com/security/center/publicationListing.x?product=Cisco&keyword=FIREPOWER&sort=-day_sir#~Vulnerabilities'

		navegador= webdriver.Firefox()
		navegador.get(url_cisco_firepower)

		campo_redireccion = navegador.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/div/div[1]/div[2]/table/tbody[2]/tr[' + str(cisco) + ']/td/table/tbody/tr[1]/td[1]/div/span[4]/a')
		redireccion = campo_redireccion.click()

		campo_nombre = navegador.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div/div/div[1]/h1[2]")
		nombre = campo_nombre.text

		campo_estado = navegador.find_element_by_xpath("//*[@id='severitycirclecontent']")
		estado = campo_estado.text

		campo_advisoryId = navegador.find_element_by_xpath("//*[@id='divpubidvalue']")
		advisoryId = campo_advisoryId.text

		campo_lastPublished = navegador.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]")
		lastPublished = campo_lastPublished.text

		campo_lastUpdate = navegador.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[2]")
		lastUpdate = campo_lastUpdate.text

		campo_version = navegador.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div[2]")
		version = campo_version.text

		campo_workarounds = navegador.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[5]/div[2]")
		workarounds = campo_workarounds.text

		navegador.quit()


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<p><b>Name</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + nombre.strip() + '</p>')
		vulnerabilities.write('		<p><b>Estate</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + estado.strip() + '</p>')
		vulnerabilities.write('		<p><b>AdvisoryId</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + advisoryId.strip() + '</p>')
		vulnerabilities.write('		<p><b>Last Published</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + lastPublished.strip() + '</p>')
		vulnerabilities.write('		<p><b>Last Update</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + lastUpdate.strip() + '</p>')
		vulnerabilities.write('		<p><b>Version</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + version.strip() + '</p>')
		vulnerabilities.write('		<p><b>Workarounds</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + workarounds.strip() + '</p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()



	#**********************
	#CVEDETAILS (FIREPOWER)
	#**********************

	print ("Ingresando a CVEDETAILS (FIREPOWER)"), '\n'

	url_cve_firesight= 'https://www.cvedetails.com/vulnerability-list/vendor_id-16/product_id-31534/Cisco-Firesight-System-Software.html'

	navegador= webdriver.Firefox()
	navegador.get(url_cve_firesight)
	navegador.save_screenshot("cve_firesight1.png")
	navegador.quit()


	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>CVEDETAILS (FIREPOWER)</b><br>*******************************<br></p>")
	vulnerabilities.write("		<img src='cve_firesight1.png' alt='cve_firesight'/><br><br>")
	vulnerabilities.close()


	for cisco_firesight in range(2,7,2):

		url_cve_firesight= 'https://www.cvedetails.com/vulnerability-list/vendor_id-16/product_id-31534/Cisco-Firesight-System-Software.html'

		navegador= webdriver.Firefox()
		navegador.get(url_cve_firesight)


		campo_cve_id = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div[5]/table/tbody/tr[' + str(cisco_firesight) + ']/td[2]/a')
		cve_id = campo_cve_id.text

		campo_vulnerabilityType = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div[5]/table/tbody/tr[' + str(cisco_firesight) + ']/td[5]')
		vulnerabilityType = campo_vulnerabilityType.text

		campo_publishDate = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div[5]/table/tbody/tr[' + str(cisco_firesight) + ']/td[6]')
		publishDate = campo_publishDate.text

		campo_updateDate = navegador.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/div/div[5]/table/tbody/tr[' + str(cisco_firesight) + ']/td[7]')
		updateDate = campo_updateDate.text

		navegador.quit()


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<p><b>CVE Id</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + cve_id.strip() + '</p>')
		vulnerabilities.write('		<p><b>Vulnerability Type</b>&nbsp;&nbsp;:' + vulnerabilityType.strip() + '</p>')
		vulnerabilities.write('		<p><b>Publish Date</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + publishDate.strip() + '</p>')
		vulnerabilities.write('		<p><b>Update Date</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + updateDate.strip() + '<br></p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()


	
	#******************************************
	#CVE - Common Vulnerabilities and Exposures
	#******************************************

	print ("Ingresando a CVE - Common Vulnerabilities and Exposures"), '\n'

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>CVE - Common Vulnerabilities and Exposures</b><br>****************************************************<br></p>")
	vulnerabilities.close()

	cves = open('fileCVE.txt', 'r')
	line = cves.readline()
	for line in cves:

		url_site= 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=' + str(line)

		navegador= webdriver.Firefox()
		navegador.get(url_site)
		navegador.save_screenshot(str(line).strip() + '1.png')



		campo_cve_name = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[1]/a")
		cve_name = campo_cve_name.text

		time.sleep(1)

		campo_cve_description = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]")
		cve_description = campo_cve_description.text

		navegador.quit()


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<img src=' + "'" + str(line) + '1.png' + "'" + '/><br><br>')
		vulnerabilities.write('		<p><b>CVE Name</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + cve_name.strip() + '</p>')
		vulnerabilities.write('		<p><b>CVE Description</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + cve_description.strip() + '<br><br></p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()



	#**********
	#EXPLOIT DB
	#**********

	print ("Ingresando a EXPLOIT DB"), '\n'

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>EXPLOITDB</b><br>**************<br></p>")
	vulnerabilities.close()

	exploitdb = open('fileCVE.txt', 'r')
	line = exploitdb.readline()
	for line in exploitdb:

		url_site_exploit= 'https://www.exploit-db.com/'

		navegador= webdriver.Firefox()
		navegador.get(url_site_exploit)

		time.sleep(3)

		campo_buscar_exploit = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/label/input")
		campo_buscar_exploit.send_keys(line)
		
		time.sleep(3)

		navegador.save_screenshot(str(line).strip() + '2.png')


		campo_exploit1_date = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]")
		exploit1_date = campo_exploit1_date.text

		if exploit1_date == "No matching records found":
			navegador.quit()
			continue

		campo_exploit1_title = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[5]/a")
		exploit1_title = campo_exploit1_title.text

		campo_exploit1_type = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[6]/a")
		exploit1_type = campo_exploit1_type.text

		campo_exploit1_platform = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[1]/td[7]/a")
		exploit1_platform = campo_exploit1_platform.text

		navegador.quit()


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<img src=' + "'" + str(line) + '2.png' + "'" + '/><br><br>')
		vulnerabilities.write('		<p><b>Date</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + exploit1_date.strip() + '</p>')
		vulnerabilities.write('		<p><b>Title</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + exploit1_title.strip() + '</p>')
		vulnerabilities.write('		<p><b>Type</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + exploit1_type.strip() + '</p>')
		vulnerabilities.write('		<p><b>Platform</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + exploit1_platform.strip() + '<br></p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()



	#**********
	#SECLISTS
	#**********

	print ("Ingresando a SECLISTS"), '\n'

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>SECLISTS</b><br>************<br></p>")
	vulnerabilities.close()


	seclists = open('seclists.txt', 'r')
	line = seclists.readline()
	for line in seclists:

		url_site_google= 'https://www.google.com/'

		navegador= webdriver.Firefox()
		navegador.get(url_site_google)

		time.sleep(3)

		campo_buscar_google = navegador.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div/div[1]/input")
		campo_buscar_google.send_keys(line)

		time.sleep(3)

		campo_boton_google = navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div/div[3]/center/input[1]')
		boton = campo_boton_google.click()

		time.sleep(3)

		campo_herramientas_google = navegador.find_element_by_xpath('//*[@id="hdtb-tls"]')
		herramientas = campo_herramientas_google.click()

		time.sleep(2)

		campo_filtro_google = navegador.find_element_by_xpath('/html/body/div[6]/div[3]/div[5]/div/div/div[2]/div/div[3]/div')
		filtro = campo_filtro_google.click()

		campo_filtro24_google = navegador.find_element_by_xpath('/html/body/div[6]/div[3]/div[5]/div/div/div[2]/div/ul[2]/li[3]/a')
		filtro24 = campo_filtro24_google.click()

		time.sleep(1)

		navegador.save_screenshot(str(line).strip() + '3.png')

		navegador.quit()


		vulnerabilities = open('salida.html', 'a')
		vulnerabilities.write('		<img src=' + "'" + str(line) + '3.png' + "'" + '/><br><br>')
		vulnerabilities.write('		<p><b>Criterio de Busqueda</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + str(line).strip() + '<br><br></p>')
		vulnerabilities.write('		<hr>')
		vulnerabilities.close()



	#**********
	#VMWARE
	#**********

	print ("Ingresando a VMWARE"), '\n'

	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write('		<p><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>')
	vulnerabilities.write("		<p><b>VMWARE</b><br>**********<br></p>")
	vulnerabilities.close()

	url_site_vmware= 'https://www.vmware.com/security/advisories.html'

	navegador= webdriver.Firefox()
	navegador.get(url_site_vmware)

	campo_vmware_principal = navegador.find_element_by_xpath('/html/body/div[4]/div[7]/div/div[2]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div/a')
	vmware_principal = campo_vmware_principal.click()

	navegador.save_screenshot("vmware.png")

	campo_vmware_advisoryId = navegador.find_element_by_xpath("/html/body/div[4]/div[7]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[1]/div[2]")
	vmware_advisoryId = campo_vmware_advisoryId.text

	campo_vmware_severity = navegador.find_element_by_xpath("/html/body/div[4]/div[7]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]")
	vmware_severity = campo_vmware_severity.text

	campo_vmware_issue = navegador.find_element_by_xpath("/html/body/div[4]/div[7]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[4]/div[2]")
	vmware_issue = campo_vmware_issue.text

	campo_vmware_cve = navegador.find_element_by_xpath("/html/body/div[4]/div[7]/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[6]/div[2]")
	vmware_cve = campo_vmware_cve.text

	navegador.close()


	vulnerabilities = open('salida.html', 'a')
	vulnerabilities.write("		<img src='vmware.png' alt='vmware'/><br><br>")
	vulnerabilities.write('		<p><b>Advisory Id</b>&nbsp;&nbsp;&nbsp;&nbsp;:' + vmware_advisoryId.strip() + '</p>')
	vulnerabilities.write('		<p><b>Severity</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + vmware_severity.strip() + '</p>')
	vulnerabilities.write('		<p><b>Issue</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + vmware_issue.strip() + '</p>')
	vulnerabilities.write('		<p><b>CVE</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:' + vmware_cve.strip() + '<br></p>')
	vulnerabilities.write('		<hr>')
	vulnerabilities.close()


else:
	print ("El archivo 'fileCVE.txt o seclists.txt' No existe")


#***********
# Crear PDF
#***********

print ("Creando informe"), '\n'

options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}

pdfkit.from_file('salida.html', 'reporte_vulnerabilidades.pdf', options=options)

print ('\n')


#************************
#Renombrando archivo(PDF)
#************************

fecha_hoy = time.strftime("%d%m%y")
os.rename("reporte_vulnerabilidades.pdf", "Reporte_Vulnerabilidades_" + fecha_hoy + ".pdf")



#*******************
#Correo electronico
#*******************

print ("Enviando correo electronico"), '\n'
#enviarCorreo():
fromaddr = "example@example.com"
recipients = "example@example.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = ", ".join(recipients)
msg['Subject'] = "Reporte de vulnerabilidades diarias"

body = "Este correo se genera de forma automatica, favor no responder."

msg.attach(MIMEText(body, 'plain'))

filename = "Reporte_Vulnerabilidades_" + fecha_hoy + ".pdf"
attachment = open("Reporte_Vulnerabilidades_" + fecha_hoy + ".pdf", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "your password")
text = msg.as_string()
server.sendmail(fromaddr, recipients, text)
server.quit()



#***************************
#Elimina archivos temporales
#***************************
print ("Eliminando archivos temporales"), '\n'

os.remove("salida.html")
for archivos in listdir("."):
	if archivos.endswith(".png"):
		os.remove(os.path.join(archivos))



hour_finally= time.time()
print 'Finally script: ',time.ctime(hour_finally), '\n'
