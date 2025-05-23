def evaluate_match(score: int) -> str:
    if score >= 85:
        return "Excellent match – likely to succeed"
    elif score >= 70:
        return "Good match – consider interviewing"
    elif score >= 50:
        return "Average match – may lack a few requirements"
    else:
        return "Low match – likely not a good fit"