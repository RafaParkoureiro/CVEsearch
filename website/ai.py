import nvdlib
import pandas as pd
from openai import OpenAI
import openai

def model(prompt, aikey):
    openai.api_key = aikey
    client = OpenAI(api_key=aikey)
    nvdapi_key = '56d9404c-f27a-453b-9065-d340bed0562f'
    parts = prompt.split(',')
    cve_id = parts[0]

    cve_details = nvdlib.searchCVE(key=nvdapi_key, cveId=cve_id)

    q = f'''
    You are a text processing agent extracting the most valuable information from this CVE and then answering about the user's prompt. Just return the final answer to the prompt, in form of a text answer

    Extract specified values from the source text:
    - "CVE_ID" <string>
    - "CVE_SCORE" <string>
    - "CVE_DESCRIPTION" <string> (in english)
    - "CVE_DATE_PUBLISHED" <string> (date when CVE was published)
    - "CVE_DATE_MODIFIED" <string> (date when CVE was modified)
    - "CVE_STATUS" <string> (status of the CVE)
    the following fields are subfields of the cve vector, and I want you to decompose into the following fields:
    AV (Attack Vector): Indicates how the vulnerability can be exploited. E.g., N for Network, A for Adjacent, L for Local, P for Physical.
    AC (Attack Complexity): The complexity level of the attack required to exploit the vulnerability. E.g., L for Low, H for High.
    PR (Privileges Required): The level of privileges an attacker must possess before exploiting the vulnerability. E.g., N for None, L for Low, H for High.
    UI (User Interaction): Whether the exploitation of the vulnerability requires user interaction. E.g., N for None, R for Required.
    S (Scope): Whether the vulnerability impacts resources beyond its security scope. E.g., U for Unchanged, C for Changed.
    C (Confidentiality Impact): Measures the impact on confidentiality. E.g., N for None, L for Low, H for High.
    I (Integrity Impact): Measures the impact on integrity. E.g., N for None, L for Low, H for High.
    A (Availability Impact): Measures the impact on availability. E.g., N for None, L for Low, H for High.
    - AV (Attack Vector) <string> (Attack Vector)
    - AC (Attack Complexity) <string> (Attack Complexity)
    - PR (Privileges Required) <string> (Privileges Required)
    - UI (User Interaction) <string> (User Interaction)
    - S (Scope) <string> (Scope)
    - C (Confidentiality Impact) <string> (Confidentiality Impact)
    - I (Integrity Impact) <string> (Integrity Impact)
    - A (Availability Impact) <string> (Availability Impact)
    - "Impact metrics" <string> (Impact metrics)

    Do not infer any data based on previous training, strictly use only source text given below as input.
    ========
    {cve_details}
    ========
    '''
    messages = [{"role": "system",
                 "content": q}]
    while True:
        messages.append({"role": "user", "content": parts[1]})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=150
        )
        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        return answer