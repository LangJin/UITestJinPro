import requests
import pytesseract
from PIL import Image
from selenium import webdriver


def codeapi():
    '''
    调用接口请求验证码，保存到本地，识别验证，检查识别的验证码对不对。
    '''
    # 获取图片的接口地址
    url = "接口地址"
    # headers需要的参数
    headers = None
    # 接口需要的参数
    querystring = {"w": "70", "h": "29"}
    # 发送请求
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    # 接口返回的数据以二进制的方式展示
    img = response.content
    # 选择保存的路径和图片格式
    with open('F:\MyPython\TestCode\data\code.jpg', 'wb') as f:
        # 保存
        f.write(img)
    # 用Image模块打开上一步保存的验证码
    image = Image.open('F:\MyPython\TestCode\data\code.jpg')
    # 识别验证码
    optCode = pytesseract.image_to_string(image)
    # 打印出验证码
    print("验证码：", optCode)


def codeimg():
    '''
    调用接口请求验证码，保存到本地，识别验证，检查识别的验证码对不对。
    '''
    driver = webdriver.Chrome()
    # 打开有验证码的界面
    driver.get("https://www.XXXX.com/login")
    # 比较好理解、截图并保存到这个路径
    driver.get_screenshot_as_file('F:/VScode/LoarRunner/Vcode/homepage.png')
    # 打开刚刚保存的图片
    im = Image.open('F:/VScode/LoarRunner/Vcode/homepage.png')
    # 设置要裁剪的区域（验证码所在的区域）
    box = (1214, 82, 1285, 111)
    # 截图，生成只有验证码的图片
    region = im.crop(box)
    # 保存到本地路径
    region.save("F:/VScode/LoarRunner/Vcode/image_code.jpg")
    # 读取验证码图片
    image = Image.open("F:/VScode/LoarRunner/Vcode/image_code.jpg")
    # 开始识别验证码
    optCode = pytesseract.image_to_string(image)
    # 打印出验证码
    print(optCode)
