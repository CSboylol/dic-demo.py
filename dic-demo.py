servers = []

for i in range(3):
    name = input(f"Enter the name of server {i+1}: ")
    servers.append(name) 

print(f"The servers you entered are: {servers}")

servers = ["nginx", "docker", "kubernetes"]

server_ips = {}

for server in servers:
    ip = input(f"Enter IP address for {server}: ")
    server_ips[server] = ip

print("\nServer IP Addresses:")
for server, ip in server_ips.items():
    print(f"{server}: {ip}")

server_ips = {
    "nginx": "192.168.1.10",
    "docker": "192.168.1.20",
    "kubernetes": "192.168.1.30"
}

server_name = input("Enter the server name to view its details: ")

if server_name in server_ips:
    print(f"Server: {server_name}, IP: {server_ips[server_name]}")
else:
    print(f"Error: Server '{server_name}' not found in the system.")

server_ips = {
    "nginx": "192.168.1.10",
    "docker": "192.168.1.20",
    "kubernetes": "192.168.1.30"
}

choice = input("Do you want to update the IP address of any server? (yes/no): ")

if choice.lower() == "yes":
    server_name = input("Enter the server name to update: ")

    if server_name in server_ips:
        new_ip = input(f"Enter the new IP address for {server_name}: ")
        server_ips[server_name] = new_ip  
        print("\nUpdated Server IP Addresses:")
        for server, ip in server_ips.items():
            print(f"{server}: {ip}")
    else:
        print(f"Error: Server '{server_name}' not found in the system.")
else:
    print("No changes made to server IP addresses.")