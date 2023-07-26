# Dependencias

` pip install smtplib schedule reportlab `

# Codigo de ejemplo - CHAT GPT

```
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import schedule
    import time
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    def crear_pdf(nombre_archivo):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        c.drawString(100, 700, "¡Hola! Este es mi PDF generado automáticamente.")
        c.save()

    def enviar_correo(correo_destino, asunto, cuerpo, archivo_adjunto):
        from_address = "tucorreo@gmail.com"  # Cambia esto a tu dirección de correo
        password = "tucontraseña"  # Cambia esto a tu contraseña

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = correo_destino
        msg['Subject'] = asunto

        msg.attach(MIMEText(cuerpo, 'plain'))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(archivo_adjunto, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {archivo_adjunto}")
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, correo_destino, msg.as_string())
        server.quit()

    def tarea_programada():
        # Crear el PDF
        nombre_archivo_pdf = "archivo_pdf_generado.pdf"
        crear_pdf(nombre_archivo_pdf)

        # Enviar el correo con el archivo adjunto
        destinatario = "destinatario@gmail.com"  # Cambia esto al correo del destinatario
        asunto_correo = "Envío mensual del archivo PDF"
        cuerpo_correo = "¡Hola! Adjunto encontrarás el archivo PDF generado automáticamente."
        archivo_adjunto = nombre_archivo_pdf
        enviar_correo(destinatario, asunto_correo, cuerpo_correo, archivo_adjunto)

    # Programar el envío mensual
    schedule.every().month.do(tarea_programada)

    # Ejecutar el programa continuamente
    while True:
        schedule.run_pending()
        time.sleep(1)
```
