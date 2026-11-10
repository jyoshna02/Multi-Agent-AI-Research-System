import re


def fact_check_agent(research_result, claims):

    # Collect content from all research sources
    sources = research_result.get("sources", [])

    # Store fact-checking results
    fact_check_results = []

    # Common words that are not useful for matching
    stop_words = {
        "the", "is", "a", "an", "and", "or",
        "to", "of", "in", "on", "for", "with",
        "are", "can", "that", "this", "it",
        "all", "does", "do", "did", "was",
        "were", "be", "been", "being", "as",
        "by", "from", "at", "their", "they"
    }

    # Check each claim separately
    for claim in claims:

        # Extract meaningful words
        words = set(
            re.findall(r"\b[a-zA-Z]+\b", claim.lower())
        )

        important_words = words - stop_words

        matched_sources = []
        matched_words = set()

        # Check each source individually
        for index, source in enumerate(sources, start=1):

            content = source.get("content", "").lower()

            source_words = set(
                re.findall(r"\b[a-zA-Z]+\b", content)
            )

            matches = important_words.intersection(source_words)

            if matches:
                matched_sources.append(index)
                matched_words.update(matches)

        # Calculate evidence keyword overlap
        if important_words:
            match_percentage = (
                len(matched_words) / len(important_words)
            ) * 100
        else:
            match_percentage = 0

        # Assign cautious evidence status
        if match_percentage >= 60 and matched_sources:
            status = "Possible evidence match - manual verification required"
        else:
            status = "Insufficient keyword evidence - needs review"

        # Save results
        fact_check_results.append({
            "claim": claim,
            "status": status,
            "match_percentage": round(match_percentage, 2),
            "matched_words": sorted(matched_words),
            "matched_sources": matched_sources
        })

    return fact_check_results