#NAME- OFORKA JESSE CHINAZOR
#Email- jae.rozan@gmail.com

#Phone repair basic test
print ("Faulty Phone Test")
print('This is test allows you run diagnostics on your device to determine device faults and possible solution. \n')
dev = input('Please enter device model \n-Infinix \n-Tecno \n-Itel \n-Gionee \n-Bonitel \n-Innjoo \n')
rep = input('What issues have you observed on your device? \n(a)White/Black LCD \n(b)Low screen sensitivity \n(c)Bootloop \n(d)Non-responsive screen \n(e)Others \n')
if (rep.lower() == "a"):
    print('Dead screen-  Change Screen')
else:
    if (rep.lower() == "b"):
        print('OS problem- Flash new OS File')
    else:
        if (rep.lower() == "d"):
            print('Faulty touchpad- Replace touchpad')
        else:
            if (rep.lower() == "c"):
                print('Low RAM/Too many Apps- Reboot, uninstall unnessary apps and do not clear Apps after use')
            else:
                if (rep.lower() == "e"):
                    print('Well need more Technical checks to get solution \n  THANK YOU \n')
