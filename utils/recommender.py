def recommend_pathway(mapping, completed, english):
    reasons = []

    if mapping is None:
        route = "Access to HE or Foundation Year"
        reasons.append("Qualification could not be reliably mapped.")
    else:
        level = mapping["likely_uk_level"].lower()
        if "level 3" in level:
            route = "Undergraduate entry or Foundation Year"
        else:
            route = "Access to HE or Foundation Year"

        reasons.append(f"Mapped to {mapping['likely_uk_level']} with {mapping['confidence']} confidence.")

    if completed == "No":
        reasons.append("Incomplete qualification — universities may request foundation or RPL assessment.")

    if english != "Yes":
        reasons.append("English language requirements may apply (IELTS or pre-sessional).")

    return route, reasons


def build_checklist():
    return [
        "Identify 2–3 universities with widening participation or refugee support.",
        "Prepare personal statement explaining background and motivation.",
        "Gather certificates and transcripts.",
        "Request an academic or professional reference.",
        "Check English language requirements.",
        "Contact admissions for qualification verification (e.g., UK ENIC)."
    ]
