from . import bot


def chat():
    """Chat locally with the bot through CLI."""

    # Initialize the bot
    chatbot = bot.Bot()

    # Start the conversation.
    # The conversation will continue until the state is ConversationState.RESPONDED
    response = chatbot.chat("")
    print(f"Bot: {response}")
    while chatbot.state != bot.ConversationState.RESPONDED:
        message = input("You: ")
        response = chatbot.chat(message)
        print(f"Bot: {response}")
