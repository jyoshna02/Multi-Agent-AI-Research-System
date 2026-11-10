from ddgs import DDGS

def search_web(query, max_results=5):

    query = query.strip()

    if not query:
        raise ValueError("Please enter a search topic.")

    print("\nDuckDuckGo Search Started!")
    print("Searching for:", query)

    try:
        search_results = DDGS().text(
            query,
            max_results=max_results
        )

        results = []

        for item in search_results:
            results.append({
                "title": item.get("title", ""),
                "url": item.get("href", ""),
                "content": item.get("body", "")
            })

        return results

    except Exception as error:
        raise RuntimeError(
            f"DuckDuckGo search failed: {error}"
        ) from error