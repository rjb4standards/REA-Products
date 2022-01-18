This NIST C-SCRM + NTIA SBOM risk assessment use case for Executive Order 14028 implementations demonstrates use of the <a href="https://spdx.github.io/spdx-spec/">SPDX SBOM format</a> along with <a href="https://raw.githubusercontent.com/rjb4standards/REA-Products/master/SAGVulnDisclosure.xsd">the open source SBOM Vulnerability Disclosure Report (VDR) with enhancements included in version 1.1.7</a>, including:

- Use of UnresolvedVulnerabilities flag to expedite risk assessment when a vendor indicates that a product SBOM contains components with known vulnerabilities
- Use of the Exploitable Flag to indicate that a particular CVE is exploitable, for a specific SBOM component

These elements enable a software consumer to perform a more efficient, rapid risk assessment when new vulnerabilities are reported

The Vendor Resposne File (VRF) is provided by a software vendor to a software customer. The VRF serves as an index to other material that is needed to perfrom a risk assessment following NIST SP 800-161 Appendix F for Executive Order 14028. The list of links to evidence data identified in the VRF includes:
<ul>
  <li> Software Supplier identification information </li>
  <li> Company data, e.g., organizational information and other information typically found in a legal filing, i.e. SEC </li>
  <li> Company Financial data, e.g., information that would typically be filed with the SEC </li>
  <li> Company Cybersecurity Policies and Practices </li>
  <li> SDLC practices and policies followed when developing a software product </li>
  <li> SDLC evidence data showing that SDLC practices and policies were followed during product development, distribution and maintenance, e.g., in-toto or SLSA data </li>
  <li> SBOM file </li>
  <li> Vulnerability Disclosure Report (VDR); published with SBOM and updated whenever a new vulnerability is reported</li>
  <li> Digital signature files for many of the above items, i.e. SBOM, VDR, etc. </li>
 </ul>
 
 A typical NIST C-SCRM risk assessment following SP 800-161 Appendix F will produce 13 files of evidence data.
