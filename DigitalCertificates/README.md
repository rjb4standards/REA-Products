This folder contains the public certificate (.cer) files used to verify digital objects, i.e. software apps, signed by Business Cyber Guardian.
https://businesscyberguardian.com/

Download Verifyscript.txt and save as a powershell script with the name sagverify.ps1

Execute the sagverify.ps1 script using the LOC parameter to locate and download the X.509 public key certificate file and -OFile parameter to name output file:

powershell -c "& { ./sagverify.ps1 -Loc 'https://github.com/rjb4standards/REA-Products/raw/refs/heads/master/DigitalCertificates/BCG-SIGNING-KEY-2030.cer' -OFile test.fil}"

How do I register a self-signed public certificate into the SAG-CTR Trust Registry?


Run sag-pm on the cer file and submit evidence data to SAG-CTR when asked to submit a trust declaration answer Y

