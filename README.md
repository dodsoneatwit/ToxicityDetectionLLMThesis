# ToxicityDetectionLLMThesis

## About

This project is an extension of a research thesis paper where we implement several GPT large language models
and compare their performance within different stages against Jigsaw's Toxic Comment Classification Challenge dataset. 
Each stage incorporates various techniques from advanced prompt engineering with few-shot learning, role-prompting, 
detailed and concise instructions, and retrieval augmented generation. In addition, we fine-tune these models to 
achieve further results with the main goal to enhance smaller GPT LLMs to perform on-par and/or better than the newer 
model of today. The following code includes our dataset retrieval, preprocessing phase, testing enhancement techniques 
with a few models, fine-tuning these models, incorporating RAG, and providing a space to test each model and their 
overall accuracy on a set size of comments. Lastly, with our final improvements made, we test our models against
untrained data to evaluate their performance on unseen data.

## Initial Setup

Install the latest version of Python at [python.org](https://www.python.org/downloads/)!

Create a python virtual environment for independency [python virtual env](https://docs.python.org/3/library/venv.html)

## Datasets Used

Toxic Comment Classification Challenge at [jigsaw-toxic-comment-classification-challenge](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge)

Jigsaw Unintended Bias in Toxicity Classification at [jigsaw-unintended-bias-in-toxicity-classification](https://www.kaggle.com/competitions/
jigsaw-unintended-bias-in-toxicity-classification)

Surge AI Toxicity Dataset at [surge-ai](https://github.com/surge-ai/toxicity/tree/main)

<b>NOTE:</b> some datasets may not be found due to them being too large for storing

## Program Spaces

The overall code is split into a few spaces depending on one's purposes. These include:

- The models space located inside of the library to view the implementation of enhancing each GPT
LLM: GPT-3.5-1106, GPT-3.5-0125, GPT-4o
- A space for preprocessing the main dataset (Toxic Comment Classification Challenge) and two others
for evaluating model performance on different types of data
- An organization of data where the evaluation and training sets, evaluation
prompts and formatted JSONs for fine-tuning are all located
- A general area for testing a single prompt, fine-tuning a single model, and testing accuracy against
a model can be executed

## Instructions for Using One's Own Data

If one wants to use their own data for testing along our implementation, simply head to the <b>lib</b>
folder and utilize the <b>chat</b>, <b>finetune</b>, <b>pinecone</b>, <b>accuracy_test</b>, <b>personal_preprocessing</b>,
and <b>testing</b> files for that usage. For certain files such as the preprocessing file, adjustments may 
need to made since every dataset labels their column values differently. Moreover, these should be small
adjustments and won't cause drastic errors who one's use-case.

## PIP commands for reference

<b>Separate Commands:</b>

- pip install os
- pip install openai
- pip install python-dotenv
- pip install nltk
- pip install pandas
- pip install tiktoken
- pip install numpy
- pip install langchain
- pip install langchain-pinecone
- pip install langchain-core
- pip install langchain-openai

<b>Single Line Command:</b> 

pip install os openai python-dotenv nltk pandas tiktoken numpy langchain langchain-pinecone langchain-core langchain-openai


## Author
- Elijah Dodson