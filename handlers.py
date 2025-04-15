import nltk
from services import Services


class Handlers:
    def __init__(self):
        self.mattbot_services = Services()

    def handle_user_query(self, user_response_received):
        response = user_response_received.response
        response = response.lower()
        if response != "bye":
            if (
                response == "thanks"
                or response == "thank you"
                or response == "thankyou"
            ):
                return "Anytime ..."
            else:
                greetings = self.mattbot_services.greetings(response)
                if greetings != None:
                    return greetings
                else:
                    self.mattbot_services.sentence_token.append(response)
                    chatbot_response = self.mattbot_services.response()
                    self.mattbot_services.sentence_token.remove(response)
                    return chatbot_response
