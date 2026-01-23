from analyzer.parser import parse_log

def test_parse_log_counts_ips_correctly(tmp_path):
    
    """testar se o parser conta corretamente as tentativas por IP."""

    log_content = """
Failed password for invalid user test from 192.168.1.10 port 22
Failed password for invalid user admin from 192.168.1.10 port 22
Failed password for invalid user root from 10.0.0.5 port 22
"""

    log_file = tmp_path / "auth.log"
    log_file.write_text(log_content)

    result = parse_log(log_file)

    assert result["192.168.1.10"] == 2
    assert result["10.0.0.5"] == 1
