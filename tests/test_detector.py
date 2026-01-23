from analyzer.detector import detect_bruteforce

def test_detect_bruteforce_flags_correct_ips():
    
    """Testa se IPs com tentativas acima do limite são detectados."""

    data = {
        "192.168.1.10": 5,
        "10.0.0.5": 2,
        "172.16.0.1": 1
    }

    threshold = 3

    suspects = detect_bruteforce(data, threshold)

    assert "192.168.1.10" in suspects
    assert "10.0.0.5" not in suspects
    assert "172.16.0.1" not in suspects