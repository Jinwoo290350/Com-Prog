x = {"arm":{1:"n",2:"แขน"}, "hello":{1:"v",2:"สวัสดี"}, "beautiful":{1:"adj",2:"สวย"}, "toilet":{1:"n",2:"ห้องน้ำ"}, 
     "kick":{1:"v",2:"เตะ"}, "handsome":{1:"adj",2:"หล่อ"}
     }

while True:
    word = input().strip()
    if word == "0":
        break
    elif word in x:
        while True:
            num_input = input().strip()
            if num_input.isdigit():
                number = int(num_input)
                if number == 0:
                    break
                elif number in x[word]:
                    print(f"{x[word][number]}")
                    break
                else:
                    print("Invalid option.")
            else:
                print("Invalid option.")
    else:
        print("Word not in dictionary.")

#การใช้ dictionary และการรับinput แบบ loop กับ dictionary