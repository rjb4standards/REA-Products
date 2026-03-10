Three PDS files are created that are used to produc three unique DNAID record in SAG-CTR:
1. Entity Information PDS containing Company Name/Entity Name/Entity IDentifier (Business Cyber Guardian/Richard Brooks/Badge Number 1
2. Resource information in PDS containing Company Name/Resource Name/Resource Identifier ((Business Cyber Guardian/SAG-CTR Database/SAGDB)
3. A Zero Trust Bond PDS that represents a Zero Trust Bond record with a unique DNAID using a Zero Trust DomainName/EntityDNAID/ResourceDNAID)


Step 1 perform a risk assessment on the entity PDS and submit the evidence data to SAG-CTR as a trust declaration
Step 2 perform a risk assessment on the resource PDS and submit the evidence data to SAG-CTR as a trust declaration
Step 3. Perform a risk assessment on the Zero Trust Bond PDS and submit the evidence data to SAG-CTR as a Zero Trust Bond declaration

The SAG-CTR Gatekeeper applies Registration Policies provided the by policy owners, i.e. Company Name, that are applied to the submitted trust declarations for entry in SAG-CTR

The Zero Trust Bouncer (ZTB) Gateway that frontends a resoruce performs a checktrust lookup in SAG-CTR using the Zero Trust Bond DNAID to verify trust before allowing access to a resource.
