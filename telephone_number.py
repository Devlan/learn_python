#coding:UTF-8
#在移动、联通、电信的号段中
#纯数字
CN_mobile = \
        [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700]
#1.长度不少于11位
number_input = raw_input("Enter your number :")
number_three = int((number_input[:3]))
number_four = int((number_input[:4]))
if len(number_input) != 11:
    print("Inwalid length,your number should be in 11 digits")
else:
    if number_three in CN_mobile or number_four in CN_mobile:
            print("Operator : China Mobile")
            print("We're sending verification code via text to your phone: %s"%number_input)
    elif number_three in CN_union or number_four in CN_union:
            print("Operator : China Mobile")
            print("We're sending verification code via text to your phone: %s"%number_input)
    elif number_three in CN_telecom or number_four in CN_telecom:
            print("Operator : China Telecom")
            print("We're sending verification code via text to your phone: %s"%number_input)
    else:
        print("No such a operator")
