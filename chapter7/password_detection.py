import re

TEST_CASES = ["abcdefghi", "aBcDeFgHIj", "12345", "abd123456", "aBcd1",
              "aBc123DeF", "ABCD1234abcd"]

pw_regex = re.compile(r"("
                      r"(?=.*[A-Z]+)"
                      r"(?=.*[a-z]+)"
                      r"(?=.*\d+)"
                      r"(?=.*\S{8,})"
                      r")")


for test in TEST_CASES:
    print(f"Password \"{test}\" is ", end="")
    print("correct.") if pw_regex.search(test) else print("incorrect.")
