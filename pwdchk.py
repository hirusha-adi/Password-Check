import os
import sys

from zxcvbn import zxcvbn


def passwordCheck(password):
    try:
        results = zxcvbn(f"{password}")
    except Exception as e:
        print("Error:", e)

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
            warning = "-"
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

    return {
        'details': results,
        'sequence_info': sequence_info,
        'calc_time': calc_time,
        'crack_time': crack_time,
        'warning': warning,
        'suggestions': suggestions
    }


def main():
    password = input("Password> ")
    passwordCheck(password=password)


if __name__ == "__main__":
    main()