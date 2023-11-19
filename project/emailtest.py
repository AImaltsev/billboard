import smtplib
from email.mime.text import MIMEText

# Ваши настройки почты
email_host = 'smtp.gmail.com'
email_port = 587
email_host_user = 'boomer47.am@gmail.com'
email_host_password = 'vzll fqyz enpw qzkc'
use_starttls = True

# Создаем объект SMTP
server = smtplib.SMTP(email_host, email_port)

# Включаем STARTTLS, если не используется SSL
if use_starttls:
    server.starttls()

# Включаем вывод отладочной информации
server.set_debuglevel(1)

# Аутентификация
server.login(email_host_user, email_host_password)

# Отправляем тестовое письмо
from_email = 'boomer47.am@gmail.com'
to_email = 'boomer47@yandex.ru'
subject = 'Тестовое письмо'
body = 'Привет, это тестовое письмо.'

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

server.sendmail(from_email, [to_email], msg.as_string())

# Закрываем соединение
server.quit()
