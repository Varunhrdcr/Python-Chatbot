import os
import openai
import gradio as gr
share=True

openai.api_key = "API KEY"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant.",
def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text


def conversation_history(input,history):
    history=history or []
    s=list(sum(history,()))
    s.append(input)
    inp =' '.join(s)
    output = openai_create(inp)
    history.append((input,output))
    return history,history

block = gr.Blocks()

with block:
    chatbot=gr.Chatbot()
    message=gr.Textbox(placeholder=prompt)
    state=gr.State()
    submit=gr.Button("Click")
    submit.click(conversation_history,inputs=[message,state],outputs=[chatbot,state])

block.launch(debug=True)
