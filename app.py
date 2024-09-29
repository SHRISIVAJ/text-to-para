from flask import Flask, request, render_template
from text_generator import TextGenerator
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Create the upload folder if it doesn't exist

# Initialize the Text Generator using GPT-2
text_gen = TextGenerator()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # If input_text is provided in the form, use it
        if 'input_text' in request.form and request.form['input_text'].strip():
            input_text = request.form['input_text']
            generated_paragraph = text_gen.generate_paragraph(input_text, max_length=200)
            return render_template('index.html', input_text=input_text, output_text=generated_paragraph)

        # If a file is uploaded, read its contents
        if 'file' in request.files:
            uploaded_file = request.files['file']
            
            # Check if a file is actually selected
            if uploaded_file.filename != '':
                # Save the uploaded file
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
                uploaded_file.save(file_path)
                
                # Read the contents of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                
                # Generate a paragraph based on the file content
                generated_paragraph = text_gen.generate_paragraph(file_content, max_length=200)
                return render_template('index.html', input_text=file_content, output_text=generated_paragraph)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
