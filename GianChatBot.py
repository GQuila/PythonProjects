import tkinter as tk

# Define a simple rule-based chatbot
def get_response(user_message):
    responses = {
        'hello': 'Hi there!',
        'how are you': 'I am good, thank you!',
        'bye': 'Goodbye! Have a great day!',
    }
    user_message = user_message.lower()
    for key in responses:
        if key in user_message:
            return responses[key]
    return "I don't understand that."

# Function to handle sending messages
def send_message():
    user_message = user_input.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f'You: {user_message}\n')
    chat_log.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)
    
    # Get the chatbot's response
    bot_response = get_response(user_message)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f'Bot: {bot_response}\n')
    chat_log.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title('Chatbot')

# Create a chat log area
chat_log = tk.Text(root, state=tk.DISABLED, height=20, width=50)
chat_log.pack(padx=10, pady=10)

# Create an entry widget for user input
user_input = tk.Entry(root, width=50)
user_input.pack(padx=10, pady=10)

# Create a send button
send_button = tk.Button(root, text='Send', command=send_message)
send_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
