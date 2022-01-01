# Password-Check v2.0

- Website to check the strength of all your passwords easily and instantly!

- This is a password strength/stats checker that is made using [Low Budget Password Strength Estimation](https://github.com/dropbox/zxcvbn) ( Learn more from [here](https://www.semanticscholar.org/paper/zxcvbn%3A-Low-Budget-Password-Strength-Estimation-Wheeler/f7403f27b0517be683836f9c1cb8b0f5a5d82b1a) or [here](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/wheeler#:~:text=zxcvbn%20is%20an%20alternative%20password,suitable%20for%20mitigating%20online%20attacks.) ). This program will also check your password in a database of some leaked passwords.

# Priavcy Policy

- No user data is collected

- Password Strength Lookups are not being logged

- Nothing is being logged, this will be the same in the future

# Setup

## Ubuntu
1. ```sudo apt update && sudo apt upgrade```
2. ```sudo apt install python3 python3-pip```
3. ```pip3 install -r requirements.txt```
4. ```python3 setup.py```
5. ```python3 start.py```

## Arch
1. ```sudo pacman -Syu```
2. ```sudo pacman -S python python-pip```
3. ```python3 -m pip3 install -r requirements.txt```
4. ```python3 setup.py```
5. ```python3 start.py```

# References

1. Color theme from: [ColorHunt](https://colorhunt.co/palettes/dark)
2. [Sad Mac 404 Error Page](https://codepen.io/jkantner/pen/aPLWJm)
