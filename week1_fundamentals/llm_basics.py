#goolge/flan was providing inaccurate results
# from transformers import pipeline

# generator = pipeline("text2text-generation", model="google/flan-t5-base")

# def ask_question(question, max_len=40):
#     prompt  = f"Answer the following question concisely: {question}"
#     response = generator(prompt, max_length=max_len)
#     return response[0]['generated_text']

# questions = [
#     'What is the capital of France?',
#     'Explain what word embeddings are in simple terms.',
#     'Who wrote Hamlet?'

# ]
# for q in questions:
#     answer = ask_question(q)
#     print(f"Question: {q}")
#     print(f"Answer:{answer}")

#OpenAI API didn't work as I was already out of quota 
# from openai import OpenAI

# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5",
#     input="What is the capital of the France?"
# )

# print(response.output_text)

#to use gemini install following
#pip install -q -U google-genai

from google import genai
from google.genai import types
client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )

"""
2.5 Flash and Pro models have "thinking" enabled by default to enhance quality, which may take longer to run and increase token usage.

When using 2.5 Flash, you can disable thinking by setting the thinking budget to zero.
"""

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="How does AI work?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0)
#     )

# )

"""
By default, the model returns a response only after the entire generation process is complete.

For more fluid interactions, use streaming to receive GenerateContentResponse instances incrementally as they're generated.
"""

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")