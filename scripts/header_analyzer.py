from email import policy
from email.parser import BytesParser

from pathlib import Path

file_path = Path(
    "/home/kali/Nexora-OSINT/headers/simulated_phishing.eml"
)

with open(file_path, "rb") as file:

    message = BytesParser(
        policy=policy.default
    ).parse(file)


print("\n===== EMAIL HEADER ANALYSIS =====")

headers = [
    "From",
    "To",
    "Reply-To",
    "Return-Path",
    "Subject",
    "Received",
    "Authentication-Results"
]

for header in headers:

    values = message.get_all(header, [])

    print(f"\n{header}:")

    if values:

        for value in values:
            print(value)

    else:

        print("Not present")


print("\n===== SENDER CONSISTENCY CHECK =====")

from_header = message.get("From")
reply_to = message.get("Reply-To")
return_path = message.get("Return-Path")

print("From:", from_header)
print("Reply-To:", reply_to)
print("Return-Path:", return_path)

if reply_to:

    print("\nWARNING: Reply-To requires verification.")

if return_path:

    print("Return-Path requires envelope verification.")

print("\n===== AUTHENTICATION RESULTS =====")

auth = message.get("Authentication-Results")

if auth:

    print(auth)

else:

    print("No authentication results available.")

print("\n===== ANALYSIS COMPLETE =====")
