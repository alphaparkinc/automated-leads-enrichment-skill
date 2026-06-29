import sys
import json
from leads_enrichment import LeadsEnrichmentClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== Automated Leads Enrichment Agent Example ===")
    client = LeadsEnrichmentClient()
    
    prospect = "Sarah Connor"
    domain = "skynet.io"
    focus = "automating factory output and hardware tracking"
    
    result = client.enrich_lead(prospect, domain, focus)
    print("\n--- Enriched Profile Metadata ---")
    print(json.dumps(result["enriched_profile"], indent=2))
    
    print("\n--- Outbound Email Draft ---")
    print(result["outreach_email_draft"])

if __name__ == "__main__":
    main()
