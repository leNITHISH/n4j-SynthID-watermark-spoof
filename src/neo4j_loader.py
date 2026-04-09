from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "test123")

driver = GraphDatabase.driver(URI, auth=AUTH)

def insert(tx, pos, token, count, z):
    tx.run("""
        MERGE (p:Position {index: $pos})
        MERGE (t:Token {word: $token})
        MERGE (p)-[r:APPEARS_IN]->(t)
        SET r.count = $count,
            r.z_score = $z
    """, pos=pos, token=token, count=count, z=z)

def push_to_neo4j(data):
    with driver.session() as session:
        for pos, tokens in data.items():
            for token, stats in tokens.items():
                session.execute_write(
                    insert,
                    pos,
                    token,
                    stats["count"],
                    stats["z"]
                )
