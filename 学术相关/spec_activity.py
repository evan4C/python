def spec_activity():
    i=1
    while i:
         Qh=float(input("enter Qh(A*V): "))
         R=0.02
         s=Qh/R*1000000/210
         I=float(input("enter I(A): "))
         Id=float(input("enter Id(A): "))
         Ik=1/(1/I-1/Id)
         spec_activity=Ik/s*1000
         print "specific activity(mA/cm2): ",spec_activity
         print "ECSA(cm2)= ",s
         i=input("continue(0/1):")
    print "over!"

spec_activity()
