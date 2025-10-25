def interleave_strings(s1, s2):
    """
    Interleaves two strings, taking characters alternately.
    Appends remaining characters of the longer string at the end.
    """
    result = []
    len1 = len(s1)
    len2 = len(s2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            result.append(s1[i])
        if i < len2:
            result.append(s2[i])

    return "".join(result)

# Example usage:
string1 = "abcd"
string2 = "pqrstu"
interleaved = interleave_strings(string1, string2)
print(f"Interleaving '{string1}' and '{string2}': {interleaved}")

string3 = "hello"
string4 = "world"
interleaved2 = interleave_strings(string3, string4)
print(f"Interleaving '{string3}' and '{string4}': {interleaved2}")

string5 = "short"
string6 = "verylongstring"
interleaved3 = interleave_strings(string5, string6)
print(f"Interleaving '{string5}' and '{string6}': {interleaved3}")
