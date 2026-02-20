Speedrun Wiki is a tool designed to find the shortest path between two Wikipedia articles using Semantic Analysis instead of random clicking.

This project is currently a Work in Progress.

Scrape: Uses BeautifulSoup to pull content from a starting Wikipedia page.

Extract: Identifies all internal links within the article.

Embed: Converts links and the target goal into vector embeddings.

Analyze: Calculates the cosine similarity (distance) between the current links and the destination.

Navigate: Automatically selects the link semantically closest to the goal.