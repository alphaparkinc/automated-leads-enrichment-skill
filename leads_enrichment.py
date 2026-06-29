import os
from typing import Dict, Any, Optional

class LeadsEnrichmentClient:
    """
    Client SDK B2B lead enrichment profiling and automated cold outreach copywriting.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("LEADS_API_KEY")
        self.mock_mode = self.api_key is None or self.api_key == "mock"

    def enrich_lead(self, prospect_name: str, domain: str, focus: str) -> Dict[str, Any]:
        """
        Simulates B2B attribute resolution and builds email copy targeting the company profiles.
        """
        # Mock lookup data based on domain
        clean_domain = domain.lower().replace("www.", "").split('.')[0]
        company_name = clean_domain.capitalize()
        
        profile = {
            "company_name": company_name,
            "estimated_size": "50-200 employees",
            "industry": "Software & Technology Services",
            "key_technologies": ["React", "Python", "PostgreSQL", "AWS"]
        }
        
        email_draft = (
            f"Subject: Enhancing {company_name}'s developer velocity with AI Agents\n\n"
            f"Hi {prospect_name},\n\n"
            f"I was researching {company_name} and noticed your focus on tech stacks including "
            f"{', '.join(profile['key_technologies'])}. We help companies automate workflows by "
            f"building production-ready agent environments. Specifically, we can help streamline your "
            f"{focus}.\n\n"
            f"Would you be open to a quick 10-minute sync next Tuesday to see how this fits into your roadmap?\n\n"
            f"Best,\nAI Automation Agent"
        )
        
        return {
            "enriched_profile": profile,
            "outreach_email_draft": email_draft
        }
