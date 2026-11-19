from aiosmtpd.controller import Controller
from pathlib import Path

class MailHandler:

    async def handle_DATA(self, server, session, envelope):

        print("Email received")
        print("From:", envelope.mail_from)
        print("To:", envelope.rcpt_tos)

        Path(
            "/home/kali/Nexora-OSINT/headers/received.eml"
        ).write_bytes(envelope.original_content)

        print("Email saved locally")

        return "250 Message accepted for lab analysis"


controller = Controller(
    MailHandler(),
    hostname="127.0.0.1",
    port=1025
)

controller.start()

print("Local SMTP sink running on 127.0.0.1:1025")

input("Press Enter to stop the server...")

controller.stop()
