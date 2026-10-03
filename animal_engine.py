import os
from google import genai

client = genai.Client()

def generate_universal_animal_behavior(visual_description):
    prompt = f"""
    คุณคือนักชีววิทยา วิวัฒนาการ และนักบรรพชีวินวิทยา (Paleontologist) ผู้เชี่ยวชาญด้านกายพฤติกรรมของสิ่งมีชีวิตทั้งในยุคปัจจุบันและยุคโบราณ
    ผู้ใช้พบเห็นสัตว์ (หรือซากดึกดำบรรพ์/ไดโนเสาร์) ที่มีลักษณะดังนี้: "{visual_description}"

    จงวิเคราะห์และอธิบายพฤติกรรมหรือลักษณะทางนิเวศวิทยาออกมาเป็นภาษาไทยที่อ่านง่าย โดยต้องครอบคลุมประเด็นเหล่านี้:
    1. ลักษณะการเคลื่อนไหวและกายภาพ (Locomotion & Physical Structure)
    2. พฤติกรรมการกินอาหารและการล่าเหยื่อ (Diet & Foraging Strategy)
    3. ถิ่นที่อยู่อาศัยและบทบาทในระบบนิเวศ (Habitat & Ecological Niche)
    """
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    return response.text
