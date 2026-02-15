All materials in this folder are available under open source MIT licensing terms

How to use these materials to create and register a product trust label in SAG-CTR:
1. Create the product.PDS file containing 3 data items, separated by a delimeter, i.e. /, SupplierName/ProductNamne/ProductVersion - see Product.pds example, https://github.com/rjb4standards/REA-Products/blob/master/JSON-SCHEMAS/Product.pds 
2. You will need to create a product VRF file and make it available online, following the SAMPLE VRF and JSON VRF Schema format. Use this link in the addMe.csv file under the NATF Response File column heading [see example addMe.csv file for details(https://github.com/rjb4standards/REA-Products/blob/master/JSON-SCHEMAS/SAG-PM-addme.csv)
3. Create the "addMe.csv" file that add product information into the SAG-PM database then use sag-pm to add the product to the database (this identifies the VRF file URL JSON artifact following the VRF Schema defiition in the repository), https://github.com/rjb4standards/REA-Products/blob/master/JSON-SCHEMAS/SAG-PM-addme.csv
4. Perform a sag-pm comprehensive risk assessment on the PDS file after adding the addme.csv file to the SAGPM database (i.e. sag-pm addProduct addme.csv evidence")
5. SAG-PM will perform a 7 step ris assessment and produce an evidence file/ Answer "Y" to submit the evidence data file as a Trust Declaration Request to SAG-CTR
6. Wait for the SAG-CTR Gatekeeper to approve your Trust Declaration Request
7. View the label in SAG-CTR using the Product ID/Digital DNA ID (SHA-256 hash value of the PDS file) using the SAG-CTR labellink API (https://softwareassuranceguardian.com/labellink/getTrustedProductLabel?ProductID=E6CC8B4801EC3408BB2FB481CA7A1FB1B775ACFC330B6E8CD996E5882ECF44FA&html=1)


The ViewVRF.py tool is available to verify and view VRF contents, based on the open source VRF schema
Usage: python ViewVRF.py --url (Location of VRF file) - requires prerequisites to be installed
Example: 
python ViewVRF.py --url https://raw.githubusercontent.com/rjb4standards/REA-Products/refs/heads/master/JSON-SCHEMAS/SAMPLEVRF-final.json
