
# DNS Enumeration

## Objective
Examine DNS records for the Nexora Technologies lab domain.

## Tools
- dig
- nslookup
- dnsrecon

## Records Examined
- A
- NS
- MX
- TXT
- SPF
- DMARC

## Commands Used

```bash
dig @127.0.0.1 nexora.test A
dig @127.0.0.1 nexora.test MX
dig @127.0.0.1 nexora.test TXT
dig @127.0.0.1 _dmarc.nexora.test TXT

nslookup nexora.test 127.0.0.1
nslookup -type=MX nexora.test 127.0.0.1

dnsrecon -d nexora.test -n 127.0.0.1 -t std
```

## Results
See dns_records.txt and dns_security_analysis.md.

## Note
These records belong to the local lab and should not be represented as real public DNS findings.
