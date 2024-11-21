from PIL import Image
import os

def process_images(input_folder, output_folder, crop_height=830, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".tiff") or filename.endswith(".tif"):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                # Recortar a imagem
                cropped_img = img.crop((0, 0, img.width, crop_height))
                
                # Converter e reduzir a qualidade
                output_filename = os.path.splitext(filename)[0] + ".jpg"
                output_path = os.path.join(output_folder, output_filename)
                cropped_img.save(output_path, "JPEG", quality=quality)
                print("Imagen redimensionada")

# Caminhos das pastas de entrada e saída
input_folder = './'
output_folder = './'

# Processar as imagens
process_images(input_folder, output_folder)

