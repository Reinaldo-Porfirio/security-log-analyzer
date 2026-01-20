import re

def parse_log(file_path):
    """
    Lê um arquivo de log e extrai os IPs de tentativas de login falhas.
    """
    ips = []

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
                if match:
                    ips.append(match.group())

    return ips
