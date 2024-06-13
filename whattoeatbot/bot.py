import random
from enum import Enum, auto


class ConversationState(Enum):
    """Enum for the state of the conversation."""

    GREETING = auto()
    ASKING_CUISINE_KIND = auto()
    ASKING_CUISINE = auto()
    RESPONDED = auto()


class Bot:
    """Bot class to handle conversation responses"""

    def __init__(self):
        self.state = ConversationState.GREETING
        self.cuisine_kind = None
        self.random_cuisine = None

    def chat(self, message: str) -> str:
        """Respond to a message."""

        if self.state == ConversationState.GREETING:
            self.state = ConversationState.ASKING_CUISINE_KIND
            return "Hello! What type of cuisine are you in the mood for? (you can say 'anything' or 'healthy')"

        elif self.state == ConversationState.ASKING_CUISINE_KIND:
            if message.lower() in ["anything", "healthy"]:
                self.state = ConversationState.ASKING_CUISINE
                self.cuisine_kind = message.lower()

                # Choose a random cuisine based on the user's preference
                cuisine_options = self.get_cuisines(message.lower())
                self.random_cuisine = random.choice(cuisine_options)
                return f"Great! How about some {self.random_cuisine} food? (yes/no)"

            else:
                return "I'm sorry, I didn't understand that. Please try again."

        elif self.state == ConversationState.ASKING_CUISINE:
            if message.lower() == "no":
                self.random_cuisine = random.choice(
                    self.get_cuisines(self.cuisine_kind)
                )
                return f"How about some {self.random_cuisine} food instead? (yes/no)"

            elif message.lower() == "yes":
                self.state = ConversationState.RESPONDED
                return f"Great choice! Here's a link to a {self.random_cuisine} restaurant: {self.get_google_maps_link(self.random_cuisine)}"

            else:
                return "I'm sorry, I didn't understand that. Please try again."

        else:
            return "I'm sorry, I didn't understand that."

    def get_cuisines(self, kind: str):
        """Return all hard-coded available cuisines."""
        if kind == "anything":
            return [
                "Italian",
                "Mexican",
                "Chinese",
                "Japanese",
                "Indian",
                "Singaporean",
                "Salad",
                "Vegetarian",
            ]
        elif kind == "healthy":
            return ["Salad", "Vegetarian"]

    def get_google_maps_link(self, cuisine: str):
        """Return a Google Maps link for a restaurant with the given cuisine."""
        return f"https://www.google.com/maps/search/?api=1&query={cuisine}+restaurant"
