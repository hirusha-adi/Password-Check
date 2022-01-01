import datetime
import os

from flask import Flask, render_template, request, url_for
from zxcvbn import zxcvbn

# Multi Platform Support
SLASH = "\\"
if os.name == 'posix':
    SLASH = "/"


app = Flask(__name__)


# loading all the passwords
passwords_dir = f"{os.getcwd()}{SLASH}pwdcheck{SLASH}passwordlists{SLASH}"
password_lists = os.listdir(passwords_dir)
all_passwords = []
for fileName in password_lists:
    try:
        with open(f"{passwords_dir}{fileName}", "r", encoding="utf-8") as f1:
            allLines = f1.readlines()
            for oneLine in allLines:
                cleaned = oneLine.strip()
                if cleaned not in all_passwords:
                    all_passwords.append(cleaned)
            allLines = []
    except:
        pass

# Incase if any password-list does not exist
    try:
        all_passwords_count = len(all_passwords)
    except:
        all_passwords_count = 0

try:
    if all_passwords_count == 0:
        PWD_LIST_CHECK = False
    else:
        PWD_LIST_CHECK = True
except:
    PWD_LIST_CHECK = False
    all_passwords_count = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        passwordi = request.form.get('password')

        try:
            results = zxcvbn(f"{passwordi}")
        except Exception as pwderr:
            return render_template("error.html",
                                   pwderr=pwderr)

        sequence_info = ""
        for dic in results["sequence"]:
            for k, v in dic.items():
                if str(k) == "base_matches":
                    if isinstance(v[0], dict):
                        sequence_info += "\n- base_matches -\n"
                        for k2, v2 in v[0].items():
                            sequence_info += f"{k2} - {v2}\n"
                        sequence_info += "\n"
                else:
                    sequence_info += f"{k} - {v}\n"
            sequence_info += "\n"

        try:
            calc_time = results['calc_time']
        except:
            calc_time = "-"

        try:
            crack_time = f"Online throttling 100 per hour - {results['crack_times_display']['online_throttling_100_per_hour']}\nOnline throttling 10 per second - {results['crack_times_display']['online_no_throttling_10_per_second']}\nOffline slow hasing 1e4 per second - {results['crack_times_display']['offline_slow_hashing_1e4_per_second']}\nOffline fast hasing 1e10 per second - {results['crack_times_display']['offline_fast_hashing_1e10_per_second']}"
        except:
            crack_time = "-"

        warning = "-"
        try:
            if results['feedback']['warning'] == '':
                pass
            else:
                warning = results['feedback']['warning']
        except:
            warning = "-"

        suggestions = "-"
        try:
            if len(results["feedback"]["suggestions"]) == 0:
                pass
            else:
                suggestions = ""
                for item in results["feedback"]["suggestions"]:
                    suggestions += f"{item}\n"
        except:
            suggestions = "-"

        leaked = "-"
        try:
            if PWD_LIST_CHECK:
                if str(passwordi) in all_passwords:
                    leaked = f"Your password has been found in a database of {all_passwords_count} leaked passwords"
                else:
                    leaked = "-"
        except:
            leaked = "-"

        return render_template(
            'index.html',
            password=results['password'],
            score=results['score'],
            guesses=results['guesses'],
            sequence_info=sequence_info,
            calc_time=calc_time,
            crack_time=crack_time,
            warning=warning,
            suggestions=suggestions,
            leaked=leaked
        )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run('0.0.0.0', port=6969, debug=True)
