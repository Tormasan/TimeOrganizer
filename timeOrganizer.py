import time

t=time.time()
m=0
h=0

while True:
    time.sleep(1)
    a=time.time()

    s=a-t
    if s >60:
        m=s/60
        s=s%60
        if m>60:
            h=int(m/60)
            m=m%60

    print("%s:%s:%s" %( int(h),int(m),int(s)))

    if int(h) %3==2:
        print("eleg a kockulasbol TANULJ, PROGRAMOZZ CSINALJ VALAMI HASZNOSAT IS !!!")

