candy=["Lollipop", "Mint", "Toffee", "Gum", "Snickers", "Jelly Bean"]
skipped_count=0
for c in candy:
    if c=="Gum":
        skipped_count+=1
        continue
        print("I dont want gum")
    

    if c=="Snickers":
        break
        print(f'I found snickers')