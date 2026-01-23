def parse_log(log_file):
    """
    Lê o arquivo de log e retorna um dicionário
    com a contagem de tentativas por IP.
    """
    ip_counts = {}

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()

                if "from" in parts:
                    ip_index = parts.index("from") + 1
                    ip = parts[ip_index]

                    if ip in ip_counts:
                        ip_counts[ip] += 1
                    else:
                        ip_counts[ip] = 1

    return ip_counts

