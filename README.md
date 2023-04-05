# qa_with_docs
Do a QA session with the docs provided as an input. Use langchain and OpenAI gpt-3.5 model as backend

The data that we want to query is present in the data folder. The data has been processed and stored in as an index file and the pickle file.
After the user inputs the query, the similar sentences are searched in the database using FAISS algorithm. The query and the similar sentences are then sent to the GPT-3.5 in the form of:
"Hey Assistant, I have this query {query}. Find me the answer to my query given the context {similar sentences}"
This prevents hallucination by the model as we give it the sources. 


https://user-images.githubusercontent.com/19887541/230017774-51fa34c7-a569-47f0-a03f-7b6fffa4172d.mov

