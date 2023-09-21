import google.generativeai as palm

palm.configure(api_key="API Key")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
                        {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
                        {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
                        {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
                        {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
                        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2}],
}

prompt = input("On which topic would you like me to write a poem ? ")

response = palm.generate_text(
    **defaults,
    prompt="Write a poem about " + prompt
)
print(response.result)
