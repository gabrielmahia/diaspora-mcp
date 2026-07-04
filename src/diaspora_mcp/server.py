"""DiasporaMCP — Kenya Diaspora Services (6 tools). All data DEMO.

Distinct from remit-mcp (which covers remittance corridors only).
This covers the full lifecycle: immigration status, dual citizenship,
diaspora taxes, Kenya homeland investment, community verification.
"""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP

mcp = FastMCP(
    name="diaspora-mcp",
    instructions="Kenya diaspora services via MCP — immigration guidance, dual citizenship, diaspora taxes, homeland investment, community verification. DEMO."
)

@mcp.tool(name="dual_citizenship_guide",
          description="Kenya dual citizenship guidance — eligibility, process, rights. DEMO.")
def dual_citizenship_guide(current_citizenship: Optional[str] = "USA") -> dict:
    return {"source": "DEMO — Kenya Citizenship and Immigration Act 2011",
            "current_citizenship": current_citizenship,
            "kenya_dual_citizenship": {
                "eligibility": "Kenya allows dual citizenship since 2010 Constitution. No need to renounce Kenya citizenship when acquiring foreign citizenship.",
                "if_born_kenyan": "Kenyans by birth retain citizenship when naturalizing abroad. Notify Kenyan embassy (not required by law but advisable for passport renewal).",
                "if_kenyan_descent": "Children born abroad to Kenyan parents are Kenyan citizens. Register at Kenyan embassy to obtain Kenyan passport.",
                "rights_retained": "Vote in Kenya elections, own land, inherit property, hold public office (with exceptions for some senior positions).",
                "restrictions": "Some senior government positions (President, Deputy President, Cabinet Secretary) require renouncing foreign citizenship.",
            }, "process": {
                "kenyan_passport": "Apply at Kenyan embassy in your country. Requirements: birth certificate, old passport (if any), ID. Cost: ~$100 USD.",
                "registration_diaspora": "Register at Kenyan embassy. Enables consular services, voter registration for diaspora voting.",
                "diaspora_voting": "Kenyans abroad can register to vote at Kenyan embassies. IEBC portal: iebc.or.ke",
            }, "contacts": {"embassy_usa": "Embassy of Kenya, Washington DC: kenyaembassydc.org",
                             "embassy_uk": "Kenya High Commission, London: kenyahighcom.org.uk"}}

@mcp.tool(name="diaspora_tax_guide",
          description="Tax obligations for Kenya diaspora — Kenya and US/UK/CA dual tax considerations. DEMO.")
def diaspora_tax_guide(residence_country: Optional[str] = "USA") -> dict:
    COUNTRIES = {
        "USA": {
            "kenya_tax": "Non-residents with Kenya income pay 30% non-resident tax. No Kenya tax on foreign-earned income.",
            "us_obligations": "US citizens/residents must file US tax returns even living abroad. Kenya income must be reported. Foreign Tax Credit (Form 1116) may reduce double taxation.",
            "fbar": "If Kenya bank account balance exceeds $10,000 at any point, file FBAR (FinCEN 114) annually. FATCA also applies to foreign account holdings.",
            "social_security": "No US-Kenya Social Security Totalization Agreement. Pay social security in whichever country you work.",
            "kenya_rental_income": "Declare Kenya rental income on US Form 1040. May also owe Kenya withholding tax. Double tax treaty: check current US-Kenya treaty status.",
        },
        "UK": {
            "kenya_tax": "Non-residents with Kenya income pay 30% non-resident withholding tax.",
            "uk_obligations": "UK tax residents must declare worldwide income. Kenya income included. UK-Kenya double taxation agreement applies.",
            "remittance_basis": "Non-domiciled UK residents may be able to use remittance basis taxation — only UK tax on Kenya income brought into UK.",
            "hmrc": "Declare Kenya income on UK Self Assessment tax return annually.",
        },
        "CA": {
            "kenya_tax": "Non-residents with Kenya income pay 30% non-resident tax.",
            "canada_obligations": "Canadian residents must report worldwide income. Kenya income included. Canada-Kenya tax treaty applies.",
            "tfsa": "TFSA contributions not affected by foreign income. RRSP contributions based on Canadian earned income only.",
        },
    }
    country_data = COUNTRIES.get(residence_country.upper(), COUNTRIES["USA"])
    return {"source": "DEMO — KRA, IRS, HMRC, CRA", "residence_country": residence_country,
            "tax_guidance": country_data,
            "key_principle": "Most diaspora Kenyans face obligations in BOTH countries. Get advice from a cross-border tax accountant.",
            "kenya_tax_portal": "itax.kra.go.ke | PIN registration required",
            "disclaimer": "Not tax advice. Consult a licensed tax professional in both Kenya and your country of residence."}

