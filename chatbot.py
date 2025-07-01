import json
import os

class ChatBot:

    def __init__(self, faq_file="faq.json", voice_enabled=True):
        self.faq_file = faq_file
        self.voice_enabled = voice_enabled
        print("Chatbot now running!")

    def load_faq(self):
        with open(self.faq_file, "r") as f:
            raw = json.load(f)
        return {
            tuple(map(str.strip, key.split(","))): value
            for key, value in raw.items()
        }
