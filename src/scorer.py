def score(similarity_score):
    if similarity_score >= 80:
        return "Great Match"
    elif similarity_score >= 60:
        return "Good Match"
    elif similarity_score >= 40:
        return "Moderate Match"
    else:
        return "Weak Match"