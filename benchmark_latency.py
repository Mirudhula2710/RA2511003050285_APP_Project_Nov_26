import time
import socket
import json
import threading
from detection.physics_model import compute_expected_drainage
from detection.ml_model import predict_severity

def benchmark_physics(n=100):
    start = time.perf_counter()
    for _ in range(n):
        compute_expected_drainage(100.0, 5.0)
    end = time.perf_counter()
    avg_ms = ((end - start) / n) * 1000.0
    return avg_ms

def benchmark_ml(n=100):
    sample_features = {
        "hour": 14,
        "minute_of_day": 840,
        "tank_level": 85.0,
        "expected_level": 98.9,
        "rate_of_change": -0.22,
        "zone_Administration Building": 0,
        "zone_Canteen": 0,
        "zone_Hostel Blocks": 1,
        "zone_Laboratories": 0
    }
    # Warmup
    predict_severity(sample_features)
    start = time.perf_counter()
    for _ in range(n):
        predict_severity(sample_features)
    end = time.perf_counter()
    avg_ms = ((end - start) / n) * 1000.0
    return avg_ms

def benchmark_tcp_ingestion(n=100):
    host = '127.0.0.1'
    port = 65439
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(5)
    
    running = True
    def server_loop():
        while running:
            try:
                conn, _ = server_sock.accept()
                with conn:
                    data = conn.recv(1024)
                    if data:
                        _ = json.loads(data.decode('utf-8'))
            except:
                break

    server_thread = threading.Thread(target=server_loop, daemon=True)
    server_thread.start()
    time.sleep(0.1)

    payload_bytes = json.dumps({'zone': 'Hostel Blocks', 'level': 95.0}).encode('utf-8')
    times = []
    for _ in range(n):
        t0 = time.perf_counter()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(payload_bytes)
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000.0)
        time.sleep(0.002)

    running = False
    server_sock.close()
    return sum(times) / len(times)

if __name__ == '__main__':
    n = 100
    phys_avg = benchmark_physics(n)
    ml_avg = benchmark_ml(n)
    tcp_avg = benchmark_tcp_ingestion(n)
    
    print(f"BENCHMARK RESULTS (over {n} runs each):")
    print(f"(a) compute_expected_drainage average latency: {phys_avg:.4f} ms")
    print(f"(b) predict_severity average latency:          {ml_avg:.4f} ms")
    print(f"(c) full TCP packet ingestion average latency:  {tcp_avg:.4f} ms")
