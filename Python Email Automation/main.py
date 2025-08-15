import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def load_html_template(company_name):
    with open("Template Email Catalin.html", "r", encoding="windows-1252") as f:
        html = f.read()
        return html.replace("{company_name}", company_name)

def start():
    # Email credentials
    your_email = "catalindanisrospin@gmail.com"
    your_password = "qumo ynbm xaok ribl"

    # List of recipients
    recipients = [
        "compec@compec.ro",
        "office@maxit.ro",
        "relatii_clienti@mega-image.ro",
        "hello@mejix.com",
        "cluj@mhp.com",
        "office@mmmautoparts.ro",
        "corporate@montran.com",
        "info.ro@nagarro.com",
        "office@nanolabs.ro",
        "office@napocasoftware.ro",
        "ni.romania@ni.com",
        "cluj@brinel.ro",
        "info@netmatch.ro",
        "office@neusoft.ro",
        "office@nightbuild.com",
        "office@nordlogic.com",
        "office.norstal@gmail.com",
        "office@novcom.swiss",
        "ro.nttdata@nttdata.com",
        "information@oreilly.co.uk",
        "publicrelations@opentext.com"
    ]

    company_names = [
        "marquardt",
        "MaXit",
        "Mega Image",
        "Mejix",
        "MHP",
        "MMM Autoparts",
        "Montran",
        "Nagarro",
        "nanolabs electronics",
        "Napoca Software",
        "National Instruments",
        "Net Brinel SA",
        "NetMatch",
        "Neusoft EDC",
        "NightBuild",
        "Nordlogic",
        "norstal",
        "novcom solutions",
        "NTT Data",
        "O'Reilly",
        "OpenText"
    ]

    # Email content
    subject = "Join Us in Empowering the Future of Space-Tech – ROSPIN Event Sponsorship Opportunity"

    # Connect to Gmail's SMTP server using TLS
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(your_email, your_password)

        for i in range(len(recipients)):
            # Create a new email for each recipient
            message = MIMEMultipart()
            message["From"] = your_email
            message["To"] = recipients[i]
            message["Subject"] = subject
            body = load_html_template(company_names[i])
            message.attach(MIMEText(body, "html"))

            print(f"Company: {company_names[i]}, Email: {recipients[i]}")
            print("Enter NO to stop the app, enter CONTINUE to jump over")
            userInput = input("Press anything to continue >> ")
            if (userInput == "NO"):
                exit(0)
            if (userInput == "CONTINUE"):
                continue

            server.sendmail(your_email, recipients[i], message.as_string())
            print()

if __name__ == '__main__':
    start()