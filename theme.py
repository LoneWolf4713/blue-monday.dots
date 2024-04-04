with open("/home/prtyksh/.config/waybar/config.jsonc") as f:
    data = f.read()
    ncolor1 = ""
    ncolor2 = ""
    with open("/home/prtyksh/.config/waybar/colors.txt") as colors:
        color1 = colors.readline().strip()
        color2 = colors.readline().strip()

        print(color1,color2)

        with open("/home/prtyksh/.cache/wal/py") as new:
            ncolor1 = new.readline().strip()
            ncolor2 = new.readline().strip()


            print(ncolor1,ncolor2)

            data = data.replace(color1,ncolor1)
            data = data.replace(color2,ncolor2)

            with open("/home/prtyksh/.config/waybar/config.jsonc","w") as wr:
                wr.write(data)
    
    with open("/home/prtyksh/.config/waybar/colors.txt","w") as w:
        w.write(ncolor1+"\n")
        w.write(ncolor2)
