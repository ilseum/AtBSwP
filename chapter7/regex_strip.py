import re


def regex_strip(text):
    both_strip = re.compile(r"^\s+|\s+$")
    return both_strip.sub("", text)


TEST_CASES = ["     lefty", "righty    ", "    bothy    ", "nothy", "mid ly", "  long  ly  "]


def main():
    for test in TEST_CASES:
        print(f"\"{test}\" becomes\n\"{regex_strip(test)}\"")


if __name__ == "__main__":
    main()
