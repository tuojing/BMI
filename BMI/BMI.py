height = input ('請輸入您的身高(cm): ')
weight = input ('請輸入您的體重(kg): ')
weight = float(weight)
height = float(height) / 100
BMI = weight / (height * height)
if BMI < 18.5:
    print('您的BMI值為:', BMI, '屬體重過輕')
elif BMI >= 18.5 and BMI < 24:
    print('您的BMI值為:', BMI, '屬正常範圍')
elif BMI >= 24 and BMI < 27:
    print('您的BMI值為:', BMI, '稍重')
elif BMI >= 27 and BMI < 30:
    print('您的BMI值為:', BMI, '輕度肥胖')
elif BMI >= 30 and BMI < 35:
    print('您的BMI值為:', BMI, '中度肥胖')
else:
    print('您的BMI值為:', BMI, '重度肥胖')
