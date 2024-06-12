import random
import string
# র‍্যান্ডম পাসওয়ার্ড তৈরি করতে random এবং string মডিউল আমদানি করা হচ্ছে।

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # পাসওয়ার্ড তৈরির জন্য একটি ফাংশন সংজ্ঞায়িত করা হচ্ছে।

    # Define character pools
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    # যদি use_uppercase True হয়, তাহলে uppercase_chars এ সমস্ত uppercase অক্ষর রাখা হচ্ছে, নাহলে ফাঁকা স্ট্রিং।

    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    # যদি use_lowercase True হয়, তাহলে lowercase_chars এ সমস্ত lowercase অক্ষর রাখা হচ্ছে, নাহলে ফাঁকা স্ট্রিং।

    digits = string.digits if use_digits else ''
    # যদি use_digits True হয়, তাহলে digits এ সমস্ত ডিজিট রাখা হচ্ছে, নাহলে ফাঁকা স্ট্রিং।

    special_chars = string.punctuation if use_special else ''
    # যদি use_special True হয়, তাহলে special_chars এ সমস্ত স্পেশাল ক্যারেক্টার রাখা হচ্ছে, নাহলে ফাঁকা স্ট্রিং।

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

# Example usage
if __name__ == "__main__":
    # স্ক্রিপ্টটি সরাসরি চালানো হলে নিম্নলিখিত কোডটি কার্যকর হবে।

    length = int(input("Enter the desired password length: "))
    # ব্যবহারকারীর কাছ থেকে পাসওয়ার্ডের দৈর্ঘ্য ইনপুট হিসেবে নেওয়া হচ্ছে এবং তা ইন্টিজারে রূপান্তর করা হচ্ছে।

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    # ব্যবহারকারীর কাছে uppercase অক্ষর অন্তর্ভুক্ত করা হবে কিনা জিজ্ঞাসা করা হচ্ছে, ইনপুটটি ছোট হরফে রূপান্তরিত করে এবং হ্যাঁ হলে True সেট করা হচ্ছে।

    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    # ব্যবহারকারীর কাছে lowercase অক্ষর অন্তর্ভুক্ত করা হবে কিনা জিজ্ঞাসা করা হচ্ছে, ইনপুটটি ছোট হরফে রূপান্তরিত করে এবং হ্যাঁ হলে True সেট করা হচ্ছে।

    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    # ব্যবহারকারীর কাছে ডিজিট অন্তর্ভুক্ত করা হবে কিনা জিজ্ঞাসা করা হচ্ছে, ইনপুটটি ছোট হরফে রূপান্তরিত করে এবং হ্যাঁ হলে True সেট করা হচ্ছে।

    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    # ব্যবহারকারীর কাছে স্পেশাল ক্যারেক্টার অন্তর্ভুক্ত করা হবে কিনা জিজ্ঞাসা করা হচ্ছে, ইনপুটটি ছোট হরফে রূপান্তরিত করে এবং হ্যাঁ হলে True সেট করা হচ্ছে।

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    # উপরের ইনপুটগুলি ব্যবহার করে পাসওয়ার্ড তৈরি করা হচ্ছে।

    print(f"Generated password: {password}")
    # তৈরি করা পাসওয়ার্ডটি প্রিন্ট করা হচ্ছে।
