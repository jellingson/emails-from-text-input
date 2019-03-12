from flask import Flask, render_template, request, jsonify

import re

app = Flask(__name__)


@app.route("/projects/get-email-application")
def get_emails_application():
    return render_template("email-application.html")


@app.route("/projects/email-results")
def show_results():
    text = request.args.get('text', "", type=str)
    emails = get_emails(text)
    print(text)

    return jsonify(result=emails)


def get_emails(text):
    regex = re.compile('[^\s]+@[^\s]+\.[^,;:\s]+')

    emails = regex.findall(text)
    emailList = []

    for email in emails:
        emailList.append(email)
        print(email)

    return emailList


if __name__ == "__main__":
    app.run(debug=True)
