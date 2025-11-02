import gradio as gr
from ollama import Client

client = Client(host='http://localhost:11434')


def translate(text):
    messages = [
        {
            "role": "system",
            "content": "あなたは英語から日本語への翻訳に特化した優秀なAIアシスタントです。回答は翻訳文にとどめ、日本語に翻訳するだけです。",
        },
        {
            "role": "user",
            "content": f"次の英語を日本語に翻訳して下さい。\n{text}",
        },
    ]
    stream = client.chat(
        model="gpt-oss:20b",
        messages=messages,
        stream=True,
    )

    result = ""
    for chunk in stream:
        result += chunk.message.content
        yield result


def main():
    app = gr.Interface(
        fn=translate,
        inputs=gr.Textbox(lines=10, max_lines=40, label="English"),
        outputs=gr.Textbox(lines=10, max_lines=40, show_copy_button=True, label="Japanese"),
        title="English to Japanese translation app",
        description="",
    )
    app.launch()


if __name__ == "__main__":
    main()
