hosts = ["workstation.local", "192.168.23.44"], ["webserver.cloud", "10.23.45.2"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
