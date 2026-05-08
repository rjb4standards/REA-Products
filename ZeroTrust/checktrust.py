#MIT License
#
#Copyright (c) 2018-2026 Business Cyber Guardian (TM) a Reliable Energy Analytics LLC Company
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
def checktrust(zero_trust_domain, entity_dnaid, resource_dnaid, delimiter):
    concat_str = f"{zero_trust_domain}{delimiter}{entity_dnaid}{delimiter}{resource_dnaid}"
    logger.info(f"CheckTrust: {concat_str}")

    ztbond_dnaid = hashlib.sha256(concat_str.encode("utf-8")).hexdigest().upper()
    url = f"{ZTBcfg.get_sag_ctr_lookup_url()}{ztbond_dnaid}"

    logger.info(f"Checking SAG-CTR for ZTBOND DNAID {ztbond_dnaid}")

    try:
        resp = requests.get(url, timeout=5, verify=VERIFY)
        data = resp.json()[0]
    except Exception as e:
        logger.error(f"SAG-CTR API error: {e}")
        return False

    sag_score = data["SAGScore"]
    logger.info(f"SAGScore Response: {json.dumps(data)}")

    return sag_score != -1 # -1 means ZTBOND record not found - not trusted
