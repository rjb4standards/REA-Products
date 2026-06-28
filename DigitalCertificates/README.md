This folder contains the public certificate (.cer) files used to verify digital objects, i.e. software apps, signed by Business Cyber Guardian.
https://businesscyberguardian.com/

Download Verifyscript.txt and save as a powershell script with the name sagverify.ps1

Execute the sagverify.ps1 script using the LOC parameter to locate and download the X.509 public key certificate file and -OFile parameter to name output file:

powershell -c "& { ./sagverify.ps1 -Loc 'https://github.com/rjb4standards/REA-Products/raw/refs/heads/master/DigitalCertificates/BCG-SIGNING-KEY-2030.cer' -OFile test.fil}"

NOTE: Placeholder to SCITT Receipt URL that resolves a SCITT registration receipt stored on the Microsoft SCITT Transparency Log (Merkle Tree), showing inclusion path on the tree.

A SAGScore return value of -1 indicates there are no trust declarations for the object in SAG-CTR identified by this SHA256 hash value- meaning it's not trusted.

Here is how to check a certificat that is not trusted (SAGScore: -1)
powershell -c "& { ./sagverify.ps1 -Loc 'https://github.com/rjb4standards/REA-Products/raw/refs/heads/master/DigitalCertificates/Cruell-De-Vil-Pubkey.cer' -OFile test.fil}"


How do I register a X.509 digital certificate in the SAG-CTR Trust Registry and the Microsoft SCITT Ledger?


Run sag-pm on the digital certificate (cer) file and submit evidence data to SAG-CTR when asked to submit a trust declaration answer Y

The SAG-CTR Gatekeeper will evaluate the submitted evidence in the Trust Declarations Queue against SAG-CTR Label Owner Registration Policies and, if all checks pass, the information will be registered in SAG-CTR Trust Registry and Microsoft SCITT Ledger.

