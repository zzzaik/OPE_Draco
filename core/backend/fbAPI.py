'''
import facebook

graph = facebook.GraphAPI(access_token="EAAPgbdQV4VkBABF5pu2sm0oqaIwbKZBkIFre8XjCfR583ZCeo0zFDMUz8uOyy6a236bYDDOmlfZCZB25MjMOY3WPsT8PrN7UlJOyLhR5kt4PhvFme2djyeooMmQs2JvEna3mIJ6VQ31nZBxjHvXjthq9S3p2LALt12pem1vWCaTzVF81BgM1QltJQxgSoe30ku77FlNEbBgZDZD", version="2.12")


def postar():
    graph.put_photo(image=open('/home/zzzaik/OPE_Draco/core/static/img/testes2.png', 'rb'), message='Look at this cool photo!')
'''