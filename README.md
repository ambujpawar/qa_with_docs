# qa_with_docs
Do a QA session with the docs provided as an input. Use langchain and OpenAI gpt-3.5 model as backend

The data that we want to query is present in the data folder. The data has been processed and stored in as an index file and the pickle file. After the user inputs the query, the similar sentences are searched in the database using FAISS algorithm. The query and the similar sentences are then sent to the GPT-3.5 in the form of:

```
"Hey Assistant, I have this query {query}. Find me the answer given the context {similar sentences}"
```

GPT-3.5 constructs sentences based on this and gives us answer in the Natural Language.


https://user-images.githubusercontent.com/19887541/230017774-51fa34c7-a569-47f0-a03f-7b6fffa4172d.mov


Using Gradio frontend

https://user-images.githubusercontent.com/19887541/230767103-defb3d22-9430-46c5-8102-8fdc087d18ab.mov

