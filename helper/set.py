from typing import List

def escape_invalid_curly_brackets(text: str, valids: List[str]) -> str:
    """
    Escape invalid curly brackets in the given text while preserving valid placeholders.

    Args:
        text (str): The input text containing curly brackets.
        valids (List[str]): A list of valid placeholder names (e.g., ["name", "age"]).

    Returns:
        str: The text with invalid curly brackets escaped.
    """
    new_text = []
    i = 0
    n = len(text)

    while i < n:
        if text[i] == "{":
            # Handle double curly brackets
            if i + 1 < n and text[i + 1] == "{":
                new_text.append("{{{{")
                i += 2
                continue

            # Check for valid placeholders
            match = None
            for valid in valids:
                placeholder = f"{{{valid}}}"
                if text.startswith(placeholder, i):
                    match = placeholder
                    break

            if match:
                new_text.append(match)
                i += len(match)
            else:
                new_text.append("{{")
                i += 1

        elif text[i] == "}":
            # Handle double closing curly brackets
            if i + 1 < n and text[i + 1] == "}":
                new_text.append("}}}}")
                i += 2
            else:
                new_text.append("}}")
                i += 1

        else:
            new_text.append(text[i])
            i += 1

    return "".join(new_text)
