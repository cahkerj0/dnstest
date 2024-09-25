from scapy.all import *

# Create a malformed DNS query with invalid data
malformed_dns_query = IP(dst="10.1.10.30") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="aaaaaaaaaa.id", qtype=1)) / Raw(load="GET / HTTP/1.1\r\nHost: f5demo.id\r\n\r\nsadasdasdasvvnaksdkasdkadjkjkjkaskdkk")

# Send the malformed packet
send(malformed_dns_query)

# Send the DNS query and receive the response
response = sr1(malformed_dns_query)

# Check if we received a response
if response:
    response.show()
else:
    print("No response received")
