Three PDS files are created that are used to produc three unique ZTDNAID record in SAG-CTR:
1. Entity Information PDS containing Company Name/Entity Name/Entity IDentifier (Business Cyber Guardian/Richard Brooks/Badge Number 1
2. Resource information in PDS containing ZeroTrustDomainName/Resource Name/Resource Identifier (Business Cyber Guardian AWS-RDS/SAG-CTR Database/SAGDB)
3. A Zero Trust Bond PDS that represents a Zero Trust Bond record with a unique DNAID using a Zero Trust DomainName/EntityDNAID/ResourceDNAID)


Step 1 perform a risk assessment on the entity PDS and submit the evidence data to SAG-CTR as a trust declaration
Step 2 perform a risk assessment on the resource PDS and submit the evidence data to SAG-CTR as a trust declaration
Step 3. Perform a risk assessment on the Zero Trust Bond PDS and submit the evidence data to SAG-CTR as a Zero Trust Bond declaration

The SAG-CTR Gatekeeper applies Registration Policies provided the by policy owners, i.e. Company Name, that are applied to the submitted trust declarations for entry in SAG-CTR

The Zero Trust Bouncer (ZTB) Gateway that frontends a resoruce performs a checktrust lookup in SAG-CTR using the Zero Trust Bond DNAID to verify trust before allowing access to a resource.

Its very easily to implement a checktrust() function in python using the example checktrust.py code which can be called using:
checktrust(ZTTrustDomain, ZTEntityDNAID, ZTResourceDNAID, delimeter)
[checktrust.py Function Source Code](https://github.com/rjb4standards/REA-Products/blob/master/ZeroTrust/checktrust.py)

Refer to ztdnaid URI scheme Internet Draft for details describing ZTDANIDs;
[ZTDNAID Internet Draft](https://www.ietf.org/archive/id/draft-brooks-ztdnaid-new-02.txt)

Example usage:
checktrust("MYZTdomainName", "ENTITY ZTDNAID HEX VALUE ONLY", "RESOURCE ZTDNAID HEX VALUE ONLY", "|")
resulting in the ZTBOND DNAID for:

"MYZTdomainName"|"ENTITY ZTDNAID HEX VALUE ONLY"|"RESOURCE ZTDNAID HEX VALUE ONLY"

This ZTBOND DNAID is then used to performa lookup in SAG-CTR, using the SAG-CTR Lookup URL.
A True response indicate an Entity ZTDNAID is trusted to access the reuqest Resource ZTDNAID.
i.e.  url = f"{ZTBcfg.get_sag_ctr_lookup_url()}{ztbond_dnaid}"


Additional examples are provided in the [ZTDNAID Internet Draft](https://www.ietf.org/archive/id/draft-brooks-ztdnaid-new-01.txt)

