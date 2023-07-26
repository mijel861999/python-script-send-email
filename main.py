# Envío de correos electrónicos
import smtplib
#  Esta clase se utiliza para crear mensajes de correo electrónico que pueden contener varias partes, como texto simple y archivos adjuntos.
from email.mime.multipart import MIMEMultipart
# Esta clase se utiliza para representar y adjuntar archivos a los mensajes de correo electrónico.
from email.mime.base import MIMEBase
# Este módulo proporciona funciones para codificar y decodificar datos binarios, lo que es útil cuando se adjuntan archivos a un correo electrónico.
from email import encoders
# Permite crear tareas que se ejecuten repetidamente o en momentos específicos.
import schedule
# El módulo time proporciona funciones relacionadas con el tiempo, como medir lapsos, pausar la ejecución, etc.
import time
#  ReportLab es una biblioteca de Python para la creación y generación de documentos PDF.
from reportlab.lib.pagesizes import letter
# La clase canvas proporciona una forma de crear y editar documentos PDF, donde puedes dibujar gráficos, agregar texto, imágenes, etc.
from reportlab.pdfgen import canvas