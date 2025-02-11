def paragraph(text):
    char_count = len(text)
    word_count = len(text.split())
    line_count = text.count('\n')

    return char_count, word_count, line_count


s = """Artificial Intelligence (AI) is a field of computer science focused on developing machines 
and software capable of mimicking human intelligence. AI enables computers to perform tasks that typically 
require human cognition, such as learning, reasoning, problem-solving, and decision-making. AI systems use 
techniques like machine learning (ML), deep learning, and neural networks to process vast amounts of data 
and improve their performance over time. 

Machine learning, a subset of AI, allows systems to recognize patterns and make predictions based on data, 
while deep learning uses artificial neural networks to handle complex tasks such as image recognition, 
speech processing, and natural language understanding. AI is classified into two main types: narrow AI, which 
specializes in specific tasks like virtual assistants (e.g., Siri, Alexa) and recommendation systems (e.g., 
Netflix, Amazon), and general AI, which, if achieved, would possess human-like intelligence capable of reasoning 
and problem-solving across various domains.

AI is transforming multiple industries, including healthcare, finance, automotive, and cybersecurity. In healthcare, 
AI assists in diagnosing diseases, predicting patient outcomes, and automating administrative tasks. In finance, 
AI-driven algorithms analyze market trends, detect fraudulent transactions, and optimize investment strategies. 
Self-driving cars use AI to process sensor data, recognize objects, and make real-time decisions to navigate 
roads safely. AI-powered chatbots and virtual assistants enhance customer service by providing personalized 
and instant responses."""

char_count, word_count, line_count = paragraph(s)
print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"lines: {line_count}")
