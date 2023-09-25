# Description

The provided Python script is designed to assist in the enumeration of subdomains for a specified target host by leveraging DNS (Domain Name System) queries. This script can be particularly useful in cybersecurity and network reconnaissance activities. Let's break down its functionality:

    Importing DNS Resolver Library:
    The script begins by importing the dns.resolver library, which is essential for performing DNS queries, including domain name resolution to IP addresses.

    Input for the Target Host:
    Users are prompted to input the target host, typically a domain name. The script uses the input function to receive this input and stores it in the host variable.

    Setting the DNS Query Type:
    The script sets the DNS query type to "A" using the tp variable. This type corresponds to querying for address records (A records) which translate domain names to IP addresses.

    Reading Subdomains from a Text File:
    The script opens and reads the contents of a text file located at "/home/kali/sublist.txt." Each line in this file is considered a subdomain, and these subdomains are stored in the subdominios list.

    Iterating Through Subdomains and Performing DNS Queries:
        For each subdomain in the subdominios list, the script enters a try-except block.
        Inside the try block, it combines the subdomain with the target host to create a complete domain name (sub_alvo).
        It then uses the dns.resolver object (res) to perform a DNS query for the sub_alvo domain using the specified query type (tp).
        If the DNS query is successful and returns results, the script prints the subdomain and the associated IP address.

The primary goal of this script is to automate the process of discovering subdomains associated with a target domain name. This can be a valuable step in security assessments, as it helps identify potential entry points or vulnerabilities in a network. However, it's essential to use this script responsibly and ethically, as unauthorized and excessive use of DNS queries can be disruptive and potentially illegal. Always ensure that you have proper authorization and adhere to legal and ethical guidelines when conducting such activities.
