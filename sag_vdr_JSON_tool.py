"""
JSON Schema for SAG-PM Vulnerability Disclosure Report (VDR)

This module defines the JSON Schema for the SPDX SAG-PM-V2_1_4-VDR.json artifact,
which is a Software Bill of Materials (SBOM) Vulnerability Disclosure Report format.

The schema defines the structure of:
- SBOMVulnerabilityDisclosure: Top-level metadata about the SBOM and scan
- Components: Array of software components with their vulnerability data
- CVE Objects: Nested vulnerability details for each component

Usage:
    import json
    import jsonschema
    
    # Load your JSON artifact
    with open('SAG-PM-V2_1_4-VDR.json') as f:
        data = json.load(f)
    
    # Validate against the schema
    jsonschema.validate(data, SAG_VDR_SCHEMA)
"""

import json


SAG_VDR_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SAG-PM Vulnerability Disclosure Report (VDR) Schema",
    "description": "JSON Schema for SPDX SBOM Vulnerability Disclosure Report format",
    "type": "object",
    "required": ["SBOMVulnerabilityDisclosure", "Components"],
    "additionalProperties": False,
    
    "properties": {
        
        # ===== SBOMVulnerabilityDisclosure =====
        "SBOMVulnerabilityDisclosure": {
            "type": "object",
            "description": "Top-level metadata about the SBOM and vulnerability scan",
            "additionalProperties": False,
            "required": [
                "CVERespository",
                "NISTNVDSearchStatus",
                "UnresolvedVulnerabilities",
                "PackageSourceLocation",
                "ProductName",
                "ProductVersion",
                "SBOMAuthor",
                "SBOMFormat",
                "SBOMFormatSyntax",
                "SBOMLocation",
                "SBOMTimestamp",
                "SBOMTotalComponentCount",
                "SupplierName",
                "VulnDisclosureCreateDate"
            ],
            
            "properties": {
                
                "CVERespository": {
                    "type": "string",
                    "description": "The CVE repository used for vulnerability lookup (e.g., NIST_NVD)",
                    "examples": ["NIST_NVD"]
                },
                
                "NISTNVDSearchStatus": {
                    "type": "string",
                    "description": "Status of the NIST NVD search operation",
                    "enum": ["Success", "Partial", "Failed", "Timeout"]
                },
                
                "UnresolvedVulnerabilities": {
                    "type": "string",
                    "description": "Whether there are unresolved vulnerabilities",
                    "enum": ["Y", "N"]
                },
                
                "PackageSourceLocation": {
                    "type": "string",
                    "description": "Source location of the package or NOASSERTION",
                    "examples": ["NOASSERTION", "https://example.com/source"]
                },
                
                "ProductName": {
                    "type": "string",
                    "description": "Name of the product being analyzed",
                    "examples": ["SAG-PM.EXE"]
                },
                
                "ProductVersion": {
                    "type": "string",
                    "description": "Version of the product",
                    "examples": ["2.1.4"]
                },
                
                "SBOMAuthor": {
                    "type": "string",
                    "description": "Author(s) of the SBOM (can be string representation of list)",
                    "examples": ["['Organization:dns:businesscyberguardian.com', 'Tool:SAG-PM Version 2.1.4']"]
                },
                
                "SBOMFormat": {
                    "type": "string",
                    "description": "Format specification used (e.g., spdx, cyclonedx)",
                    "enum": ["spdx", "cyclonedx", "other"]
                },
                
                "SBOMFormatSyntax": {
                    "type": "string",
                    "description": "Syntax format of the SBOM (e.g., JSON, XML)",
                    "enum": ["JSON", "XML", "YAML", "RDF", "Text"]
                },
                
                "SBOMLocation": {
                    "type": "string",
                    "description": "File path or URL to the SBOM document",
                    "examples": ["file:///C:\\Users\\dick\\ReliableEnergyAnalytics\\...\\SAG-PM-V2_1_4-SBOM.json"]
                },
                
                "SBOMTimestamp": {
                    "type": "string",
                    "format": "date-time",
                    "description": "ISO 8601 timestamp when the SBOM was created"
                },
                
                "SBOMTotalComponentCount": {
                    "type": "string",
                    "description": "Total number of components in the SBOM",
                    "examples": ["112"]
                },
                
                "SupplierName": {
                    "type": "string",
                    "description": "Name and type of the supplier/organization",
                    "examples": ["Organization:BUSINESS CYBER GUARDIAN (Reliable Energy Analytics LLC)"]
                },
                
                "VulnDisclosureCreateDate": {
                    "type": "string",
                    "format": "date-time",
                    "description": "ISO 8601 timestamp when the vulnerability disclosure report was created"
                }
            }
        },
        
        # ===== Components Array =====
        "Components": {
            "type": "array",
            "description": "Array of software components analyzed for vulnerabilities",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "CVESearchString",
                    "ComponentID",
                    "ComponentName",
                    "ComponentSupplierName",
                    "ComponentVersion",
                    "NumberVulnsReported"
                ],
                
                "properties": {
                    
                    "CVESearchString": {
                        "type": "string",
                        "format": "uri",
                        "description": "URL to search NIST NVD for vulnerabilities of this component",
                        "examples": ["https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=SAG-PM.EXE+2.1.4"]
                    },
                    
                    "ComponentID": {
                        "type": "string",
                        "description": "Unique identifier for the component (often empty or UUID)",
                        "examples": ["", "123e4567-e89b-12d3-a456-426614174000"]
                    },
                    
                    "ComponentName": {
                        "type": "string",
                        "description": "Human-readable name of the component",
                        "examples": ["SAG-PM.EXE", "requests", "numpy"]
                    },
                    
                    "ComponentSupplierName": {
                        "type": "string",
                        "description": "Organization or person who supplied/created the component",
                        "examples": [
                            "Organization:BUSINESS CYBER GUARDIAN (Reliable Energy Analytics LLC)",
                            "Person: Python Software Foundation",
                            "NOASSERTION"
                        ]
                    },
                    
                    "ComponentVersion": {
                        "type": "string",
                        "description": "Version number of the component",
                        "examples": ["2.1.4", "1.13.0", "2.2.1", ""]
                    },
                    
                    "NumberVulnsReported": {
                        "type": "string",
                        "description": "Count of reported CVEs for this component",
                        "examples": ["0", "1", "5"]
                    },
                    
                    "CVE": {
                        "type": "array",
                        "description": "Array of CVE details for vulnerabilities found in this component",
                        "items": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": [
                                "CVEID",
                                "CVSS",
                                "CVEDescription",
                                "Exploitable",
                                "CISAKEV",
                                "DisruptionImpact",
                                "FixStatus",
                                "AnalysisFindings",
                                "SecurityAdvisoryURL"
                            ],
                            
                            "properties": {
                                
                                "CVEID": {
                                    "type": "string",
                                    "pattern": "^CVE-\\d{4}-\\d{4,}$",
                                    "description": "CVE Identifier (Common Vulnerabilities and Exposures)",
                                    "examples": ["CVE-2014-8564", "CVE-2023-29530"]
                                },
                                
                                "CVSS": {
                                    "type": "string",
                                    "description": "CVSS score (Common Vulnerability Scoring System)",
                                    "examples": ["5.0", "7.5", "9.8"]
                                },
                                
                                "CVEDescription": {
                                    "type": "string",
                                    "description": "Detailed description of the vulnerability"
                                },
                                
                                "Exploitable": {
                                    "type": "string",
                                    "description": "Whether the vulnerability is exploitable in this context",
                                    "enum": ["Y", "N"]
                                },
                                
                                "CISAKEV": {
                                    "type": "string",
                                    "description": "CISA Known Exploited Vulnerabilities (KEV) status",
                                    "examples": ["--NOT CISA KEV--", "CISA_KEV_ACTIVE"]
                                },
                                
                                "DisruptionImpact": {
                                    "type": "string",
                                    "description": "Impact of the vulnerability on operations",
                                    "examples": ["None", "Low", "Medium", "High"]
                                },
                                
                                "FixStatus": {
                                    "type": "string",
                                    "description": "Status of the fix for this vulnerability",
                                    "enum": ["Available", "N/A", "In Progress", "Unknown"]
                                },
                                
                                "AnalysisFindings": {
                                    "type": "string",
                                    "description": "Analysis and findings about the vulnerability (e.g., false positive explanation)"
                                },
                                
                                "SecurityAdvisoryURL": {
                                    "type": "string",
                                    "description": "URL to the security advisory or N/A",
                                    "examples": ["N/A", "https://nvd.nist.gov/vuln/detail/CVE-2014-8564"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


def validate_vdr(data: dict) -> tuple[bool, list[str]]:
    """
    Validate a VDR JSON object against the SAG schema.
    
    Args:
        data: The parsed JSON data to validate
    
    Returns:
        tuple: (is_valid, error_messages)
            is_valid (bool): True if data conforms to schema
            error_messages (list): List of validation error messages (empty if valid)
    """
    try:
        import jsonschema
    except ImportError:
        return False, ["jsonschema module not installed. Run: pip install jsonschema"]
    
    errors = []
    validator = jsonschema.Draft7Validator(SAG_VDR_SCHEMA)
    
    for error in sorted(validator.iter_errors(data), key=str):
        path = " -> ".join(str(p) for p in error.absolute_path) or "root"
        errors.append(f"{path}: {error.message}")
    
    return len(errors) == 0, errors


def print_schema(indent: int = 4) -> str:
    """Return a formatted string of the schema."""
    return json.dumps(SAG_VDR_SCHEMA, indent=indent)


def describe_schema() -> str:
    """Generate a human-readable description of the schema."""
    description = """
SAG-PM VULNERABILITY DISCLOSURE REPORT (VDR) - SCHEMA OVERVIEW
==============================================================

ROOT OBJECT
-----------
The VDR is a JSON object with two required top-level properties:
1. SBOMVulnerabilityDisclosure - Metadata about the SBOM and scan
2. Components - Array of analyzed software components

SBOM VULNERABILITY DISCLOSURE (Metadata)
---------
Contains scan metadata:
- CVERespository: Source of CVE data (e.g., NIST_NVD)
- ProductName & ProductVersion: What was analyzed
- SBOMLocation: File path to the source SBOM
- SBOMTimestamp: When the SBOM was created
- SBOMTotalComponentCount: Number of components scanned
- SupplierName: Organization responsible for the product
- VulnDisclosureCreateDate: When this report was generated
- NISTNVDSearchStatus: Success/Partial/Failed
- UnresolvedVulnerabilities: Y/N flag

COMPONENTS (Array)
------------------
Each component represents a software package with:
- ComponentName: Name (e.g., "requests", "numpy", "SAG-PM.EXE")
- ComponentVersion: Semantic version
- ComponentSupplierName: Creator/maintainer (Organization or Person)
- NumberVulnsReported: Count of CVEs found
- CVESearchString: NIST NVD API URL for this component
- CVE: [Optional] Array of CVE details (if vulnerabilities found)

COMPONENT CVE DETAILS (Nested)
------------------------------
Each CVE object contains:
- CVEID: CVE identifier (CVE-YYYY-NNNNN format)
- CVSS: Severity score (0-10)
- CVEDescription: Details about the vulnerability
- Exploitable: Y/N - Can it be exploited in this product?
- CISAKEV: CISA Known Exploited Vulnerabilities status
- DisruptionImpact: Severity of potential impact
- FixStatus: Availability of patches
- AnalysisFindings: Security team analysis (e.g., "FALSE POSITIVE")
- SecurityAdvisoryURL: Link to advisory

EXAMPLE USES
------------
1. Validate an existing VDR:
   is_valid, errors = validate_vdr(json.load(open('vdr.json')))
   
2. Export schema as JSON:
   print(print_schema())
   
3. Count vulnerabilities:
   total_vulns = sum(int(c.get('NumberVulnsReported', 0))
                     for c in data['Components'])
   
4. Find false positives:
   false_positives = [c for c in data['Components']
                      if 'FALSE POSITIVE' in c.get('CVE', [{}])[0].get('AnalysisFindings', '')]
"""
    return description


if __name__ == "__main__":
    import sys
    
    print(describe_schema())
    
    # Example: Load and validate a VDR file
    if len(sys.argv) > 1:
        vdr_file = sys.argv[1]
        print(f"\nValidating: {vdr_file}")
        try:
            with open(vdr_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            is_valid, errors = validate_vdr(data)
            if is_valid:
                print("✓ VDR is valid!")
                print(f"  Product: {data['SBOMVulnerabilityDisclosure']['ProductName']} "
                      f"v{data['SBOMVulnerabilityDisclosure']['ProductVersion']}")
                print(f"  Components: {len(data['Components'])}")
                total_vulns = sum(int(c.get('NumberVulnsReported', 0)) 
                                 for c in data['Components'])
                print(f"  Total CVEs: {total_vulns}")
            else:
                print("✗ VDR validation failed:")
                for error in errors:
                    print(f"  - {error}")
        except FileNotFoundError:
            print(f"✗ File not found: {vdr_file}")
        except json.JSONDecodeError as e:
            print(f"✗ Invalid JSON: {e}")
    print(print_schema())
