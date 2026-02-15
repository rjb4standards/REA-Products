import json
import argparse
import requests
from jsonschema import Draft3Validator

# URL of the authoritative VDR JSON Schema
VDR_SCHEMA_URL = (
    "https://raw.githubusercontent.com/rjb4standards/REA-Products/"
    "refs/heads/master/JSON-SCHEMAS/SAG-VDR-SCHEMA.json"
)

_cached_vdr_schema = None


def load_vdr_schema():
    """
    Fetch the VDR JSON Schema from GitHub (if not already cached).
    """
    global _cached_vdr_schema

    if _cached_vdr_schema is None:
        response = requests.get(VDR_SCHEMA_URL, timeout=10)
        response.raise_for_status()
        _cached_vdr_schema = response.json()

    return _cached_vdr_schema


def validate_vdr(vdr_json: dict):
    """
    Validate a VDR JSON document against the authoritative online schema.
    Raises jsonschema.ValidationError on failure.
    """
    schema = load_vdr_schema()
    validator = Draft3Validator(schema)
    validator.validate(vdr_json)
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Validate a VDR JSON file against the online SAG-VDR schema."
    )
    parser.add_argument(
        "vdr_file",
        help="Path to the VDR JSON file to validate"
    )

    args = parser.parse_args()

    # Load the VDR JSON file provided on the command line
    with open(args.vdr_file, "r") as f:
        vdr_data = json.load(f)

    try:
        validate_vdr(vdr_data)
        print("VDR is valid against the online SAG-VDR schema.")
    except Exception as e:
        print("VDR validation failed:")
        print(e)


if __name__ == "__main__":
    main()