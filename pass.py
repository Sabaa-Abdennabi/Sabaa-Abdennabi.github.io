from flask import Flask, render_template
import random

app = Flask(__name__)

file_path = 'passwords.txt'  # Adjust the file name

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

passwords = read_passwords_from_file(file_path)

def generate_random_password():
    global passwords
    if passwords:
        random_password = random.choice(passwords)
        passwords.remove(random_password)
        return random_password
    else:
        return "No more passwords available."

@app.route('/')
def generate_password():
    random_password = generate_random_password()
    return render_template('index.html', password=random_password)

if __name__ == "__main__":
    app.run(debug=True)
