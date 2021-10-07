#librerias de envio

import smtplib,ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time as t

velas = {
    "1": "Muñeco de nieve, precio:10.000$",
    "2": "Santa, precio:10.000$",
    "3": "Caballero , precio: 10.000$",
    "4": "Corazon , precio: 10.000$",
}
#Correo gmail y contraseña del remitente 
username = ""
password =  ""

#Ingresar asunto del correo y correo gmail destinatario
destinario = input("Ingrese el correo del destinatario:")
asunto = "Recibo de vela"

#Datos fundamentales del destinatario
Nombre = input("Nombre del comprador: ")
numero = input("Digita el numero de celular del comprador: ")
direccion = input("Escribe la dirreccion del comprador: ")
orden = input("Digita el numero de orden que quieres: ")

#Estructura Html del correo

mensaje = MIMEMultipart("alternative")
mensaje["subject"] = asunto
mensaje["From"] = username
mensaje["To"] = destinario
               
                
html = f"""
<html>
<body>
        <p>*******************</p>
        <p>Hola {destinario}<br>
        <p> EMPRESA : SECLES </p>
        <p> Nombre del combrador: {Nombre}</p>
        <p> Celular : {numero}</p>
        <p> Direccion: {direccion}</p>
        <p>{t.strftime("%H:%M:%S")}</p>
        <p>{t.strftime("%d/%m/%y")}</p>
        {(orden == "1"):}
        ===> producto: #1, vela muñeco de nieve 10.000$ //
        {(orden == "2"):}
        ===> producto: #2, vela de navidad 10.000$ //
        {(orden == "3"):}
        ===> producto: #3, vela de caballero 10.000$ //
        {(orden == "4"):}
        ===> producto: 4, vela de corazon 10.000$ //
        <p>(El producto marcado por "True"es el producto que escojiste)</p>
        <p>*******************</p>
</body>
</html>
"""
parte_html = MIMEText(html,"html")
mensaje.attach(parte_html)
context = ssl.create_default_context()

#Protocolo para enviar el correo

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        print("Inicia sesion")
        server.sendmail(username, destinario, mensaje.as_string())
        print("Mensaje enviado")
     

        