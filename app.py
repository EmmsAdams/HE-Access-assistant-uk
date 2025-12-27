import streamlit as st
import pandas as pd
from utils.mapping import find_mapping
from utils.recommender import recommend_pathway, build_checklist

st.set_page_config(page_title="HE Access Assistant UK", page_icon="🎓")

st.title("🎓 HE Access Assistant (UK)")
st.caption("Guidance tool for asylum seekers and refugees exploring UK higher education.")
st.warning("This tool provides approximate guidance only. It is not official qualification recognition or legal advice.")

df = pd.read_csv("data/qualification_mappings.csv")

st.header("Your Qualifications")
country = st.text_input("Country of qualification")
qualification = st.text_input("Qualification name")
completed = st.selectbox("Completed qualification?", ["Yes", "No"])
english = st.selectbox("English proficiency evidence?", ["Yes", "No", "Not sure"])

mapping = find_mapping(df, country, qualification)

st.header("Qualification Mapping (Approximate)")
if mapping:
    st.success("Possible match found")
    st.write("Likely UK Level:", mapping["likely_uk_level"])
    st.write("Confidence:", mapping["confidence"])
    st.write("Notes:", mapping["note"])
else:
    st.info("No reliable match found. Verification needed.")

route, reasons = recommend_pathway(mapping, completed, english)

st.header("Recommended Pathway")
st.write(route)

st.subheader("Why")
for r in reasons:
    st.write("-", r)

st.header("Next Steps Checklist")
checklist = build_checklist()
st.text_area("Checklist", value="\n".join(f"- {c}" for c in checklist), height=200)

st.download_button(
    "Download Checklist",
    "\n".join(checklist),
    file_name="he_access_checklist.txt"
)
