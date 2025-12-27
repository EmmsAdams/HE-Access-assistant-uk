# HE Access Assistant (UK)

A decision-support web app to help asylum seekers and refugees explore UK higher education routes.  
Users can enter their qualifications and receive an approximate UK level mapping, a recommended pathway, and a personalised checklist of next steps.

**Important:** This tool gives guidance only. It is **not** official qualification recognition, and it does **not** offer legal advice. Always check outcomes with university admissions and official qualification comparison services.
---

## Features
- Qualification input (country + qualification name + completion status)
- Approximate mapping to likely UK education level with a confidence indicator
- Recommended study route (Access to HE, Foundation Year, Undergraduate entry)
- Personalised next-steps checklist with downloadable text file
- Clear signposting to official verification routes

---

## How it works (simple explanation)
1. The app looks for a close match in a small qualification mapping table (`data/qualification_mappings.csv`).
2. It returns a **likely** UK level and a **confidence** rating (Low/Medium/High).
3. A rules-based recommender suggests a pathway and generates a checklist.

---

## Tech Stack
- Python
- Streamlit
- pandas

---

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
