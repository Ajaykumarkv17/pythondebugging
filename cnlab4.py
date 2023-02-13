
# Import libraries
import dns.resolver
  
# Finding A record
result = dns.resolver.query('instagram.com', 'A')
  
# Printing record
for val in result:
    print('A Record : ', val.to_text())