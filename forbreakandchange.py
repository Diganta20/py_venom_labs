for i in range(15):
    print(i)                    #break aftr print, skips the loop after 10, so 10 is printed
    if i==10:
     break


for i in range(15):
   if i==10:
      break
   print("new1:",i)                    #break before print, skips the loop before 10, so 10 is not printed


for i in range(15):
    print("new2:",i)                        #continue after print , skips the iteration after 10, so 10 is printed
    if i==10:
        continue
    
for i in range(15):
    if i==10:
        continue
    print("new3:",i)                        #continue before print  , skips the iteration after 10, so 10 is not printed