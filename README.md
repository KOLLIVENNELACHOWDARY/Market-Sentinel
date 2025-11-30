# ** **Market-Sentinel** **

## Overview

This project implements a **multi-agent AI system** that can analyze business or technology domains by gathering information, extracting claims, fact-checking, summarizing news, identifying competitors, and generating a final strategy report.  

It leverages **Google’s Gemini LLM** and custom agent orchestration for sequential or parallel execution of tasks, providing actionable insights and strategic guidance for founders or analysts.

---

## Features

1. **Research Agent**
   - Extracts information on a topic using web search or knowledge retrieval.
   - Summarizes key insights for further analysis.

2. **Claim Extraction**
   - Identifies factual claims from raw text.
   - Outputs claims in a structured JSON format.

3. **Fact-Checker**
   - Validates extracted claims using external sources.
   - Highlights unverified or false claims.

4. **Competitor Analysis**
   - Identifies competitors and their strategies in the chosen domain.
   - Summarizes key points for market positioning.

5. **News Summary**
   - Collects recent news from technology/business domains.
   - Provides summaries with founder-focused insights.

6. **Final Strategy**
   - Aggregates outputs from all agents.
   - Generates a **comprehensive strategy report** with opportunities, risks, and actionable recommendations.

7. **Flexible Execution**
   - Agents can run **sequentially** or in **parallel** using an in-memory runner.
   - Outputs structured JSON for further processing.

---

## Technology Stack

- **Language:** Python 3.12+
- **LLM:** Google Gemini (2.5 flash-lite)
- **Agents & Runners:** Google ADK (`google.adk.agents`, `google.adk.runners`)
- **Tools:** Google Search integration
- **Platform:** Kaggle Notebook

---

## Installation and Usage

1. Clone the repository:

```bash
git clone https://github.com/KOLLIVENNELACHOWDARY/Market-Sentinel.git
cd ai-multi-agent-strategy
```
<br>
2.Install required packages:

```
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types
```
<br>
3. Set your Google API

```import os
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
```
<br>
4. Run all  Sub Agents, Root Agent 
<br>
<br>
5. Execute Runner
<br>
<br>
6. Sample input and ouput
<br>
<br>
INPUT

```
I want to start a toy business .. what will be it's status by 2030 ..
```

<br>
OUTPUT

```
StartupIntelligenceRoot > Here's a detailed report on the potential status of a toy business by 2030 and strategies for improvement:

**Toy Business Status by 2030:**

*   **Market Growth:** The global children's toy market is projected to grow significantly. One report estimates it will grow from $113.8 billion in 2023 to $142.6 billion by 2030, with a Compound Annual Growth Rate (CAGR) of 3.5%. Another forecast suggests the kids' toy market could reach $183.15 billion globally by 2030, growing at a CAGR of 5.1% from 2022.
*   **Rise of Sustainable Toys:** The sustainable toys market is expected to experience substantial growth, reaching approximately $59.6 billion by 2030, with a CAGR of 8.2%. This is driven by increasing environmental consciousness among consumers and concerns about the environmental impact of traditional plastic toys.
*   **Smart and Tech Toys:** Smart toys, incorporating technologies like AI, IoT, and augmented reality, are becoming mainstream and are a significant growth driver. The smart toys market is projected to grow from $10.84 billion in 2021 to $107.61 billion by 2030, with a high CAGR of 24.71%.
*   **Educational and STEM Toys:** There's a continued surge in demand for educational and STEM (Science, Technology, Engineering, and Mathematics) toys, as parents increasingly seek products that promote early learning and skill development.
*   **E-commerce Dominance:** Online channels are a key distribution method and are growing rapidly. The online sale of toys, including sustainable options, is expected to gain significant traction.

**How to Improve Your Toy Business:**

*   **Understand Your Customer:** Conduct thorough research into consumer behavior to understand customer needs and preferences. Build customer loyalty through excellent service and by exceeding purchase expectations. It's often effective to target children's desires while appealing to parents' purchasing power by highlighting benefits and quality.
*   **Product Strategy:**
    *   **Unique and Desirable Items:** Offer a unique product range and focus on quality over quantity. Consider sourcing exclusive items like handcrafted toys from local artisans or specialized eco-friendly brands to differentiate from large chains.
    *   **Diversify Offerings:** Expand into complementary categories to create multiple revenue streams and increase average transaction value.
    *   **Embrace Sustainability:** Offer sustainable or "green" toys made from organic materials. This aligns with growing consumer demand and environmental consciousness.
    *   **Incorporate Technology:** Explore offering smart toys that integrate AI or other advanced technologies for enhanced interactive play.
*   **Store and Online Presence:**
    *   **Optimized Store Layout:** Design your store with an appealing and easy-to-navigate layout. Highlight products effectively, possibly using eye-level displays and organizing by age group or toy type.
    *   **Engaging In-Store Experiences:** Create engaging in-store experiences, such as workshops or play areas for children, to attract customers and encourage longer visits.
    *   **Strong Online Presence:** Develop a professional website and maintain an active social media presence to build credibility, engage with customers, and gather data. Prioritize e-commerce as a distribution channel.
*   **Marketing and Sales:**
    *   **Targeted Marketing:** Develop marketing strategies that appeal to both children (e.g., bright colors, characters) and parents (e.g., emphasizing benefits, quality, and price).
    *   **Promotions and Discounts:** Offer strategic promotions and discounts, but remember that price isn't the only factor; service and quality are also crucial.
    *   **Leverage Local Partnerships:** Collaborate with local schools, libraries, or community centers for events and co-promotions to expand reach and build brand presence.
    *   **Build Customer Relationships:** Be polite, patient, welcoming, and show genuine concern for your customers to foster loyalty. Implement loyalty programs to encourage repeat business.
*   **Inventory Management:** Hold inventory on desired or high-demand stocks, especially for anticipated rushes like weekends and holidays.

By focusing on these strategies, you can position your toy business for success in the evolving market landscape.'''
