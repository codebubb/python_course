import pickle
import time
from hashlib import md5

users = [
          {"username": "james", "pin": "1234", "account_type": "bank_account", "balance": 1000, "transactions": []},
          {"username": "fred", "pin": "1234", "account_type": "student_account", "balance": 1000, "transactions": []},
          {"username": "dave", "pin": "1234", "account_type": "savings_account", "balance": 1000, "transactions": [], "interest_rate": 1.2, "last_savings_time": time.time()}
        ]

print "Creating bank account users..."
for user in users:
  for key,val in user.items():
      exec(key + '=val')
  with open("users/" + username + ".txt", 'w') as f:
    pickle.dump({"pin": md5(pin).hexdigest(), "account_type": account_type}, f)
  print ">>>User account:", username, "created successfully!"
  if account_type == "savings_account":
    account_data = {"balance": balance, "transactions": transactions, "interest_rate": user["interest_rate"], "last_savings_time": user["last_savings_time"]}
  else:
    account_data = {"balance": balance, "transactions": transactions}
  with open("accounts/" + username + ".txt.", 'w') as f:
      pickle.dump(account_data, f)
  print ">>>Bank account:", username, "created successfully!"
