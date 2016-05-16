#!/ur/bin/python

if __name__ =='__main__':
    x=y=999
    max_prod=0
    while x >= 100: 
        while y >= 100:
            print('x: ', x, ' y: ',y)
            prod = x * y
            str_prod= str(prod)
            if str_prod == str_prod[::-1]:
                print('found palindrone: ', prod)
                if prod > max_prod: 
                   max_prod=prod
            y = y-1
        x = x-1
        y = 999

    print(max_prod)
