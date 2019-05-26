sysctl -w net.ipv4.ip_forward=1 #enabling forwarding

#defining tables for both ISPs
echo "10 ISP1" >> /etc/iproute2/rt_tables
echo "20 ISP2" >> /etc/iproute2/rt_tables
