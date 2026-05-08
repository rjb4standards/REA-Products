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
