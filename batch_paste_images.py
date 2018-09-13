from PIL import Image
import os

# 存放背景图片的文件夹路径
background_path = "D:/batch_paste_images/background"
# 存放上层图片的文件夹路径
upper_path = "D:/batch_paste_images/upper"
# 存放合成后图片的文件夹路径
pastes_path = "D:/batch_paste_images/pastes"

for upper_name in os.listdir(upper_path):
    upper = Image.open(os.path.join(upper_path, upper_name))
    for background_name in os.listdir(background_path):
        background = Image.open(os.path.join(background_path, background_name))
        # 调整图片大小
        # upper = upper.resize((400, 200), Image.ANTIALIAS)
        # 此处可以定义上层图片的位置，例如：(200, 100)，代表距离左边200，距离顶部100
        background.paste(upper, (100, 100), upper)
        background.save(os.path.join(pastes_path, upper_name.split(".")[0] + "_" + background_name))