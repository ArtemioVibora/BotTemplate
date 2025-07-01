import json
import os

class ChatBot:

    def __init__(self, faq_file="faq.json", voice_enabled=True):
        self.faq_file = faq_file
        self.voice_enabled = voice_enabled
        self.responses = self.load_faq()
        print("Chatbot now running!")

    def load_faq(self):
        with open(self.faq_file, "r") as f:
            raw = json.load(f)
        return {
            tuple(map(str.strip, key.split(","))): value
            for key, value in raw.items()
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keywords, reply in self.responses.items():
            if any(keyword in user_input for keyword in keywords):
                if self.voice_enabled:
                    self.speak(reply)
                return reply
        return "Sorry, I dont understand!"

    def speak(self, text):
        os.system(f'espeak "{text}"')

    def reload_faq(self):
        self.responses = self.load_faq()
