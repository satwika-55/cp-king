def computeLPSArray(pattern):
    """
    Preprocess the pattern to create the LPS (Longest Prefix Suffix) array.
    """
    m = len(pattern)
    lps = [0] * m  # LPS array initialization
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Consider the previous longest prefix suffix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def KMP_search(text, pattern):
    """
    KMP algorithm for pattern searching.
    Returns the starting index of each occurrence of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    lps = computeLPSArray(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    results = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # Pattern found
            results.append(i - j)
            j = lps[j - 1]

        # Mismatch after j matches
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return results

