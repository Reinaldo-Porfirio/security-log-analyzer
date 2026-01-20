import os
from dotenv import load_dotenv
from analyzer.parser import parse_log
from analyzer.detector import detect_bruteforce
from analyzer.report import generate_csv_report

from rich.console import Console
from rich.table import Table

load_dotenv()

console = Console()

log_file = os.getenv("LOG_FILE")
threshold = int(os.getenv("BRUTEFORCE_THRESHOLD", 3))
ips = parse_log(log_file)
suspects = detect_bruteforce(ips, threshold)

console.print("\n[bold red]🚨 Security Analysis Report[/bold red]\n")

if suspects:
    table = Table(title="Suspicious IPs Detected")
    table.add_column("IP Address", style="cyan")
    table.add_column("Failed Attempts", style="magenta")

    for ip, attempts in suspects.items():
        table.add_row(ip, str(attempts))

    console.print(table)

    report_file = generate_csv_report(suspects)
    console.print(f"\n[green]✔ Report generated:[/green] {report_file}")
else:
    console.print("[green]✔ No suspicious activity detected.[/green]")
