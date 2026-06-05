This folder contains the public certificate (.cer) files used to verify digital objects, i.e. software apps, signed by Business Cyber Guardian.
https://businesscyberguardian.com/

Download Verifyscript.txt and save as a powershell script with the name sagverify.ps1

Execute the sagverify.ps1 script using the LOC parameter to locate and download the X.509 public key certificate file:

powershell -c "& './sagverify.ps1' -LOC 'https://github.com/rjb4standards/REA-Products/raw/refs/heads/master/DigitalCertificates/BCG-CODE-SIGNING-KEY-2026.cer'"
