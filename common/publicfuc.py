def GetWriteCode():
    '''
    调用接口请求验证码，保存到本地，识别验证，检查识别的验证码对不对。
    '''
    filename = 'getCaptcha.jpg'  # 定义的验证码的名字
    url = hurl + "/file/getCaptcha1"  # 获取验证码的接口地址
    headers = {  # 接口所需参数
        'content-type': "application/json;charset=utf-8",
        'fr': "6",
        'http-cust-oid': "988"
        }
    hcode = 'b0a3dc8f-c0d4-475d-9c1a-eb41370bf4bf'  # 获取验证码需要的参数
    # print("???????")
    try:
        # print(hcode)
        querystring = {"w": "100", "h": "38", "code": hcode}  # 传入对于的headers数据
        response = requests.request("GET", url, headers=headers, params=querystring)  # 发送请求
        # print(response.text)
        img = response.content  # 二进制保存验证码
        with open(file_home+filename, 'wb') as f:  # 保存到上面定义的路径
            f.write(img)
            # print("OK")
        image = Image.open(file_home+filename)  # 读取验证码图片
        optCode = pytesseract.image_to_string(image)  # 开始识别验证码
        assert len(optCode) == 4  # 判断是不是四位数
        print(optCode)  # 打印出验证码
        # print("-----------------------------")
        return optCode
    except:
        return GetWriteCode()  # 递归