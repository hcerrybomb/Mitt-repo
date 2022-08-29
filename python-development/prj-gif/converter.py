from msilib.schema import Directory
from PIL import Image
import os
from pathlib import Path

def convert(file, output=""):
    
    filepath = str(file)
    output_path = str(output)
    
    if output_path == "":
        output_path = filepath[:-5]+".gif"
        
    if not output_path.endswith(".gif"):
        
        if not output_path.endswith('\\'):
            
            output_path += "\\"
        
        output_path += "\\output.gif"
        
    image = Image.open(filepath)
    image.info.pop('background', None)
    image.save(output_path, 'gif', save_all = True)
    
    print("\nSuccess. File Created At:",output_path)





def files(directory):
    top_dir = Path(directory)
    
    for item in top_dir.iterdir():

        item_name = str(item)
        item_name = item_name.split("\\")
        item_name = item_name[-1][:len(item_name[-1])-5]

        convert(item, f"C:\\Users\\Gaming_Dator_VII\\Desktop\\gifsOut\\{item_name}.gif")
    
files("C:\\Users\\Gaming_Dator_VII\\Desktop\\webpIn")
