from PIL import Image
import os
import shutil

# 存放背景图片的文件夹路径
background_path = "D:/batch_paste_images/background"
# 存放上层图片的文件夹路径
upper_path = "D:/batch_paste_images/upper"
# 存放合成后图片的文件夹路径
pastes_path = "D:/batch_paste_images/pastes"

for upper_name in os.listdir(upper_path):
    upper = Image.open(os.path.join(upper_path, upper_name))
    if os.path.exists(os.path.join(pastes_path, upper_name)):
        shutil.rmtree(os.path.join(pastes_path, upper_name))
    os.mkdir(os.path.join(pastes_path, upper_name))
    for background_name in os.listdir(background_path):
        background = Image.open(os.path.join(background_path, background_name))
        # 调整图片大小
        # upper = upper.resize((1000, 1000), Image.ANTIALIAS)
        # 此处可以定义上层图片的位置，例如：(200, 100)，代表距离左边200，距离顶部100
        background.paste(upper, (0, 0), upper)
        # quality最大值为100，值越大图片精度越高。或者设置为PNG格式（质量好，图片较大）
        background.save(os.path.join(pastes_path + "/" + upper_name + "/" + upper_name.split(".")[0] + "_" + background_name), quality = 95)