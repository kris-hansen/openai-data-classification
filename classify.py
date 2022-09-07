import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

training = [["First Name", "Medium"], ["Last Name", "Medium"], ["IP Address", "Medium"], ["Address", "Medium"], ["City", "Medium"], ["State", "Medium"], 
    ["Zip Code", "Medium"], ["Phone Number", "Medium"], ["Email Address", "Medium"], ["Date of Birth", "High"], ["SSN", "Secret"], 
    ["Credit Card Number", "Secret"], ["Credit Card Expiration Date", "Secret"], ["Credit Card CVV", "Secret"], ["Bank Account Number", "High"], 
    ["Driver's License Number", "High"], ["Driver's License State", "High"], ["Driver's License Expiration Date", "High"], ["Passport Number", "High"],
    ["Passport Country", "High"], ["Passport Expiration Date", "High"], ["Mother's Maiden Name", "Medium"], ["Mother's Birth City", "Medium"],
    ["Bank Routing Number", "Medium"], ["Bank Account Type", "Medium"], ["Bank Account Balance", "Medium"], ["Bank Account Currency", "Medium"], 
    ["Bank Account Country", "Medium"], ["Bank Account Owner", "Medium"], ["Bank Account Owner Address", "Medium"], ["Bank Account Owner City", "Medium"], 
    ["Bank Account Owner State", "Medium"], ["Bank Account Owner Zip Code", "Medium"], ["Bank Account Owner Phone Number", "Medium"], 
    ["Bank Account Owner Email Address", "Medium"], ["Bank Account Owner Date of Birth", "Medium"], ["Bank Account Owner SSN", "Secret"], 
    ["Bank Account Owner Credit Card Number", "Secret"], ["Bank Account Owner Credit Card Expiration Date", "Secret"], ["Bank Account Owner Credit Card CVV", "Secret"], 
    ["Bank Account Owner Bank Account Number", "High"], ["Bank Account Owner Bank Routing Number", "Medium"], ["Bank Account Owner Bank Account Type", "Medium"], 
    ["Bank Account Owner Bank Account Balance", "Medium"], ["Bank Account Owner Bank Account Currency", "Medium"], ["Bank Account Owner Bank Account Country", "Medium"]]

# take in a query via command line
query = input("Enter a query: ")

predict = openai.Classification.create(
    search_model="davinci",
    model="davinci",
    examples = training,
    query = query,
    labels = ["High", "Medium", "Secret", "None"],
).label.lower()

print("The classification is: " + predict)