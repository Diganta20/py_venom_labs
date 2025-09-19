candy=["Lollipop", "Mint", "Toffee", "Gum", "Snickers", "Jelly Bean"]
skipped_count=0
for c in candy:
    if c=="Gum":
        skipped_count+=1
       
        print("I dont want gum")
        continue
    
    if c=="Snickers":
       
        print(f'I found:',c)
        break
    else:
        print("Searching for snicker but it is:",c)

