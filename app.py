import gradio as gr
from calculator import Calculator

def calculator_demo(num1, operation, num2):
    calc = Calculator()
    try:
        if operation == "add":
            result = calc.add(num1, num2)
        elif operation == "subtract":
            result = calc.subtract(num1, num2)
        elif operation == "multiply":
            result = calc.multiply(num1, num2)
        elif operation == "divide":
            result = calc.divide(num1, num2)
        history = calc.get_history()
        return result, history
    except ValueError as e:
        return str(e), []

demo = gr.Interface(fn=calculator_demo, inputs=[gr.Number(label="Number 1"), gr.Dropdown(choices=["add", "subtract", "multiply", "divide"], label="Operation"), gr.Number(label="Number 2")], outputs=[gr.Number(label="Result"), gr.Textbox(label="History")], title="Simple Calculator")
demo.launch()