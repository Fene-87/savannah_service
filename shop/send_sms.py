import africastalking

username = 'sandbox'
api_key = '8a98028e205ac56d5ba81d1aa2b7caa1a6ce85e5f516c0924abffccb3ec1ebc0'

sms = africastalking.SMS


class send_sms():
    def sending(self):
        recipients = ["+254713129863"]
        message = "Order created successfully";
        sender = "Savannah orders"
        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')