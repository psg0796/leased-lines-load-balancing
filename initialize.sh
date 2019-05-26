#reference
#http://linux-ip.net/html/adv-multi-internet.html?fbclid=IwAR0i5B-OX1a2BQFwO5PGJLX4RDty3Y5cUnypt8ESUbmY-fZkjwkCyM38VAw
#https://lartc.org/howto/lartc.rpdb.multiple-links.html?fbclid=IwAR0c_RELSMMMmDEWm4efPzVOIwdsTDhIOxBdGsgyj2Hwsku9VQu-eA1yugo
#https://serverfault.com/questions/93678/load-balancing-nat-ing-multiple-isp-connections-on-linux?fbclid=IwAR1_GGBzyj2-eODkTUQFwiLW6trel7aadMHxvdZFL_Lkj7S23Bc7Yiw8Oo4

#creating table ISP1 using default table
ip route show table main | grep -Ev '^default' \
   | while read ROUTE ; do
     ip route add table ISP1 $ROUTE
done

ip route add default via $P1 table ISP1


#creating table ISP2 using default table

ip route show table main | grep -Ev '^default' \
   | while read ROUTE ; do
     ip route add table ISP2 $ROUTE
done

ip route add default via $P2 table ISP1

# ip route add default via $P2 table ISP1
#marking packet
iptables -t mangle -A PREROUTING -j CONNMARK --restore-mark
iptables -t mangle -A PREROUTING -m mark ! --mark 0 -j ACCEPT
iptables -t mangle -A PREROUTING -j MARK --set-mark 10

#here we are doing random load balancing
#50% probability of packet to via line 2
iptables -t mangle -A PREROUTING -m statistic --mode random --probability 0.5 -j MARK --set-mark 20
iptables -t mangle -A PREROUTING -j CONNMARK --save-mark

#natting
iptables -t nat -A POSTROUTING -o $IF1 -j MASQUERADE
iptables -t nat -A POSTROUTING -o $IF2 -j MASQUERADE
