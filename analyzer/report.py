import csv
import os
from datetime import datetime

def generate_csv_report(suspects, output_dir="reports"):
    """
    Gera um relatório CSV com IPs suspeitos.
    """
    # Garante que o diretório existe
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{output_dir}/security_report_{timestamp}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Failed Attempts"])

        for ip, attempts in suspects.items():
            writer.writerow([ip, attempts])

    return filename

