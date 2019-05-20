ip route show table main | grep -Ev '^default' \
   | while read ROUTE ; do
     ip route add table ISP1 $ROUTE
done

ip route add default via $P1 table ISP1


ip route show table main | grep -Ev '^default' \
   | while read ROUTE ; do
     ip route add table ISP2 $ROUTE
done

ip route add default via $P2 table ISP1

# ip route add default via $P2 table ISP1

iptables -t mangle -A PREROUTING -j CONNMARK --restore-mark
iptables -t mangle -A PREROUTING -m mark ! --mark 0 -j ACCEPT
iptables -t mangle -A PREROUTING -j MARK --set-mark 10
iptables -t mangle -A PREROUTING -m statistic --mode random --probability 0.5 -j MARK --set-mark 20
iptables -t mangle -A PREROUTING -j CONNMARK --save-mark

iptables -t nat -A POSTROUTING -o $IF1 -j MASQUERADE
iptables -t nat -A POSTROUTING -o $IF2 -j MASQUERADE
