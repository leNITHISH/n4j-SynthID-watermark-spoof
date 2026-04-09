from src.oracle import run_oracle
from src.attacker import build_freq_map
from src.zscore import compute_stats
from src.neo4j_loader import push_to_neo4j

def main():
    print("[+] Running oracle...")
    data = run_oracle()

    print("[+] Building frequency map...")
    freq = build_freq_map(data)

    print("[+] Computing Z-scores...")
    stats = compute_stats(freq, K=50, N=len(data))

    print("[+] Pushing to Neo4j...")
    push_to_neo4j(stats)

    print("[+] Done.")

if __name__ == "__main__":
    main()
