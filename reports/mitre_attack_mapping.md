# MITRE ATT&CK Mapping – Nexora Technologies

## 1. Objective

The objective of this mapping is to identify and classify the adversary techniques relevant to the OSINT reconnaissance and targeted phishing emulation conducted against the fictional organization Nexora Technologies.

The MITRE ATT&CK framework is used to understand attacker behaviour and associate the activities demonstrated in the controlled laboratory with documented adversary techniques.

## 2. Technique Mapping

| MITRE ID | Technique | Tactic | Project Activity |
|---|---|---|---|
| T1589 | Gather Victim Identity Information | Reconnaissance | Created a synthetic employee database containing names, roles and email addresses. |
| T1598 | Phishing for Information | Reconnaissance | Examined how a targeted HR-themed phishing message could be used to solicit information. |
| T1566.002 | Spearphishing Link | Initial Access | Created a simulated HR email containing a link to a local training portal. |
| T1583.001 | Acquire Infrastructure: Domains | Resource Development | Studied how domain infrastructure can support phishing campaigns. Used nexora.test as a local test domain. |

## 3. Attack Scenario

An attacker targeting Nexora Technologies could first collect employee information and identify individuals in departments such as HR and IT.

The attacker could then prepare a convincing HR-themed email containing a link to a fraudulent portal. The recipient might be persuaded to visit the page.

In this laboratory, these activities were reproduced using fictional identities, a reserved test domain and a local training portal. No real employees were targeted and no real credentials were collected.

## 4. Defensive Recommendations

- Provide employee phishing awareness training.
- Implement SPF, DKIM and DMARC email authentication.
- Monitor suspicious email headers and sender mismatches.
- Use secure email gateways and URL filtering.
- Restrict access to sensitive internal portals.
- Conduct periodic phishing awareness assessments.

## 5. Conclusion

MITRE ATT&CK mapping helped classify the reconnaissance and phishing-related activities demonstrated in the Nexora laboratory. It provides a structured way to understand attacker behaviour and identify appropriate defensive controls.

All activities were conducted in a controlled environment using fictional information.
