from transformers import GPT2LMHeadModel, GPT2Tokenizer

class TextGenerator:
    def __init__(self):
        # Load pre-trained GPT-2 model and tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_paragraph(self, seed_text, max_length=100):
        # Encode the input text
        input_ids = self.tokenizer.encode(seed_text, return_tensors='pt')
        
        # Generate text using the model
        output = self.model.generate(
            input_ids, 
            max_length=max_length, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2, 
            top_p=0.92, 
            temperature=0.75,
            do_sample=True,
            top_k=50
        )

        # Decode the generated text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text
