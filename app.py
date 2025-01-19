from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# List of words to check in the username
gay_users = ["soumo", "Aditya", "dhiru", "starexx", "garena", "GUN"]

# List of users who are always marked as "not gay"
not_gay_users = ["AKIRU", "I SHOW AKIRU", "AKHIL", "AKHIL DAS"]

@app.route("/", methods=["GET"])
def check_user():
    # Get query parameters
    username = request.args.get("username")
    age = request.args.get("age")
    sex = request.args.get("sex")

    # Check if the username is in the not_gay_users list
    if username in not_gay_users:
        gay_status = "no"
    # Check if the username contains any of the words in the gay_users list
    elif any(gay_user.lower() in username.lower() for gay_user in gay_users):
        gay_status = "yes"
    else:
        # For other users, randomly decide if they are "yes" or "no"
        gay_status = random.choice(["yes", "no"])

    # Return the response as JSON
    return jsonify({
        "Username": username,
        "Age": age,
        "Sex": sex,
        "Gay": gay_status
    })

if __name__ == "__main__":
    app.run(debug=True)
