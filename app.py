import cv2 as cv
import numpy as np
import gradio as gr

def nostalji(image):
    image = np.array(image)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray_image

# Gradio arayüzünü oluşturalım
with gr.Blocks() as demo:   
    gr.Markdown("# Görseli siyah beyaza çevir")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin!")

    image_input = gr.Image(type='pil')
    image_output = gr.Image(type='numpy', label="Sonuç Resmi")

     # Bileşenleri fonksiyonla bağla
    btn = gr.Button("Çevir")
    btn.click(fn=nostalji, inputs=image_input, outputs=image_output)
    
# Gradio arayüzü başlat
if __name__ == "__main__":
    demo.launch(share=True)
