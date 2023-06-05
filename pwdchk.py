import os
import sys

from colorama import init, Fore, Back, Style
from zxcvbn import zxcvbn


def passwordStat(password):
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


def print_box(text: str):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'
    print(border)
    for line in lines:
        print('| ' + line.ljust(max_length) + ' |')
    print(border)


def passwordCheck(passwords, clean):
    passwords_len = len(passwords)

    for count, password in enumerate(passwords, 1):
        stat = passwordStat(password=password)
        if clean:
            print_box(
                f"#{count}: {password}\n\n" +
                f"{'#'*29} Score {'#'*29}\n{stat['details']['score']}\n\n\n" +
                f"{'#'*28} Guesses {'#'*28}\n{stat['details']['guesses']}\n\n\n" +
                f"{'#'*27} Crack Time {'#'*26}\n{stat['crack_time']}\n\n\n" +
                f"{'#'*27} Warnings {'#'*28}\n{stat['warning']}\n\n\n" +
                f"{'#'*26} Suggestions {'#'*26}\n{stat['suggestions']}\n\n\n" +
                f"{'#'*25} Sequence Info {'#'*25}\n{stat['sequence_info']}\n\n\n" +
                f"{'#'*66}\n{stat['calc_time']}\n\n\n"
            )
        else:
            _start = f"{Style.RESET_ALL}{Back.MAGENTA}{Fore.MAGENTA}"
            _title_end = f"{Back.MAGENTA}{Fore.MAGENTA}"
            print(f"{Style.RESET_ALL}{Back.YELLOW}{Fore.YELLOW}{'#'*66}{Style.RESET_ALL}")
            print(
                f"### {password} ###\n\n" +
                f"{_start}{'#'*29}{Fore.RESET} Score {_title_end}{'#'*29}{Style.RESET_ALL}\n{stat['details']['score']}\n\n\n" +
                f"{_start}{'#'*28}{Fore.RESET} Guesses {_title_end}{'#'*28}{Style.RESET_ALL}\n{stat['details']['guesses']}\n\n\n" +
                f"{_start}{'#'*27}{Fore.RESET} Crack Time {_title_end}{'#'*26}{Style.RESET_ALL}\n{stat['crack_time']}\n\n\n" +
                f"{_start}{'#'*27}{Fore.RESET} Warnings {_title_end}{'#'*28}{Style.RESET_ALL}\n{stat['warning']}\n\n\n" +
                f"{_start}{'#'*26}{Fore.RESET} Suggestions {_title_end}{'#'*26}{Style.RESET_ALL}\n{stat['suggestions']}\n\n" +
                f"{_start}{'#'*25}{Fore.RESET} Sequence Info {_title_end}{'#'*25}{Style.RESET_ALL}\n{stat['sequence_info']}\n" +
                f"{_start}{'#'*66}{Style.RESET_ALL}\nIt took {stat['calc_time']} seconds\n"
            )


def main():
    args = sys.argv[1:]

    clean = False
    if ("--clean" in args) or ("-c" in args):
        try:
            args.remove("--clean")
        except:
            args.remove("-c")
        clean = True

    passwordCheck(passwords=args, clean=clean)


if __name__ == "__main__":
    init()
    main()
