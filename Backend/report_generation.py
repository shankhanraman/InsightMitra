from reportlab.lib.pagesizes import letter
from reportlab.pdfgenmport canvas
import os

def generate_report():
    report_path = "business_report.pdf"
    c = canvas.Canvas(report_path, pagesize=letter)
    c.drawString(100, 750, "Business Analysis Report")
    c.drawString(100, 730, "Here are the insights generated for your query:")
    
    # Sample content - Replace with actual analysis
    c.drawString(100, 710, "- Revenue increased by 15% last quarter.")
    c.drawString(100, 690, "- Customer satisfaction remains high.")
    
    c.save()
    return report_path
