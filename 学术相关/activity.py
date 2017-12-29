def spec_activity():
    i=1
    while i:
         Qh=eval(input("enter Qh(A*V): "))
         R=0.02
         s=Qh/R*1000000/210
         I=eval(input("enter I(A): "))
         Id=eval(input("enter Id(A): "))
         Ik=1/(1/I-1/Id)
         spec_activity=Ik/s*1000
         print ('specific activity(mA/cm2): {}'.format(spec_activity))
         print ('ECSA(cm2)= {}'.format(s))
         i=eval(input("continue(0/1):"))
    print "over!"

spec_activity()
