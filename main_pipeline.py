import os
import smtplib
from email.message import EmailMessage
from google import genai
from groq import Groq

# Khởi tạo Client theo chuẩn SDK mới
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = os.environ["EMAIL_USERNAME"]
    msg['To'] = os.environ["EMAIL_USERNAME"]

    # Lưu ý: EMAIL_PASSWORD phải là App Password 16 ký tự
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ["EMAIL_USERNAME"], os.environ["EMAIL_PASSWORD"])
        smtp.send_message(msg)

def run_research_pipeline():
    # Giả định dữ liệu nghiên cứu
    raw_data = "Nội dung 100 triệu từ hoặc danh sách transcript về Y sinh & AI..."
    
    # Sử dụng model gemini-1.5-flash với cấu trúc gọi hàm mới
    prompt = f"Bạn là chuyên gia Y sinh & AI. Hãy viết báo cáo nghiên cứu định kỳ từ dữ liệu sau: {raw_data}"
    
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=prompt,
    )
    report_content = response.text

    # Gửi báo cáo
    send_email("BÁO CÁO NGHIÊN CỨU AI ĐỊNH KỲ", report_content)
    print("Đã gửi báo cáo về Gmail thành công!")

if __name__ == "__main__":
    run_research_pipeline()
