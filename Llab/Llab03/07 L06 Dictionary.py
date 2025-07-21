x = {"arm":{1:"n",2:"แขน"}, "hello":{1:"v",2:"สวัสดี"}, "beautiful":{1:"adj",2:"สวย"}, "toilet":{1:"n",2:"ห้องน้ำ"}, 
     "kick":{1:"v",2:"เตะ"}, "handsome":{1:"adj",2:"หล่อ"}
     }

while True:
    word = input().strip()
    num = int(input().strip())
    if num == "":
        print("Word not in dictionary.")
    else:
        if word in x:
            if num in x[word]:
                print(f"{x[word][num]}")
