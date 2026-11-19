import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["From"] = "Nexora HR <hr@nexora.test>"
msg["To"] = "priya.sharma@nexora.test"
msg["Reply-To"] = "training@example.invalid"

msg["Subject"] = "Important: Employee Benefits Portal Update"

msg.set_content(
    "This is a controlled cybersecurity training simulation."
)

with smtplib.SMTP("127.0.0.1", 1025) as server:

    server.send_message(
        msg,
        from_addr="bounce@nexora.test",
        to_addrs=["priya.sharma@nexora.test"]
    )

print("Lab email submitted to local SMTP sink.")
