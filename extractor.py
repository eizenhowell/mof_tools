import os
import shutil 
rootfolder = "I:/Games Backup/MOFP/extracted_resources/UI/"
exported_folder = "I:/Games Backup/MOFP/extracted_resources/UI/"

def move_extracted_ravioli (src_folder=rootfolder, trg_folder=exported_folder, filename="/File0001.png", replace_hypens=True):
    for fldr_name in os.listdir(src_folder):
        current_file = src_folder + fldr_name
        for ext_file in os.listdir(current_file):
            filename = ext_file
        current_file = src_folder+fldr_name+"/"+filename

        target_filename = fldr_name.replace('.gi', '')+".png"
        if replace_hypens:
            target_filename = fldr_name.replace("-", "_")
        current_file = src_folder+fldr_name+"/"+filename
        target_file = trg_folder+target_filename

        shutil.move(current_file, target_file)

# Sample function
from PIL import Image, ImageDraw
def splice_and_rejoin(src, map_src):
    with open(map_src) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    map = []
    im = Image.open(src)
    #X,Y.Width,Height,PosX,PosY
    #max_width : 55
    #max_height : 82 (85?)
    row = 0
    img = Image.new('RGBA',(1020, 510), (255, 255, 255, 0))
    if im.mode == 'P':
        img.putpalette( im.palette.getdata()[ 1 ] )
    for idx, coords in enumerate(content):
        region = None
        col = idx % 12 
        if (idx %12 == 0 and idx != 0):
            row += 1
        max_width = 85
        max_height = 85 #82
        coords = coords.split(',')
        print(len(coords))
        if len(coords)!=1:
            x = max_width * col
            y = max_height * row
            #if col != 0: x+=1
            #if row != 0: y+=1
            width = int(coords[2])
            height = int(coords[3])
            offset_x = int(coords[4])
            offset_y = int(coords[5])
            x+=offset_x
            y+=offset_y

            original_x = int(coords[0])+int(coords[4])
            original_y = int(coords[1])+int(coords[5])

            box = (original_x, original_y, original_x+width, original_y+height)
            new_coords = (x, y)
            region = im.crop(box)
            print (idx)
            print(box)
            print(new_coords)
            img.paste(region, new_coords)
    img.save(src, 'PNG')


def create_regular_tileset (src_folder=rootfolder):
    map_loc = "I:/Games Backup/MOFP/extracted_resources/character_map.txt"
    src = "I:/Games Backup/MOFP/extracted_resources/Experiments/0f0003d2_basic boy_01.png"
    for file_name in os.listdir(src_folder):
        #print(file_name)
        splice_and_rejoin(src_folder+"/"+file_name, map_loc)
