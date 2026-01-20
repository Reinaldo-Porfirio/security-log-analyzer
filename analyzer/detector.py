from collections import Counter

def detect_bruteforce(ips, threshold=3):
    
    counter = Counter(ips)

    suspects = {
        ip: attempts
        for ip, attempts in counter.items()
        if attempts >= threshold
    }

    return suspects
