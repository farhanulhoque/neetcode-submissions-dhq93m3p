class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BELLMAN-FORD

        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for u, v, price in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price
            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1
 

        # TC:
        # SC: 


        # Solution Description: We want the cheapest path from src to dst using at most k stops — meaning at most k+1 flights. The stop limit breaks plain Dijkstra, so we use Bellman-Ford, whose round structure naturally bounds the number of edges. We keep a prices array (cheapest cost to each airport, starting at infinity except src = 0). We run k+1 rounds. Each round, we relax every flight using a snapshot of the previous round’s prices (so each round adds exactly one flight to any path). After k+1 rounds, prices[dst] is the cheapest price reachable within k stops; if it’s still infinity, dst is unreachable within the limit → return -1.


        # ----- Deep Dive -----

        # BELLMAN-FORD:

                # 1. A DISTANCE array: dist[node] = cheapest cost to reach node from src so far.
                # Initialized to infinity, except dist[src] = 0.

                # 2. ROUNDS: repeat (k+1) times — each round relaxes all edges once, extending
                # paths by one more flight.

                # 3. SNAPSHOT per round: relax using last round's distances (a copy), so each
                # round adds exactly one edge.

                # 4. RELAXATION: for each flight (u→v, price), if reaching u (per snapshot) + price
                # beats v's current best, update dist[v].

                # After k+1 rounds, dist[dst] is the cheapest price within k stops (or still
                # infinity → unreachable → return -1).


                # Plain Dijkstra breaks with a stop limit because its greedy “finalize the cheapest path to each node, never revisit” discards paths that are pricier but use fewer stops — and one of those might be the only option within the limit. Bellman-Ford doesn’t greedily finalize; it relaxes all edges repeatedly, which makes “within k steps” natural to enforce.

                # Bellman-Ford relaxes every edge repeatedly over rounds. Its key property: after i rounds, shortest paths using at most i edges are correct — each round lets paths grow one edge longer. This makes the stop constraint trivial: “at most k stops” = “at most k+1 flights” = run exactly k+1 rounds. The round count directly bounds the path length, which is exactly what Dijkstra can’t do cleanly.

                # The critical subtlety: each round must relax using a snapshot of the previous round’s distances, not values updated mid-round. Otherwise a chain of edges could all relax in one round, letting a path “travel” many edges at once — violating the “at most i edges after round i” guarantee and exceeding the stop limit. Reading from a frozen copy (temp) while writing to dist ensures each round extends any path by exactly one edge.
        

        # 



        # ----- Edge Cases -----

        # 








