class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BELLMAN-FORD

        # prices[node] = cheapest cost to reach each airport; start all at infinity (unreached)
        prices = [float("inf")] * n
        # The source costs 0 to reach (we start there)
        prices[src] = 0

        # Run k + 1 rounds — k stops means up to k+1 flights, so k+1 rounds of relaxation
        for _ in range(k + 1):
            # Snapshot: copy the current prices — this round relaxes using last round’s values
            temp = prices.copy()

            # Relax every flight (u, v, price)
            for u, v, price in flights:
                # If airport u isn’t reachable yet (still infinity), skip — no path through it to relax
                if prices[u] == float("inf"):
                    continue
                # If reaching u (from the snapshot) plus this flight’s price beats v’s current best
                if prices[u] + price < temp[v]:
                    # update v’s price in temp (writing to temp, reading from the snapshot prices)
                    temp[v] = prices[u] + price

            # Commit this round’s updates — temp becomes the new prices for the next round
            prices = temp
        
        # After k+1 rounds, return dst’s price, or -1 if still unreachable
        return prices[dst] if prices[dst] != float("inf") else -1
 

        # TC: O(k . E) -> we run k+1 rounds. Each round relaxes all E flights once → O(E) per round, plus copying the prices array each round → O(V) per round. O((k+1) · (E + V)) = O(k · (E + V)), typically written O(k · E) since E usually dominates V in a connected graph. Overall O(k · E).
        # SC: O(n) -> the prices array and the temp snapshot are each size n → O(n). No adjacency list needed (we iterate the flights list directly). Overall O(n).

        # Variables: V = n (airports), E = number of flights, k = stop limit.


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
        

        # Why k + 1 rounds (the stop-to-flight conversion) -> "k stops" = k intermediate airports between src and dst. The number of FLIGHTS is one more than the number of stops:
                # 0 stops → 1 flight  (src → dst directly)
                # 1 stop  → 2 flights (src → A → dst)
                # k stops → k+1 flights

                # Bellman-Ford's property: after i rounds, shortest paths using ≤ i edges (flights) are found. We want paths with ≤ k+1 flights → run k+1 rounds.

                # run k+1 rounds → prices reflect the cheapest cost using at most k+1 flights = at most k stops. Exactly the constraint. This is the whole reason Bellman-Ford fits: the round count directly caps the number of flights, which Dijkstra can't do cleanly.

        
        # Why the snapshot (temp) is essential -> We READ from `prices` (last round's frozen values) and WRITE to `temp`. This ensures each round extends any path by EXACTLY ONE flight. 

                # Without the snapshot (relaxing in place, reading and writing the same array): a flight u→v could update v, then IN THE SAME ROUND a flight v→w uses the just-updated v to update w → a path src→...→u→v→w travels MULTIPLE flights in one round → counted as "one round" but uses several flights → EXCEEDS the k-stop limit.
                # Example: round 1 should only reach airports 1 flight from src. Without the snapshot, a chain could reach airports 2, 3+ flights away in round 1 → wrong (too many stops).

                # The snapshot freezes last round's distances, so within a round, updates to v don't cascade into w. Each round = exactly one more flight.
        

        # Why skip unreachable airports (prices[u] == inf) -> If airport u hasn't been reached yet (prices[u] is still infinity), there's no path to u, so we can't extend any path THROUGH u. Relaxing from an unreachable u would compute inf + price = inf (meaningless, and could cause overflow issues in some languages). Skipping it is both correct and cleaner. Only relax flights whose SOURCE u is actually reachable → paths grow from= reached airports outward.


        # Why prices[dst] == inf means unreachable (-1) -> After k+1 rounds, prices[dst] holds the cheapest cost to reach dst using at most k+1 flights. If it's STILL infinity, no such path exists (dst can't be reached from src within k stops) → return -1. 
                # prices[dst] finite → that's the cheapest price within k stops → return it.
                # prices[dst] == inf → no valid path within the stop limit → return -1.

                # The infinity sentinel doubles as the "unreachable" marker: never updated = never reached = impossible.
        

        # Visual Walkthrough:

                # n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
                # src=0, dst=3, k=1   (at most 1 stop → at most 2 flights → 2 rounds)

                # prices = [0, inf, inf, inf]  (prices[0]=0)

                # ── ROUND 1 ── (paths using ≤ 1 flight)
                #     temp = [0, inf, inf, inf]
                #     relax flights (reading from prices=[0,inf,inf,inf]):
                #         [0,1,100]: prices[0]=0 reachable, 0+100=100 < temp[1]=inf → temp[1]=100
                #         [1,2,100]: prices[1]=inf → skip
                #         [2,0,100]: prices[2]=inf → skip
                #         [1,3,600]: prices[1]=inf → skip
                #         [2,3,200]: prices[2]=inf → skip
                #     prices = temp = [0, 100, inf, inf]
                #     (after round 1: airport 1 reached via 1 flight, cost 100)

                # ── ROUND 2 ── (paths using ≤ 2 flights)
                #     temp = [0, 100, inf, inf]
                #     relax flights (reading from prices=[0,100,inf,inf]):
                #         [0,1,100]: 0+100=100 < temp[1]=100? no (not strictly less)
                #         [1,2,100]: prices[1]=100, 100+100=200 < temp[2]=inf → temp[2]=200
                #         [2,0,100]: prices[2]=inf → skip
                #         [1,3,600]: prices[1]=100, 100+600=700 < temp[3]=inf → temp[3]=700
                #         [2,3,200]: prices[2]=inf → skip (prices[2] still inf THIS round — snapshot!)
                #     prices = temp = [0, 100, 200, 700]
                #     (after round 2: airport 3 reached via 2 flights (0→1→3), cost 700)

                # ── Done (2 rounds) ──
                #     prices[dst=3] = 700 (finite) → return 700 

                # Note the SNAPSHOT at work in round 2: even though temp[2] became 200, the flight
                # [2,3,200] read from prices (where prices[2] was still inf) → it did NOT chain
                # 2→3 in the same round. So the path 0→1→2→3 (3 flights, 2 stops) was correctly
                # NOT counted — it exceeds k=1 stop. The answer 700 uses path 0→1→3 (1 stop). 

                # (Without the snapshot, [2,3] would have chained off the new temp[2]=200 →
                # temp[3]=400 via 0→1→2→3, a 2-STOP path, violating k=1. The snapshot prevents this.)


        # ----- Edge Cases -----

        # No path within k stops -> prices[dst] stays infinity → return -1.

        # Direct flight exists (k=0) -> 1 round (k+1=1); relaxes direct src→dst flights → finds the direct price (or -1 if no direct flight).

        # k large enough to reach freely -> Enough rounds to find the globally cheapest path → returns it (behaves like unconstrained shortest path).

        # dst unreachable at any stop count -> Never relaxed → infinity → -1

        # Cheaper path needs more than k stops -> That path requires more rounds than we run, so it’s not found — we correctly return the cheapest within-k-stops path (which may be pricier), or -1. This is the whole point of the constraint.

        # Self-src -> src != dst is guaranteed; prices[src]=0 seeds correctly.

        # Multiple flights between same airports -> No duplicates guaranteed, but parallel-ish flights would just relax to the cheapest.








