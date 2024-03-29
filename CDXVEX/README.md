Many thanks to the generous help provided by Steve Springett that put me on the right path. This material is still considered a rough draft, but it does pass XML validation using Eclipse, so I'm comfortable the XML is proper. I still have a lot to learn about the semantics of this construct, but it looks very promising as a method to supply automated vulnerability disclosure reports to sw consumers, required to meet Executive Order 14028, including the NTIA minimum elements.

I think of this CDX VDR artifact as a "CARFAX" for SBOM's listing all the known issues and their status, using an implicit reporting model (only components with vulnerabilities are listed in the report). This artifact updates independently from an SBOM but is tied directly to a single SBOM document in order to answer the question:

<h3>What is the vulnerability status NOW, of product P, version V from Supplier S at the SBOM component level?</h3>
<a href="https://www.einpresswire.com/article/565091476/automated-software-product-vulnerability-reporting-in-sag-pm">Here is a writeup showing how automated vulnerability reporting can be used before procurement and before installation </a>

<a href="https://energycentral.com/c/um/bod-and-c-level-series-software-vulnerability-reporting-and-risk-management">An analogy using a food recall makes this concept clear</a> to those working outside of the cybersecurity field

It's very easy to associate a "SBOM CARFAX" artifact, like this <b>IMPLICIT</b> CDX VDR example to a specific CycloneDX SBOM, by including a "hard reference URL" where the updated NOW "CARFAX" CDX VDR document is available for download, place an external reference in your SBOM immediately following the end of components tag, as shown here:

	<externalReferences>
		<reference type="advisories">
			<url>
			https://raw.githubusercontent.com/rjb4standards/REA-Products/master/CDXVEX/CDX14.xml
			</url>
		</reference>
	</externalReferences>

</bom>

Dependency Track makes it super easy for software vendors to generate a "CARFAX for SBOM" report on the fly so that the most current report is always available at the link listed in an SBOM artifact. Software customers can monitor all of their products for vulnerabilities daily, thanks to the new VDR functionality in CycloneDX version 1.4. 


Legal Disclaimer: 
This information is provided as is with no guarantee of accuracy, completeness or merchantability. Use this information at your own risk and liability.  
