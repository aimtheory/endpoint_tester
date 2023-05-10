import csv
import socket
from scapy.layers.inet import traceroute, TCP, IP


def port_open(domain_name, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 80))
    if result == 0:
        status = "open"
    else:
        status = "closed"
    sock.close()

    return status


def get_hops(domain_name):
    result, _ = traceroute(domain_name)
    return min(snd[IP].ttl for snd, _ in result[TCP])


with open('./check_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open('./endpoints.csv', 'r') as read_obj:
        endpoints = csv.reader(read_obj)
        for item in endpoints:
            print(item)

            for item in endpoints:
                writer.writerow([item[0],
                                 port_open(item[0], item[1]),
                                 port_open(item[0], item[2]),
                                 get_hops(item[0])
                                 ])

