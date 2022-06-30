import os
import cv2
import time
from xml.dom import minidom
 
name_dict = {'0': 'background', '1': 'open', '2': 'short',
             '3': 'mousebite', '4': 'spur', '5': 'copper', '6': 'pin-hole'}
 
 
def transfer_to_xml(pic, txt, file_name,xml_save_path):
    if not os.path.exists(xml_save_path):
        os.makedirs(xml_save_path,exist_ok=True)
 
    img = cv2.imread(pic)
    img_w = img.shape[1]
    img_h = img.shape[0]
    img_d = img.shape[2]
    doc = minidom.Document()
 
    annotation = doc.createElement("annotation")
    doc.appendChild(annotation)
    folder = doc.createElement('folder')
    folder.appendChild(doc.createTextNode('visdrone'))
    annotation.appendChild(folder)
 
    filename = doc.createElement('filename')
    filename.appendChild(doc.createTextNode(file_name))
    annotation.appendChild(filename)
 
    source = doc.createElement('source')
    database = doc.createElement('database')
    database.appendChild(doc.createTextNode("Unknown"))
    source.appendChild(database)
 
    annotation.appendChild(source)
 
    size = doc.createElement('size')
    width = doc.createElement('width')
    width.appendChild(doc.createTextNode(str(img_w)))
    size.appendChild(width)
    height = doc.createElement('height')
    height.appendChild(doc.createTextNode(str(img_h)))
    size.appendChild(height)
    depth = doc.createElement('depth')
    depth.appendChild(doc.createTextNode(str(img_d)))
    size.appendChild(depth)
    annotation.appendChild(size)
 
    segmented = doc.createElement('segmented')
    segmented.appendChild(doc.createTextNode("0"))
    annotation.appendChild(segmented)
 
    with open(txt, 'r') as f:
        lines = [f.readlines()]
        for line in lines:
            for boxes in line:
                box = boxes.strip('\n')
                box = box.split(" ")
                x_min = box[0]
                y_min = box[1]
                x_max = box[2]
                y_max = box[3]
                object_name = name_dict[box[4]]
                if object_name != "background":
                    object = doc.createElement('object')
                    nm = doc.createElement('name')
                    nm.appendChild(doc.createTextNode(object_name))
                    object.appendChild(nm)
                    pose = doc.createElement('pose')
                    pose.appendChild(doc.createTextNode("Unspecified"))
                    object.appendChild(pose)
                    truncated = doc.createElement('truncated')
                    truncated.appendChild(doc.createTextNode("1"))
                    object.appendChild(truncated)
                    difficult = doc.createElement('difficult')
                    difficult.appendChild(doc.createTextNode("0"))
                    object.appendChild(difficult)
                    bndbox = doc.createElement('bndbox')
                    xmin = doc.createElement('xmin')
                    xmin.appendChild(doc.createTextNode(x_min))
                    bndbox.appendChild(xmin)
                    ymin = doc.createElement('ymin')
                    ymin.appendChild(doc.createTextNode(y_min))
                    bndbox.appendChild(ymin)
                    xmax = doc.createElement('xmax')
                    xmax.appendChild(doc.createTextNode(str(x_max)))
                    bndbox.appendChild(xmax)
                    ymax = doc.createElement('ymax')
                    ymax.appendChild(doc.createTextNode(str(y_max)))
                    bndbox.appendChild(ymax)
                    object.appendChild(bndbox)
                    annotation.appendChild(object)
                    with open(os.path.join(xml_save_path, file_name + '.xml'), 'w') as x:
                        x.write(doc.toprettyxml())
                    x.close()
    f.close()
 
 
if __name__ == '__main__':
    t = time.time()
    print('Transfer .txt to .xml...ing....')
    txt_folder = 'data/PCBDatasets/txt'
    txt_file = os.listdir(txt_folder)
    img_folder = 'data/PCBDatasets/images'
    xml_save_path = 'data/PCBDatasets/xml/'
 
    for txt in txt_file:
        txt_full_path = os.path.join(txt_folder, txt)
        img_full_path = os.path.join(img_folder, txt.split('.')[0] + '_temp.jpg')
 
        try:
            transfer_to_xml(img_full_path, txt_full_path, txt.split('.')[0],xml_save_path)
        except Exception as e:
            print(e)
 
    print("Transfer .txt to .XML sucessed. costed: {:.3f}s...".format(time.time() - t))