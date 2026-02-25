import json, xml.etree.ElementTree as ET, datetime, argparse, sys

fn = "SAG-PM_VulnDisclosure_V1_1_8.xml"
fnjson = "SAG-PM_VulnDisclosure_V1_1_8.json"
print("Starting SAG-PM(TM) VDR File Converter at: "+ str(datetime.datetime.now()))
parser = argparse.ArgumentParser( 
                                    description = "Converts an XML VDR file into JSON format",
                                    epilog = "Copyright and all other rights reserved by Reliable Energy Analytics LLC (REA) 2019-2022 CONFIDENTIAL PROPERTY OF REA")
  
parser.add_argument(
                      "InputFileName",
                      help = "You must provide an input VDR file in XML format",
                      metavar = "infilename")
  
parser.add_argument(
                      "OutputFileName",
                      help = "You must provide a location to store output files (F850CR evidence data) and SBOM files",
                      metavar = "outfilename")
args = parser.parse_args()
fn = args.InputFileName
fnjson = args.OutputFileName

VDR = {"SBOMVulnerabilityDisclosure":{"CVERespository": "",
                                 "NISTNVDSearchStatus": "",	
                                 "UnresolvedVulnerabilities": "",
                                 "PackageSourceLocation": "",
                                 "ProductName": "",
                                 "ProductVersion": "",
                                 "SBOMAuthor": "",
                                 "SBOMFormat": "",
                                 "SBOMFormatSyntax": "",
                                 "SBOMLocation": "",
                                 "SBOMTimestamp": "",
                                 "SBOMTotalComponentCount": "",
                                 "SupplierName": "",
                                 "VulnDisclosureCreateDate": ""}, 
        "Components":[]}
with open(fn) as KVData:
####    ns = {"SAG": "http://softwareassuranceguardian.com/2_1_2", "xsi": "http://www.w3.org/2001/XMLSchema-instance"}
    tree = ET.ElementTree()
    tree.parse(KVData)
    root = tree.getroot()
    rootns = root.tag.split("}")[0]
    ns = {"SAG": rootns.replace("{",""), "xsi": "http://www.w3.org/2001/XMLSchema-instance"}
#    print("ROOTNS:",rootns, ns)
    VDR["SBOMVulnerabilityDisclosure"]["CVERespository"] = root.attrib["CVERespository"]
    VDR["SBOMVulnerabilityDisclosure"]["NISTNVDSearchStatus"] = root.attrib["NISTNVDSearchStatus"]
    VDR["SBOMVulnerabilityDisclosure"]["UnresolvedVulnerabilities"] = root.attrib["UnresolvedVulnerabilities"]
    VDR["SBOMVulnerabilityDisclosure"]["PackageSourceLocation"] = root.attrib["PackageSourceLocation"]
    VDR["SBOMVulnerabilityDisclosure"]["ProductName"] = root.attrib["ProductName"]
    VDR["SBOMVulnerabilityDisclosure"]["ProductVersion"] = root.attrib["ProductVersion"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMAuthor"] = root.attrib["SBOMAuthor"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMFormat"] = root.attrib["SBOMFormat"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMFormatSyntax"] = root.attrib["SBOMFormatSyntax"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMLocation"] = root.attrib["SBOMLocation"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMTimestamp"] = root.attrib["SBOMTimestamp"]
    VDR["SBOMVulnerabilityDisclosure"]["SBOMTotalComponentCount"] = root.attrib["SBOMTotalComponentCount"]
    VDR["SBOMVulnerabilityDisclosure"]["SupplierName"] = root.attrib["SupplierName"]    
    VDR["SBOMVulnerabilityDisclosure"]["VulnDisclosureCreateDate"] = root.attrib["VulnDisclosureCreateDate"]
    for component in root.findall('.//SAG:Component', ns) :
        hasCVE = False
        CVE = []
        for cvedata in component.findall('.//SAG:CVE', ns) :
            hasCVE = True
            CVEID = cvedata.find('.//SAG:CVEID', ns).text
            CVSS = cvedata.find('.//SAG:CVSS', ns).text
            CVEdesc = cvedata.find('.//SAG:CVEDescription', ns).text
            Exploitable = cvedata.find('.//SAG:Exploitable', ns).text
            KEVIndicator = cvedata.find('.//SAG:CISAKEV', ns).text
            DisruptionImpact = cvedata.find('.//SAG:DisruptionImpact', ns).text
            FixStat = cvedata.find('.//SAG:FixStatus', ns).text
            VendorFindings = cvedata.find('.//SAG:AnalysisFindings', ns).text
            SecurityAdvisoryURL = cvedata.find('.//SAG:SecurityAdvisoryURL', ns).text

            CVE.append({'CVEID':CVEID, 'CVSS': CVSS, 'CVEDescription': CVEdesc, 'Exploitable':Exploitable, 'CISAKEV': KEVIndicator, 'DisruptionImpact': DisruptionImpact, 'FixStatus':FixStat, 'AnalysisFindings': VendorFindings, 'SecurityAdvisoryURL':SecurityAdvisoryURL})
        if hasCVE :
            VDR["Components"].append({"CVESearchString": component.attrib["CVESearchString"],
                                 "ComponentID": component.attrib["ComponentID"],
                                 "ComponentName": component.attrib["ComponentName"],
                                 "ComponentSupplierName": component.attrib["ComponentSupplierName"],
                                 "ComponentVersion": component.attrib["ComponentVersion"],
                                 "NumberVulnsReported": component.attrib["NumberVulnsReported"],
                                 "CVE": CVE
                                }
                                )
        else :
            VDR["Components"].append({"CVESearchString": component.attrib["CVESearchString"],
                                 "ComponentID": component.attrib["ComponentID"],
                                 "ComponentName": component.attrib["ComponentName"],
                                 "ComponentSupplierName": component.attrib["ComponentSupplierName"],
                                 "ComponentVersion": component.attrib["ComponentVersion"],
                                 "NumberVulnsReported": component.attrib["NumberVulnsReported"]
                                }
                                )
    json = json.dumps(VDR, indent=4)
    try:
        with open(fnjson, "w") as JSONData:
            JSONData.write(json)
            JSONData.close()
            print("SUCCESS: VDR Data file created:", fnjson)
    except:
        print("ERROR with VDR conversion:", sys.exc_info())