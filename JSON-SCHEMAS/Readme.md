All materials in this folder are available under open source MIT licensing terms

How to use these materials to create and register a product trust label in SAG-CTR:
1. Create the product.PDS file containing 3 data items, separated by a delimeter, i.e. /, SupplierName/ProductNamne/ProductVersion - see Product.pds example
2. Create the "addMe.csv" file that add product information into the SAG-PM database then use sag-pm to add the product to the database (this identifies the VRF file URL JSON artifact following the VRF Schema defiition in the repository)
3. Perform a sag-pm comprehensive risk assessment on the PDS file after adding the addme.csv file to the SAGPM database
4. Answey "Y" to submit the evidence data file as a Trust Declaration Request to SAG-CTR
5. Wait for the SAG-CTR Gatekeeper to approve your Trust Declaration Request
6. View the label in SAG-CTR using the Product ID/Digital DNA ID (SHA-256 hash value of the PDS file) using the SAG-CTR labellink API (https://softwareassuranceguardian.com/labellink/getTrustedProductLabel?ProductID=E6CC8B4801EC3408BB2FB481CA7A1FB1B775ACFC330B6E8CD996E5882ECF44FA&html=1)


The ViewVRF.py tool is available to verify and view VRF contents, based on the open source VRF schema
Usage: python ViewVRF.py --url (Location of VRF file) - requires prerequisites to be installed
Example: 
python ViewVRF.py --url https://raw.githubusercontent.com/rjb4standards/REA-Products/refs/heads/master/JSON-SCHEMAS/SAMPLEVRF-final.json
