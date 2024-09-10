# Groq AI Document Summarizer

# docsum ![](https://github.com/alexcnsf/docsum/workflows/tests/badge.svg)

I developed a docuemnt summarizier, `docsum.py`,  using GROQ's cutting-edge, low-latency LLM API to summarize documents of any size and text type. It is a python script that recursively splits and summarizes texts into inputtable sizes to summarize documents of anything length while abiding by Groq's token limit. 

## Notes

- **Requirements**: All requirements and dependencies are listed in the up-to-date requirements.txt file.
- **API Key** You have ot create your own [Groq API key](https://groq.com) and store it as GROQ_API_KEY in your `.env` file (e.g. `GROQ_API_KEY=your_key_here`) and you must initialize the enviromental variable using code: ``` $ export $(cat .env) ``` 

## Usage

Upload a summarize any document you want and summarize using the the line of code ``` $ python3 docsum.py /file/path/to/document ```

## Example

A summarization of the Mexican Constitution looks like:

``` The Mexican Constitution outlines the country's fundamental laws and structure of government, including the powers and limitations of the federal government, states, and citizens, as well as individual rights and freedoms. It establishes the executive, legislative, and judicial branches, and guarantees rights such as due process, freedom of expression, and the right to vote. The Constitution also governs the relationship between the federal government and states, and sets out the responsibilities of public servants, including the President of Mexico, the Supreme Court of Justice, and state governments. Additionally, it establishes labor laws, including the right to a minimum wage, equal pay for equal work, and protection from mistreatment by employers, as well as addressing agrarian reform and the repeal of unconstitutional laws. ```

Reach out or raise an issue if you have any questions or improvements!
