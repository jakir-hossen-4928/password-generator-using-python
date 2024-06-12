from flask import Flask, render_template, request
# Flask থেকে প্রয়োজনীয় মডিউল আমদানি করা হচ্ছে:
# Flask - Flask অ্যাপ তৈরি করতে,
# render_template - HTML টেমপ্লেট রেন্ডার করতে,
# request - HTTP অনুরোধ পরিচালনা করতে।

#module (random and string)
import random
import string
# র‍্যান্ডম পাসওয়ার্ড তৈরি করতে random এবং string মডিউল আমদানি করা হচ্ছে।

app = Flask(__name__)
# Flask অ্যাপ্লিকেশন ইন্সট্যান্স তৈরি করা হচ্ছে।

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # পাসওয়ার্ড তৈরির জন্য একটি ফাংশন সংজ্ঞায়িত করা হচ্ছে।

    # Define character pools
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    # যদি uppercase ক্যারেক্টার ব্যবহার করা হয়, তাহলে uppercase_chars এ সমস্ত uppercase অক্ষর রাখা হচ্ছে।

    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    # যদি lowercase ক্যারেক্টার ব্যবহার করা হয়, তাহলে lowercase_chars এ সমস্ত lowercase অক্ষর রাখা হচ্ছে।

    digits = string.digits if use_digits else ''
    # যদি ডিজিট ব্যবহার করা হয়, তাহলে digits এ সমস্ত ডিজিট রাখা হচ্ছে।

    special_chars = string.punctuation if use_special else ''
    # যদি স্পেশাল ক্যারেক্টার ব্যবহার করা হয়, তাহলে special_chars এ সমস্ত স্পেশাল ক্যারেক্টার রাখা হচ্ছে।

    # Combine pools into a single string
    all_chars = uppercase_chars + lowercase_chars + digits + special_chars
    # সমস্ত ক্যারেক্টার পুল একত্রিত করে all_chars এ রাখা হচ্ছে।

    # Ensure there's at least one type of character to choose from
    if not all_chars:
        raise ValueError("At least one character type must be selected")
    # যদি কোন ক্যারেক্টার টাইপ নির্বাচিত না হয়, তাহলে একটি ValueError ত্রুটি উত্থাপন করা হচ্ছে।

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    # length অনুযায়ী all_chars থেকে র‍্যান্ডমভাবে ক্যারেক্টার নির্বাচন করে পাসওয়ার্ড তৈরি করা হচ্ছে।

    return password
    # তৈরি করা পাসওয়ার্ড রিটার্ন করা হচ্ছে।

@app.route('/', methods=['GET', 'POST'])
# রুট URL ('/') এর জন্য একটি রুট ডিফাইন করা হচ্ছে যা GET এবং POST উভয় অনুরোধ গ্রহণ করে।

def index():
    password = ''
    # প্রাথমিকভাবে password ভ্যারিয়েবল ফাঁকা স্ট্রিং হিসেবে সেট করা হচ্ছে।

    if request.method == 'POST':
        length = int(request.form['length'])
        # ফর্ম থেকে length ইনপুট সংগ্রহ করে তা ইন্টিজারে রূপান্তর করা হচ্ছে।

        use_uppercase = 'uppercase' in request.form
        # ফর্ম থেকে use_uppercase ইনপুট সংগ্রহ করা হচ্ছে।

        use_lowercase = 'lowercase' in request.form
        # ফর্ম থেকে use_lowercase ইনপুট সংগ্রহ করা হচ্ছে।

        use_digits = 'digits' in request.form
        # ফর্ম থেকে use_digits ইনপুট সংগ্রহ করা হচ্ছে।

        use_special = 'special' in request.form
        # ফর্ম থেকে use_special ইনপুট সংগ্রহ করা হচ্ছে।

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        # উপরের ইনপুটগুলি ব্যবহার করে পাসওয়ার্ড তৈরি করা হচ্ছে।

    return render_template('index.html', password=password)
    # index.html টেমপ্লেট রেন্ডার করা হচ্ছে এবং তৈরি করা পাসওয়ার্ডটি টেমপ্লেটে পাস করা হচ্ছে।

if __name__ == '__main__':
    app.run(debug=True)
    # যদি স্ক্রিপ্টটি সরাসরি চালানো হয়, তাহলে Flask অ্যাপটি ডিবাগ মোডে চালু করা হচ্ছে।
