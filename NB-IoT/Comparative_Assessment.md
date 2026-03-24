# Evidence-Based Comparative Assessment

## Secondary-source analysis in place of lab based validation

This comparative assessment will serve the purpose of providing evidence and rigor behind the security posture of NB-IoT compared to RSAEmist.

Because internship equipment was not delivered in time, NB-IoT findings are based on standards review, published security research, and architecture-level comparison rather than lab-test validation. As a result, conclusions on replay resilience and battery impact should be treated as moderate-confidence until verified experimentally.

This assessment will be grounded in:
- Standards
- Vendor Architecture Claims
- Published attack research


## NB-IoT Security Posture Questions:
1. What security controls does NB-IoT inherit by design?
2. Where does NB-IoT still face operational risk?
3. Relative to Mist, where is the evidence stronger, weaker, or still unverified?

NB-IoT will be compared against Mist across:
- identity and authentication
- encryption/integrity
- replay resistance
- resilience to battery/resource exhaustion
- dependency on centralized infrastructure
- mobile asset support
- visibility/logging/forensics
- confidence level of evidence

Rated by score and evidence type:
- High confidence = standards docs, formal specs, peer-reviewed studies
- Medium confidence = vendor whitepapers or product docs
- Low confidence = inferred or marketing-style claims


## Threat-Model Comparison
NB-IoT vs Mist based on concrete attack scenarios:
- passive snooping/eavesdropping
- replay/spoofing of acknowledgments or delivery state
- battery-drain / retry-loop abuse
- compromised gateway or relay behavior
- coverage disruption / interference
- loss of backhaul or upstream connectivity
- device theft / SIM compromise / credential misuse

For each scenario, answer:
- what architectural control exists,
- where the trust boundary sits,
- what the likely impact is,
- and whether the mitigation is native, operator-dependent, or application-dependent.

