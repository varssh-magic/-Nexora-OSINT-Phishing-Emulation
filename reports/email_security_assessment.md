# Nexora Technologies
## Email Security Assessment

### 1. SPF Analysis

SPF record:
v=spf1 ip4:192.168.56.10 -all

Assessment:
Only the specified lab IP is authorized by this policy.
Other sending IPs should fail SPF evaluation.

### 2. DMARC Analysis

Initial policy:
v=DMARC1; p=none

Assessment:
Monitoring policy without requested DMARC enforcement.

Updated policy:
v=DMARC1; p=reject

Assessment:
Requests rejection of messages failing DMARC.

### 3. DKIM Analysis

Initial laboratory configuration:
DKIM not configured.

Assessment:
No DKIM signature validation was demonstrated.

### 4. Email Header Analysis

Investigated fields:
- From
- Reply-To
- Return-Path
- Authentication-Results

Finding:
The sample contained inconsistent sender-related information.

### 5. Conclusion

The laboratory demonstrated why sender identity
must be evaluated using authentication results
rather than relying exclusively on the displayed
From field.
