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
            # Check for double curly brackets `{{`
            if i + 1 < n and text[i + 1] == "{":
                new_text.append("{{{{")
                i += 2
                continue

            # Check if the curly bracket starts a valid placeholder
            valid_found = False
            for valid in valids:
                placeholder = "{" + valid + "}"
                if text.startswith(placeholder, i):
                    new_text.append(placeholder)
                    i += len(placeholder)
                    valid_found = True
                    break

            # If not a valid placeholder, escape the single curly bracket
            if not valid_found:
                new_text.append("{{")
                i += 1

        elif text[i] == "}":
            # Check for double curly brackets `}}`
            if i + 1 < n and text[i + 1] == "}":
                new_text.append("}}}}")
                i += 2
                continue

            # Escape the single curly bracket
            new_text.append("}}")
            i += 1

        else:
            # Append regular characters
            new_text.append(text[i])
            i += 1

    return "".join(new_text)
