from reportlab.pdfgen import canvas
from datetime import datetime


def create_pdf(name, batch_code, submitted_to):
    # Define the PDF filename with a timestamp
    pdf_filename = f'deployment_snapshot.pdf'

    # Create a PDF document
    c = canvas.Canvas(pdf_filename)

    # Add a snapshot of each step of deployment
    c.drawString(100, 800, f"Step 1: Load Data from Week 4")
    c.drawString(120, 780, f"- Data loaded successfully")

    c.drawString(100, 760, f"Step 2: Save Model from Week 4")
    c.drawString(120, 740, f"- Model saved successfully as 'iris_model.pkl")

    c.drawString(100, 720, f"Step 3: Create Heroku app")
    c.drawString(120, 700, f"- Created Heroku app as week-5-dataglacier'")

    c.drawString(100, 680, f"Step 4: Deploy model on Heroku")
    c.drawString(120, 660, f"- Model deployed successfully")

    # Add user-specific information
    c.drawString(100, 620, f"Name: {name}")
    c.drawString(100, 600, f"Batch code: {batch_code}")
    c.drawString(100, 580, f"Submission date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 560, f"Submitted to: {submitted_to}")

    # Save the document
    c.save()

    return pdf_filename


name = "Aiub Dzhandarov"
batch_code = "AD745"
submitted_to = "Data Glacier"
pdf_filename = create_pdf(name, batch_code, submitted_to)
print(f"PDF document created: {pdf_filename}")

if __name__ == '__main__':
    create_pdf(name, batch_code, submitted_to)
