from flask import Flask, render_template, request

app = Flask(__name__)  

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += new_char
        else:
            result += char  
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        choice = request.form['choice']
        
        if choice == 'encrypt':
            result = caesar_cipher(text, shift)
        elif choice == 'decrypt':
            result = caesar_cipher(text, -shift)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 
