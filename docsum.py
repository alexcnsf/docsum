import os
from dotenv import load_dotenv
from groq import Groq
import argparse
import fulltext

#load_dotenv()
#api_key = os.getenv('GROQ_API_KEY')

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

text = fulltext.get(args.filename)

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

# filename = 'docs/declaration'
#with open(filename) as f:
#	text = f.read()

chat_completion = client.chat.completions.create(
    messages=[
	{
	'role':'system',
	'content':'Summarize the input text below and give me a summary of what it says on a 5th grade level',
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
