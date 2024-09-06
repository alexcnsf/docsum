import os
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key="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",
)

filename = 'docs/declaration'
with open(filename) as f:
	text = f.read()

chat_completion = client.chat.completions.create(
    messages=[
	{
	'role':'system',
	'content':'Summarize the input text below and give me a summary of what it says in spanish at a very easy level of vocabulary',
}
,
        {
            "role": "user",
            "content": text,
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
