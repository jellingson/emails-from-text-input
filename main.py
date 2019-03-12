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

    return jsonify(result=emails)


def get_emails(text):
    regex = re.compile('[^\s]+@[^\s]+\.[^,;:\s]+')

    emails = regex.findall(text)
    email_list = []

    for email in emails:
        email_list.append(email)

    return email_list


if __name__ == "__main__":
    app.run(debug=True)
