from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

PROMPT = '''
You are BiblAI - a chatbot designed to discuss the Bible and its contents. You will talk to the human conversing with you and provide meaningful answers as they ask questions.
Avoid saying things like "how can I help you?".
Be social and engaging while you speak, and be very philosophic and thoughtful.

Use appropriate language and encouraging statements.
Don't make your answers so long unless you are asked to.
Don't repeat an identical answer if you have given it in the past.
Be honest, if you can't answer something, tell the human that you can't provide an answer.
Use the following pieces of MemoryContext to answer the question at the end. 
---
MemoryContext: {context}
---
'''

def train(out_file='index.json'):
    docs = SimpleDirectoryReader('scripture', recursive=True).load_data()
    index = GPTSimpleVectorIndex(docs)
    index.save_to_disk(out_file)
    return index

def ask(index, question: str, messages: list = None):
    if messages in (None, []):
        TEMPLATE = PROMPT
    else:
        TEMPLATE = '---\nMemoryContext: {context}\n---\n'
    context = []
    query = index.query(question)
    for node in query.source_nodes:
        context.append(f'Context {node.doc_id}: {node.source_text}')
    messages.append({'role': 'system', 'content':TEMPLATE.format(context='\n\n'.join(context))})
    # add user question
    messages.append({'role': 'user', 'content': question})
    resp = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    text = resp['choices'][0]['message']['content']
    messages.append({'role': 'assistant', 'content': text})
    return text, messages

'''
if __name__ == '__main__':
    if os.path.exists('index.json'):
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
    else:
        print('building index')
        index = train()

    hist = []
    print('Welcome to BiblAI - a chatbot that knows its scripture')
    while True:
        q = input('User > ')
        print('[*] Generating response...')
        res, hist = ask(index, q, messages=hist)
        print('BiblAI >', res)
'''