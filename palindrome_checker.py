import gradio as gr
import re

# Palindrome checking function
def is_palindrome_ai(input_text):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', input_text.lower())

    # Check palindrome logic
    if s == s[::-1]:
        return f"✅ Yes! '{input_text}' is a palindrome."
    else:
        return f"❌ No, '{input_text}' is not a palindrome."

# Gradio UI
iface = gr.Interface(
    fn=is_palindrome_ai,
    inputs=gr.Textbox(lines=2, placeholder="Enter text to check..."),
    outputs="text",
    title="🤖 AI Palindrome Checker",
    description="Ask me if a word or sentence is a palindrome! I’ll check it intelligently for you.",
    theme="default"
)

# Launch the app
iface.launch()

