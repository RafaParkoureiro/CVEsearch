import nvdlib
import pandas as pd
import openai

#Replace 'YOUR_API_KEY' with your actual API key
#api_key = '1aac5d44-2d62-415e-92a8-ff2a6e251fc0'

#Fetch details of a specific CVE to serve as an example
#cve_id = 'CVE-2021-26855'
#cve_details = nvdlib.searchCVE(cveId=cve_id, key=api_key)
#cve_details = nvdlib.searchCVE(key=api_key,cveId=cve_id)


#if cve_details:
    #print(cve_details)


'''print(f"Severity: {cve_details.v31severity} - Score: {cve_details.v31score}")
print(f"Description: {cve_details.descriptions[0].value}")
print(f"Vector: {cve_details.v31vector}")'''
## Simple data extraction

# Read output file
with open('output', 'r') as f:
    output = f.read()

#print(output)
# Read lease.txt
#with open('lease.txt') as f:
 #   lease = f.read()
openai_key = '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'


# Create prompt
q = f'''
You are responsible for outputting a pandas query to select a specific group of CVEs from the dataframe, for example, if I give you the following prompt: "I want CVEs with a score greater than 7", you should return the following query: "df[df['v31score'] > 7]". You should return the query as a string.
Do not infer any data based on previous training, strictly use only source text given below as input.
This are the "parameters" you can make queries with:
data is in ISO 8601 date/time format!!
========
['id', 'description', 'sourceIdentifier', 'published', 'lastModified',
       'vulnStatus', 'exploitAdd', 'actionDue', 'requiredAction', 'references',
       'cwe', 'configurations', 'url', 'cpe', 'v31score', 'v30score',
       'v2score', 'v31vector', 'v30vector', 'v2vector', 'v31severity',
       'v30severity', 'v2severity', 'v31exploitability', 'v30exploitability',
       'v2exploitability', 'v31impactScore', 'v30impactScore', 'v2impactScore',
       'v31attackVector', 'v2accessVector', 'v31attackComplexity',
       'v2accessComplexity', 'v31privilegesRequired', 'v31userInteraction',
       'v31scope', 'v31confidentialityImpact', 'v2authentication',
       'v2confidentialityImpact', 'v31integrityImpact', 'v2integrityImpact',
       'v31availabilityImpact', 'v2availabilityImpact'],
       ========
       NOW THIS IS AN EXAMPLE OF A CVE PARAMETERS and the respective datatype example SO YOU CAN CREATE THE QUERIES ACCORDINGLY TO EXACTLY WHAT I WANT
       {output}
        ======
'''

messages = [{"role": "system",
             "content": q}]


def model(prompt):
    openai.api_key = "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"
    client = openai.OpenAI()
    while True:
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            max_tokens=150
        )
        
        answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        return answer
    