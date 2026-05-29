# leep year by using nested condistional statement 

leepyear = int(input(("Enter the leep year :")))

if leepyear  % 4 == 0:
    if leepyear % 100 == 0:
        if leepyear % 400 == 0 :
            print("leepyear")
        else:
            print("year is not an leepyear")
    else:
        print("year is  an leepyear")
else :
    print("year is not an leepyear")
