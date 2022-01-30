'''
Legal Disclaimer
Copyright and all other rights reserved by Reliable Energy Analytics, LLC (REA) 2018-2021. 
Others are free to use this “boilerplate” template under the Creative Commons V4.0 license terms.

DISCLAIMER OF WARRANTIES
TO THE EXTENT NOT PROHIBITED BY LAW, REA HEREBY DISCLAIMS ALL EXPRESS OR IMPLIED REPRESENTATIONS, WARRANTIES, GUARANTEES, AND CONDITIONS OF ANY KIND, ARISING BY LAW OR OTHERWISE, WITH REGARD TO THIS ARTIFACT, INCLUDING BUT NOT LIMITED TO REPRESENTATIONS, WARRANTIES, GUARANTEES, AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, NONINFRINGEMENT, AND QUALITY OF SERVICE.
REA MAKES NO REPRESENTATIONS OR WARRANTIES REGARDING THE CONTENT, EFFECTIVENESS, USEFULNESS, RELIABILITY, AVAILABILITY, TIMELINESS, QUALITY, SUITABILITY, ACCURACY OR COMPLETENESS OF THIS ARTIFACT OR THE RESULTS YOU MAY OBTAIN BY USING THE ARTIFACT OR THAT THE ARTIFACT WILL BE ERROR-FREE.

'''
import json 
with open("vdrtest.json", "r") as f:
    SBOMVDRdata = json.load(f)
    print("Software Product:", SBOMVDRdata["SBOMVulnerabilityDisclosure"]["ProductName"] ," Unresolved Vulnerabilities Flag: ", SBOMVDRdata["SBOMVulnerabilityDisclosure"]["UnresolvedVulnerabilities"], "as of: ", SBOMVDRdata["SBOMVulnerabilityDisclosure"]["VulnDisclosureCreateDate"])
    for c in SBOMVDRdata["Components"] :
        if "CVE" in c:
            for v in c["CVE"]:
                print(c["ComponentName"], " Component has a CVE:", "---->",v["CVEID"])
				