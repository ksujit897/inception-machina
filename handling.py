try:

    f = open("abc.txt")

    p = 44445
    b = 76476

    p = b / 0




    for line in f:
        print(line)

except FileNotFoundError as e:
    print(e.filename)

except Exception as e:
    print(e)


#i = 0/0
# We added it here just for fun
