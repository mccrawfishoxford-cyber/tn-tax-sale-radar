import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

TO_EMAIL = os.getenv("TN_TAXSALE_TO_EMAIL")

msg = EmailMessage()
msg["Subject"] = "✅ TN Tax Sale Radar LIVE"
msg["From"] = TO_EMAIL
msg["To"] = TO_EMAIL

msg.set_content(f"""
Your Tennessee Tax Sale AI Agent is LIVE.

Deployment Time:
{datetime.now()}
""")

with smtplib.SMTP(
    os.getenv("TN_TAXSALE_SMTP_HOST"),
    int(os.getenv("TN_TAXSALE_SMTP_PORT"))
) as s:
    s.starttls()
    s.login(
        os.getenv("TN_TAXSALE_SMTP_USER"),
        os.getenv("TN_TAXSALE_SMTP_PASS")
    )
    s.send_message(msg)

print("Radar Email Sent")
