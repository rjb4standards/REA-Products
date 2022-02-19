Many thanks to the generous help provided by Steve Springett that put me on the right path. This material is still considered a rough draft, but it does pass XML validation using Eclipse, so I'm comfortable the XML is proper. I still have a lot to learn about the semantics of this construct, but it looks very promising as a method to supply vulnerability reports to sw consumers, required to meet Executive Order 14028, including the NTIA minimum elements.

I think of this CDX VEX artifact as a "CARFAX" for SBOM's listing all the known issues and their status. This artifact updates independently from an SBOM but is tied directly to a single SBOM document in order to answer the question:

<h3>What is the vulnerability status of product P, version V from Supplier S at time(NOW) at the SBOM component level?</h3>

It's very easy to associate a "SBOM CARFAX" artifact, like this CDX VEX example to a specific CycloneDX SBOM, by including a "hard reference URL" where the updated NOW "CARFAX" CDX VEX document is available for download, place an external reference in your SBOM immediately following the end of components tag, as shown here:

	<externalReferences>
		<reference type="advisories">
			<url>
			https://raw.githubusercontent.com/rjb4standards/REA-Products/master/CDXVEX/CDX14.xml
			</url>
		</reference>
	</externalReferences>

</bom>



Legal Disclaimer: 
This information is provided as is with no guarantee of accuracy, completeness or merchantability. Use this information at your own risk and liability.  
