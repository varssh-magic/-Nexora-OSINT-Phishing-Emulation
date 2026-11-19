
# Nexora Technologies – OSINT Footprinting to Targeted Phishing Emulation

## Project Overview

This project demonstrates an end-to-end OSINT footprinting and controlled phishing-emulation workflow using a fictional organization named Nexora Technologies.

The project explores how publicly available information, DNS records, employee-role information, and email security configurations can be examined to understand an organization's potential exposure to phishing threats.

All activities use a controlled lab environment and synthetic identities.

## Objectives

- Perform OSINT reconnaissance using SpiderFoot and theHarvester.
- Identify and document domain and subdomain information.
- Enumerate DNS records using dig, nslookup, and dnsrecon.
- Examine SPF and DMARC email security configurations.
- Create a synthetic employee dataset.
- Develop a controlled phishing email simulation.
- Analyze raw email headers using Python.
- Map relevant activities to MITRE ATT&CK.
- Prepare an OSINT target dossier and phishing simulation report.

## Lab Environment

| Component | Details |
|---|---|
| Analyst OS | Kali Linux |
| Virtualization | Oracle VirtualBox |
| Organization | Nexora Technologies |
| Test Domain | nexora.test |
| Reconnaissance | SpiderFoot, theHarvester |
| DNS Tools | dig, nslookup, dnsrecon |
| Graph Analysis | Maltego |
| Programming | Python |
| Email Analysis | Python email parser |
| Framework | MITRE ATT&CK |

## Project Structure

- recon/ – OSINT reconnaissance results
- dns/ – DNS enumeration and email security analysis
- employees/ – Synthetic employee dataset
- phishing/ – Controlled phishing simulation files
- headers/ – Raw email and header analysis
- reports/ – Final assessment reports
- scripts/ – Supporting scripts
- evidence/ – Screenshots and evidence index

## Methodology

### Phase 1: Reconnaissance and Footprinting
- Domain reconnaissance
- Subdomain enumeration
- DNS enumeration
- Synthetic employee profiling
- Attack surface documentation

### Phase 2: Phishing Emulation and Header Analysis
- Simulated HR-themed email
- Local-only training portal
- Email header inspection
- SPF and DMARC assessment

### Phase 3: Reporting and MITRE ATT&CK Mapping
- Asset inventory
- Employee dossier
- Email security assessment
- Phishing simulation report
- MITRE ATT&CK technique mapping

## Safety and Scope

This is an educational, controlled cybersecurity lab.

- Nexora Technologies is fictional.
- nexora.test is used as a reserved test domain.
- Employee identities and email addresses are synthetic.
- No real credentials are collected.
- No phishing emails are sent to real users.
- No unauthorized systems are scanned.
- The training portal is intended for local testing only.

## Disclaimer

This repository is intended for educational and authorized cybersecurity testing only. The tools and techniques demonstrated must not be used against systems or individuals without permission.
