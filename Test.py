name = input("お名前は？")
print("%s さん、こんにちは！" % name)
prompt = name + " > "
while 1:
    answer = input(prompt)
    if answer == "さよなら":
        print("またね！")
        break
    elif not answer:
        print("......")
        break
    print("「{}」うんうん！".format(answer))