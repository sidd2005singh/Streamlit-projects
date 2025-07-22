import gradio as gr 
import pywhatkit 
import psutil 
import urllib.parse 
import webbrowser 
from datetime import datetime, timedelta 
from PIL import Image, ImageDraw 
from twilio.rest import Client 
 
# WhatsApp Automation 
def send_whatsapp(number, message, delay_sec): 
    try: 
        future_time = datetime.now() + timedelta(seconds=int(delay_sec)) 
        hour, minute = future_time.hour, future_time.minute 
        pywhatkit.sendwhatmsg(number, message, hour, minute) 
        return f"   Message scheduled to {number} at {hour}:{minute}" 
    except Exception as e: 
        return f"  Error: {str(e)}" 
 
# Email via browser 
def send_email(to, subject, body): 
    try: 
        params = urllib.parse.urlencode({ 
            'to': to, 
            'subject': subject, 
            'body': body 
        }) 
        url = f"https://mail.google.com/mail/?view=cm&fs=1&{params}" 
        webbrowser.open(url) 
        return "           Gmail opened in browser." 
    except Exception as e: 
        return f"  Error: {str(e)}" 
 
# RAM Info 
def ram_info(): 
    mem = psutil.virtual_memory() 
    return f""" 
    Total: {mem.total / (1024 ** 3):.2f} GB 
    Used: {mem.used / (1024 ** 3):.2f} GB 
    Free: {mem.free / (1024 ** 3):.2f} GB 
    Usage: {mem.percent} % 
    """ 
 
# Image generation 
def create_image(): 
    image = Image.new("RGB", (300, 300), "red") 
    draw = ImageDraw.Draw(image) 
    draw.ellipse((110, 110, 190, 190), fill="blue") 

    path = "generated_image.png" 
    image.save(path) 
    return path 
    
# Twilio SMS 
def send_sms(sid, token, from_no, to_no, msg): 
    try: 
        client = Client(sid, token) 
        message = client.messages.create(body=msg, from_=from_no, to=to_no) 
        return f"   SMS sent! Message SID: {message.sid}" 
    except Exception as e: 
        return f"  Error: {str(e)}" 
 
# Interface blocks 
with gr.Blocks(title="Automation Panel using Gradio") as demo: 
    gr.Markdown("##          Automation Panel") 
 
    with gr.Tab("1 WhatsApp"): 
        number = gr.Textbox(label="Phone Number (+91...)") 
        message = gr.Textbox(label="Message") 
        delay = gr.Slider(30, 300, label="Delay in Seconds") 
        btn1 = gr.Button("Send Message") 
        output1 = gr.Textbox() 
        btn1.click(send_whatsapp, [number, message, delay], output1) 
 
    with gr.Tab("2 Email"): 
        to = gr.Textbox(label="To") 
        subject = gr.Textbox(label="Subject") 
        body = gr.Textbox(label="Body") 
        btn2 = gr.Button("Open Gmail") 
        output2 = gr.Textbox() 
        btn2.click(send_email, [to, subject, body], output2) 
 
    with gr.Tab("3 RAM Info"): 
        btn3 = gr.Button("Check RAM Usage") 
        output3 = gr.Textbox() 
        btn3.click(ram_info, outputs=output3) 
 
    with gr.Tab("4 Image Generator"): 
        btn4 = gr.Button("Generate Image") 
        output4 = gr.Image() 
        btn4.click(create_image, outputs=output4) 
 
    with gr.Tab("5 Send SMS (Twilio)"): 
        sid = gr.Textbox(label="Twilio SID", type="password") 
        token = gr.Textbox(label="Twilio Token", type="password") 
        from_no = gr.Textbox(label="Twilio Number") 
        to_no = gr.Textbox(label="Recipient Number") 
        msg = gr.Textbox(label="Message") 
        btn5 = gr.Button("Send SMS") 
        output5 = gr.Textbox()
        btn5.click(send_sms, [sid, token, from_no, to_no, msg], output5) 

demo.launch()