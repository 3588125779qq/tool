import os
ip1=0
ip2=0
ip3=0
ip4=0
a=1
while a==1:
 ip=str(ip4) + "." + str(ip3) + "." + str(ip2) + "." + str(ip1)
 ip1=ip1+1
 if ip1==255:
  ip1=0
  ip2=ip2+1
 if ip2==255:
  ip2=0
  ip3=ip3+1
 if ip3==255:
  ip3=0
  ip4=ip4+1
 print(ip)
 os.system("curl -s https://ip.cn/ip/" + str(ip) + ".html | grep tab0_address") 