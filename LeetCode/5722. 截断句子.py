def truncateSentence(s: str, k: int) -> str:
    s = s.split()
    return ' '.join(s[:k])


print(truncateSentence(s="Hello how are you Contestant", k=4))
