import dns.resolver

def perform_dns_lookup(domain):
    results = {}
    record_types = ["A", "AAAA", "MX", "NS"]

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(r) for r in answers]
        except Exception as e:
            results[record_type] = [f"Error: {e}"]

    return results
