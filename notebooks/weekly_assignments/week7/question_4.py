"""One approach to analysing some encrypted data where a substitution is suspected is frequency analysis.
This program takes a message string, counts how many times each letter appears(ignoring case and non-letters),
sorts the results by frequency, and then displays the six letters with most counts with their counts.
"""


def frequency_analysis(message):
    message = message.lower()
    ltr_count = {}
    for ch in message:
        if ch.isalpha():
            ltr_count[ch] = ltr_count.get(ch, 0) + 1
    sorted_count = sorted(ltr_count.items(), key=lambda item: (-item[1], item[0]))
    return sorted_count[:6]


msg = "One approach to analysing some encrypted data where a substitution is suspected is frequency analysis."
result = frequency_analysis(msg)
print("Six Most Common Letters And Their Counts:")
for letter, count in result:
    print(f"{letter}: {count}")
