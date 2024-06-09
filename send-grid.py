import os
import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(from_email: str, to_emails: list[str], subject: str, html_content: str, api_key: str) -> None:
    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=html_content
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        logging.info(f"Email sent successfully: {response.status_code}")
        logging.debug(f"Response body: {response.body}")
        logging.debug(f"Response headers: {response.headers}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    from_email = 'your_email@example.com'
    to_emails = ['recipient@example.com']
    subject = 'Email Deliverability Analytics using SendGrid and AWS Big Data Services'
    html_content = '<p>Your HTML content here</p>'
    
    # Fetch API key from environment variable for security
    api_key = os.getenv('SENDGRID_API_KEY')
    
    if not api_key:
        logging.error("SendGrid API key not found. Please set the SENDGRID_API_KEY environment variable.")
    else:
        send_email(from_email, to_emails, subject, html_content, api_key)
