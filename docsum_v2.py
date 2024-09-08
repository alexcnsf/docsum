import argparse
import chardet
import os
from groq import Groq  # Assuming you have a Groq client library

# Function to detect encoding using chardet
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

# Function to read the file with detected encoding
def read_file_with_encoding(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# Read the document text with detected encoding
text = read_file_with_encoding(args.filename)

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Define CHUNK_SIZE for splitting the text
CHUNK_SIZE = 3000  # You can adjust this value based on your needs

# Define the summary prompt (no changes here)
SUMMARY_PROMPT = "Please summarize this text."

# Function to chunk text into smaller parts
def chunk_text(text, chunk_size):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

# Summarize each chunk
def summarize_chunk(chunk):
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': SUMMARY_PROMPT},
            {'role': 'user', 'content': chunk},
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Break the text into chunks
chunks = list(chunk_text(text, CHUNK_SIZE))

# Summarize each chunk
chunk_summaries = []
for chunk in chunks:
    summary = summarize_chunk(chunk)
    chunk_summaries.append(summary)

# Combine chunk summaries into a single paragraph summary (as you had it)
final_summary_prompt = "Summarize the following summaries into a single paragraph:\n" + " ".join(chunk_summaries)
final_summary = summarize_chunk(final_summary_prompt)

# Print the final single-paragraph summary
print("\nFinal Summary:")
print(final_summary.strip())

