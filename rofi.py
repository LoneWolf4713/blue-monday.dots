import os

def generate_gallery(folder):
    # Generate HTML for the gallery
    html = f'''<!DOCTYPE html>
    <html>
    <head>
        <title>Image Gallery</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #111;
                color: #fff;
            }}
            .gallery-container {{
                display: grid;
                grid-auto-flow: dense;
                gap: 10px;
                padding: 20px;
                justify-content: center;
                border: 2px solid #fff;
                border-radius: 10px;
                margin: 20px auto;
                max-width: 800px;
            }}
            .gallery-item {{
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
                transition: transform 0.2s;
                cursor: pointer; /* Add cursor pointer to indicate clickability */
            }}
            .gallery-item:hover {{
                transform: scale(1.1);
            }}
        </style>
    </head>
    <body>
        <div class="gallery-container">
    '''
    
    # Get list of image files sorted by modification date in reverse order
    image_files = sorted((os.path.join(root, file) for root, _, files in os.walk(folder) for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))), key=os.path.getmtime, reverse=True)
    
    # Add image thumbnails to the gallery
    for image_path in image_files:
        image_relative_path = image_path.split("/home/prtyksh/Wallpapers/")[1]
        html += f'<img class="gallery-item" src="{image_relative_path}" alt="{os.path.basename(image_path)}" onclick="sendAjaxRequest(\'{image_relative_path}\')">\n'
    
    html += '''</div>
    <script>
        function sendAjaxRequest(imageHref) {
            var xhr = new XMLHttpRequest();
            var url = 'http://localhost:8000/?query=' + encodeURIComponent(imageHref);
            xhr.open('GET', url, true);
            xhr.send();
        }
    </script>
    </body>
    </html>'''

    return html

# Define the folder containing the images
folder_path = "/home/prtyksh/Wallpapers"

# Generate the gallery HTML
gallery_html = generate_gallery(folder_path)

# Write the HTML to a file
with open("gallery.html", "w") as f:
    f.write(gallery_html)

print("Gallery generated successfully.")

