from transformers import pipeline

def generator(input_text, max_lenght, do_sample):
    generator = pipeline("text-generation", model='gpt2')
    generated_text = generator(input_text, max_lenght=max_lenght, do_sample=do_sample)
    return generated_text