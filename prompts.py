with open('faqs.txt', 'r', encoding='utf-8') as f:
    FAQ_CONTEXT = f.read()

def get_response_prompt(history, user_query):
    formatted_history = "\n".join([f"{sender}: {message}" for sender, message in history])

    prompt = f"""
You are a helpful and friendly AI customer support agent for a company in India.
Your goal is to answer customer questions accurately based ONLY on the information provided in the CONTEXT below.
Do not make up information. If the answer is not in the provided CONTEXT, you MUST say "I'm sorry, I don't have that information. Would you like me to connect you with a human agent?"

CONTEXT:
---
{FAQ_CONTEXT}
---

Here is the conversation history so far:
HISTORY:
---
{formatted_history}
---

Now, please answer the following customer query:
Customer: {user_query}
AI Agent:
"""
    return prompt

def get_summary_prompt(history):
    """Generates the prompt for summarizing a conversation for escalation."""
    formatted_history = "\n".join([f"{sender}: {message}" for sender, message in history])
    prompt = f"""
Please provide a concise, one-paragraph summary of the following customer support conversation for a human agent.
Focus on the customer's main issue and what they have asked for.

CONVERSATION:
---
{formatted_history}
---

Summary for agent:
"""
    return prompt