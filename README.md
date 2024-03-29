# FCUP-HACKATHON2024-v3zados

## Introduction

Welcome to the FCUP-HACKATHON2024-v3zados project repository!

This project aims to leverage Large Language Model (LLM) capabilities, particularly OpenAI's GPT-3.5 API, to enhance intelligence in handling Common Vulnerabilities and Exposures (CVEs).

By utilizing data from the National Vulnerability Database (NVD), we've endeavored to develop interactive methods for extracting insights from CVEs:
Our primary focus has been on employing AI to answer questions and provide deeper understanding regarding specific CVEs.
The second thing was creating a dataset with ~10k entries to make a more advanced search using user input,(for example, you could the agent to show the CVEs within a daterange).

Additionally, we explored the feasibility of predicting CVE vulnerability scores solely based on textual descriptions, using a logistic regression.

## Getting Started

To run the code, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by executing the following command in your terminal:

pip install -r requirements.txt

3. Generate a OPEN API key ( probably it will expire at the time of the presentation so you will need to generate one )
(note that also the is a nvdlib related API code that you can use, or generate your own)


3. Run the app.py code to open the fron-end part of the program, where you can search per specific CVE-ID to have some general informations about that CVE and then you can ask questions about it (for instance, you can ask "When was the attack?", or "What was the score of that CVE?".

4. We did a model to classify the CVE score but we couldn't implement in the front-end on time, but it's there :)

It's recommended to set up a new environment to ensure clean dependencies.

## Collaborators

This project was made possible through the collaborative efforts of the following individuals:

- Daniel Dias
- Lucas Santiago
- Rafael Conceição

## Useful Links

To delve deeper into the technologies and resources we utilized, consider exploring the following links:

- [OpenAI Platform Usage](https://platform.openai.com/usage)
- [National Vulnerability Database (NVD)](https://nvdlib.com/en/latest/v2/CVEv2.html#searching-cves)
- [Harness the Power of LLMs: Extracting Data from Legacy Documents](https://medium.com/@brightestlights/harness-the-power-of-your-how-to-extract-data-from-legacy-documents-using-llms-2841f5835359)

Feel free to explore the codebase and contribute to further advancements in CVE intelligence leveraging LM technologies!
