#Copyright and all other rights reserved by Business Cyber Guardian 2018-2026. Licensed under open source MIT licensing terms
import sys
import json
import urllib.request
import argparse
from jsonschema import validate, Draft3Validator
from jsonschema.exceptions import ValidationError

VRF_SCHEMA_URL = (
    "https://raw.githubusercontent.com/rjb4standards/REA-Products/"
    "refs/heads/master/JSON-SCHEMAS/VRF-SCHEMA-FCCUSCTM.json"
)

def load_json_from_url(url: str):
    """Load JSON from a remote URL."""
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return json.load(response)

def verify_vrf(vrf_data: dict) -> bool:
    """Validate VRF JSON against the official VRF schema."""
    try:
        schema = load_json_from_url(VRF_SCHEMA_URL)

        # Use Draft 2020-12 (correct for your schema)
        validator = Draft3Validator(schema)
        validator.validate(vrf_data)

        print("✔ VRF file is VALID according to the VRF schema")
        return True

    except ValidationError as ve:
        print("✘ VRF validation FAILED")
        print("Validation error:", ve.message)
        print("At path:", list(ve.path))
        return False

    except Exception as e:
        print("✘ Could not validate VRF schema")
        print("Error:", e)
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Load and validate a JSON VRF/VDR file from a URL."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="URL of the JSON VRF/VDR/SBOM file to load"
    )

    args = parser.parse_args()
    url = args.url

    try:
        SBOMVDRdata = load_json_from_url(url)
    except Exception as e:
        print("Failed to load JSON from URL:", e)
        sys.exit(1)

    # Validate VRF before printing fields
    verify_vrf(SBOMVDRdata)

    try:
        vr = SBOMVDRdata["VendorResponse"]

        print(
            vr["VendorLegalName"],
            vr["SupplierID"],
            vr["StreetAddress"],
            vr["City"],
            vr["StateOrProvince"],
            vr["ZipCode"],
            vr["Country"],
            vr["WebsiteURL"],
            vr["ContactTelephone"],
            vr["ContactEmail"],
            vr["ContactPerson"],
            vr["DUNSNumber"],
            vr["NAESBEIRID"],
            vr["CyberSecPolicyURL"],
            vr["FinancialDataURL"],
            vr["CompanyDataURL"]
        )

        for p in vr["Products"]:
            print(p["LicensorName"], p["ProductName"], p["Version"])

            print(
                p["SBOM"]["type"],
                p["SBOM"]["version"],
                p["SBOM"]["format"],
                p["SBOM"]["DigitalSignatureURL"],
                p["SBOM"]["URL"],
                p["SourceLocationURL"],
                p["DigitallySigned"],
                p["UnsolvedVulnerabilities"],
                p["KnownVulnInfoURL"]["DocFormat"],
                p["KnownVulnInfoURL"]["DigitalSignatureURL"],
                p["KnownVulnInfoURL"]["URL"],
                p["SDLCPolicyURL"],
                p["SDLCEvidenceDataURL"],
                p["CommercialStatus"],
                p["SupportStatus"],
                p["LastModifiedDateTimeUTC"]
            )

    except Exception as e:
        print("Trying to process as XML")
        print("Error:", e)

if __name__ == "__main__":
    main()