@mcp.tool(name="kenya_homeland_investment",
          description="Investment options for Kenya diaspora investing back home. DEMO.")
def kenya_homeland_investment(budget_usd: Optional[float] = 10000.0) -> dict:
    return {"source": "DEMO — NSE, CBK, Kenya Investment Authority", "budget_usd": budget_usd,
            "investment_options": [
                {"name": "M-Akiba Treasury Bonds", "min_usd": 500,
                 "returns": "~14% annual (2025 rates)", "risk": "Low (government-backed)",
                 "access": "M-PESA via *844# | DhowCSD portal: dhow.centralbank.go.ke",
                 "note": "Kenya's mobile-first retail bond. Diaspora can buy via international M-PESA or through DhowCSD."},
                {"name": "NSE Equities", "min_usd": 500,
                 "returns": "Varies (NSE 20-share index avg 8-15% historically)", "risk": "Medium",
                 "access": "Open CDS account via stockbroker. Genghis Capital, Dyer & Blair, AIB-AXYS Africa.",
                 "note": "Diaspora can invest. Dividends subject to 5% withholding tax."},
                {"name": "Unit Trusts (MMF)", "min_usd": 100,
                 "returns": "12-15% (money market, 2025)", "risk": "Low",
                 "access": "CIC, Britam, Old Mutual apps. Mobile-accessible.",
                 "note": "Money Market Funds are the safest, most liquid option. Good entry point."},
                {"name": "Kenya Infrastructure Bonds", "min_usd": 5000,
                 "returns": "~14-16% TAX FREE", "risk": "Low",
                 "access": "CBK DhowCSD portal during infrastructure bond auctions",
                 "note": "Tax-free returns. High demand. Often oversubscribed within days of announcement."},
                {"name": "Real Estate (REIT)", "min_usd": 1000,
                 "returns": "8-12% rental yield + capital appreciation", "risk": "Medium",
                 "access": "ILAM Fahari I-REIT listed on NSE (ticker: ILAM.NRE)",
                 "note": "Kenya's only listed REIT. Liquid real estate exposure without buying property."},
            ], "platform_recommendation": f"For ${budget_usd:,.0f}: Start with M-Akiba + MMF (liquid, low risk), then add NSE equities as comfort grows.",
            "faida_mcp": "pip install faida-mcp for full capital markets guide"}

@mcp.tool(name="diaspora_verification",
          description="Services for diaspora identity verification and document authentication for Kenya use. DEMO.")
def diaspora_verification(document_type: Optional[str] = None) -> dict:
    DOCS = {
        "birth_certificate": {
            "apostille": "Apostille not required for Kenya. Submit to Kenyan embassy with sworn translation if not in English.",
            "kenya_equivalent": "Kenyan birth certificate required for many government processes. Register at Civil Registration in Kenya.",
            "use_cases": "Passport renewal, succession, NHIF registration for dependents.",
        },
        "marriage_certificate": {
            "apostille": "Apostille required if married abroad for use in Kenya courts.",
            "recognition": "Foreign marriages generally recognised in Kenya if valid in country where performed.",
            "use_cases": "Succession rights, next-of-kin registration, NHIF dependant registration.",
        },
        "academic_certificates": {
            "authentication": "Degree certificates need authentication by issuing institution then apostille for Kenya professional bodies (e.g., Law Society, Medical Board).",
            "kenya_recognition": "Kenya National Qualifications Authority (KNQA): knqa.go.ke",
        },
        "police_clearance": {
            "process": "Request from your country's police/FBI/DBS. Apostille. Submit to Kenya employer or immigration as required.",
            "kenya_clearance": "Kenya Certificate of Good Conduct: DCI Kenya via ecitizen.go.ke",
        },
    }
    if document_type:
        d = document_type.lower().replace(" ","_")
        matched = {k: v for k, v in DOCS.items() if k in d}
        return {"source": "DEMO — Kenya Immigration, ecitizen.go.ke", "document": document_type,
                "guidance": matched or {"general": "Contact Kenyan embassy in your country for document authentication requirements."}}
    return {"source": "DEMO — Kenya Immigration Department", "all_documents": DOCS,
            "apostille": "Hague Apostille Convention: Kenya is a member. Apostille from issuing country accepted in Kenya.",
            "kenya_embassy": "Find your nearest Kenya embassy: mfa.go.ke/missions-abroad"}

