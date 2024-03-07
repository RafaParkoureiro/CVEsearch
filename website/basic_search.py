import nvdlib
import pandas as pd

def search(cveid):
    api_key = 'f13bc9f8-9937-4e5b-832f-7c02469a1e0a'
    cve_id = cveid
    cve_details = nvdlib.searchCVE(cveId=cve_id, key=api_key)
    cve = cve_details[0]

    data = {
        'id': cve.id,
        'description': cve.descriptions[0].value if cve.descriptions else None,
        'sourceIdentifier': cve.sourceIdentifier,
        'published': cve.published,
        'score': cve.score if hasattr(cve, 'score') else None
    }

    # Creating DataFrame
    df = pd.DataFrame(data)

    return df