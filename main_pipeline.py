import os
import smtplib
from email.message import EmailMessage
import google.generativeai as genai
from groq import Groq

# Cấu hình API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.environ["EMAIL_USERNAME"]
    msg['To'] = os.environ["EMAIL_USERNAME"] # Gửi cho chính bạn

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ["EMAIL_USERNAME"], os.environ["EMAIL_PASSWORD"])
        smtp.send_message(msg)

def run_research_pipeline():
    # 1. Giả định lấy dữ liệu (Bạn có thể tích hợp Apify ở đây)
    raw_data = "Nội dung 100 triệu từ hoặc danh sách transcript..."
    
    # 2. Dùng Gemini 1.5 Flash để tóm tắt và viết báo cáo (Free & Fast)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Bạn là chuyên gia Y sinh & AI. Hãy viết báo cáo nghiên cứu định kỳ từ dữ liệu sau: {raw_data}"
    
    response = model.generate_content(prompt)
    report_content = response.text

    # 3. Gửi báo cáo về Gmail
    send_email("BÁO CÁO NGHIÊN CỨU AI ĐỊNH KỲ", report_content)
    print("Đã gửi báo cáo về Gmail thành công!")

if __name__ == "__main__":
    run_research_pipeline()
