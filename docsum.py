import argparse
import chardet
import os
from groq import Groq  # Assuming you have a Groq client library
import fulltext

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

# Function to extract text from the file using fulltext and fallback to chardet if necessary
def extract_text(file_path):
    try:
        # Try using fulltext to extract text from the file
        return fulltext.get(file_path)
    except (UnicodeDecodeError, Exception) as e:
        print(f"fulltext failed: {e}")
        print("Attempting to detect encoding with chardet...")

        # Fallback to using chardet to detect encoding and read the file
        try:
            return read_file_with_encoding(file_path)
        except Exception as e:
            print(f"Failed to read the file even after detecting encoding: {e}")
            exit(1)

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# Read the document text using fulltext or chardet as a fallback
text = extract_text(args.filename)

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

# Combine chunk summaries into a single paragraph summary
final_summary_prompt = "Summarize the following summaries into a single paragraph:\n" + " ".join(chunk_summaries)
final_summary = summarize_chunk(final_summary_prompt)

# Print the final single-paragraph summary
print("\nFinal Summary:")
print(final_summary.strip())