@mcp.tool(name="diaspora_community_guide",
          description="Kenya diaspora community resources and organisations by country. DEMO.")
def diaspora_community_guide(country: Optional[str] = "USA") -> dict:
    COMMUNITIES = {
        "USA": [
            {"name": "Kenya USA Diaspora Council (KUDC)", "focus": "Advocacy, investment facilitation, cultural preservation"},
            {"name": "Kenya Community Abroad (KCA)", "focus": "Welfare, community events, emergency support"},
            {"name": "KENASAS (Kenya Scientists and Engineers)", "focus": "Professional network for Kenyan STEM professionals in USA"},
            {"name": "Kenya Investment Authority (KenInvest) USA Office", "focus": "Investment guidance for diaspora: invest.go.ke"},
        ],
        "UK": [
            {"name": "Kenya Community Organisation UK", "focus": "Community welfare and events"},
            {"name": "Kenya High Commission London Community Desk", "focus": "Consular services, community liaison"},
        ],
        "CA": [
            {"name": "Kenya Diaspora Canada", "focus": "Community building, investment, cultural events"},
            {"name": "Kenya High Commission Ottawa", "focus": "Consular services"},
        ],
    }
    orgs = COMMUNITIES.get(country.upper(), COMMUNITIES["USA"])
    return {"source": "DEMO — Kenya diaspora community directory", "country": country,
            "organisations": orgs,
            "investment_facilitation": "Kenya Investment Authority: invest.go.ke | diaspora@kenyainvest.go.ke",
            "voter_registration": "Register to vote at Kenyan embassy. IEBC: iebc.or.ke",
            "remittance": "Kenyans abroad sent $4.1B home in 2024. See remit-mcp for corridor rates."}

@mcp.tool(name="immigration_status_guide",
          description="Common immigration questions for Kenyans in USA, UK, or Canada. DEMO.")
def immigration_status_guide(country: Optional[str] = "USA", status: Optional[str] = None) -> dict:
    USA_GUIDE = {
        "green_card_holder": "Permanent resident. Can sponsor spouse and unmarried children. 5 years (3 if married to US citizen) to naturalise. Travel >6 months may affect residency.",
        "h1b": "Employer-sponsored work visa. Subject to annual cap. Can apply for green card while on H-1B. Valid for 3+3 years.",
        "f1_student": "Student visa. OPT allows 12 months work after graduation (STEM: 36 months). Limited off-campus work rights.",
        "citizenship": "Naturalization: 5 years PR (3 if married to US citizen), 30+ months physically present, English test, civics test. Does NOT affect Kenya citizenship.",
        "i751_removal": "Conditional green card holders must file I-751 (Removal of Conditions) within 90 days of 2-year anniversary. File jointly with US citizen spouse, or file solo with waiver.",
    }
    UK_GUIDE = {
        "tier2_skilled": "Skilled Worker visa. Employer-sponsored. Can apply for ILR after 5 years. Points-based system.",
        "ilt": "Indefinite Leave to Remain after 5 years on eligible visa. Biometrics at UKVI. Fee: ~£2,400+.",
        "citizenship": "British naturalisation: 5 years ILR (1 year for spouses). Does NOT affect Kenya citizenship.",
    }
    GUIDES = {"USA": USA_GUIDE, "UK": UK_GUIDE}
    guide = GUIDES.get(country.upper(), USA_GUIDE)
    if status:
        s = status.lower().replace(" ","_").replace("-","_")
        matched = {k: v for k, v in guide.items() if k in s or any(w in s for w in k.split("_"))}
        return {"source": "DEMO — USCIS, UKVI, IRCC", "country": country, "status": status,
                "guidance": matched or {"general": f"Consult an immigration attorney in {country} for personalised advice."},
                "disclaimer": "Not immigration legal advice."}
    return {"source": "DEMO — USCIS, UKVI, IRCC", "country": country, "all_statuses": guide,
            "legal_aid": "Find a licensed immigration attorney via your country's bar association.",
            "disclaimer": "Not immigration legal advice. Situations vary. Always consult a licensed attorney."}

def main() -> None:
    """Console entry point."""
    mcp.run()
