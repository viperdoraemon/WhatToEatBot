import sys

from whattoeatbot import localchat


def main():
    # Run local chat if --local flag is provided
    if "--local" in sys.argv:
        localchat.chat()


if __name__ == "__main__":
    main()
