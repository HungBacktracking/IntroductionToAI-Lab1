# !/bin/bash
pip install -r requirements.txt

python ./source/main.py 1 1 bfs
python ./source/main.py 1 1 astar_heuristic_1
python ./source/main.py 1 1 astar_heuristic_2
python ./source/main.py 1 1 dfs
python ./source/main.py 1 1 gbfs_heuristic_1
python ./source/main.py 1 1 gbfs_heuristic_2
python ./source/main.py 1 1 ucs

python ./source/main.py 1 2 bfs
python ./source/main.py 1 2 astar_heuristic_1
python ./source/main.py 1 2 astar_heuristic_2
python ./source/main.py 1 2 dfs
python ./source/main.py 1 2 gbfs_heuristic_1
python ./source/main.py 1 2 gbfs_heuristic_2
python ./source/main.py 1 2 ucs

python ./source/main.py 1 3 bfs
python ./source/main.py 1 3 astar_heuristic_1
python ./source/main.py 1 3 astar_heuristic_2
python ./source/main.py 1 3 dfs
python ./source/main.py 1 3 gbfs_heuristic_1
python ./source/main.py 1 3 gbfs_heuristic_2
python ./source/main.py 1 3 ucs

python ./source/main.py 1 4 bfs
python ./source/main.py 1 4 astar_heuristic_1
python ./source/main.py 1 4 astar_heuristic_2
python ./source/main.py 1 4 dfs
python ./source/main.py 1 4 gbfs_heuristic_1
python ./source/main.py 1 4 gbfs_heuristic_2
python ./source/main.py 1 4 ucs

python ./source/main.py 1 5 bfs
python ./source/main.py 1 5 astar_heuristic_1
python ./source/main.py 1 5 astar_heuristic_2
python ./source/main.py 1 5 dfs
python ./source/main.py 1 5 gbfs_heuristic_1
python ./source/main.py 1 5 gbfs_heuristic_2
python ./source/main.py 1 5 ucs


python ./source/main.py 2 1 dijkstra
python ./source/main.py 2 1 astar_lv2_heuristic_1
python ./source/main.py 2 1 astar_lv2_heuristic_2
python ./source/main.py 2 1 dp

python ./source/main.py 2 2 dijkstra
python ./source/main.py 2 2 astar_lv2_heuristic_1
python ./source/main.py 2 2 astar_lv2_heuristic_2
python ./source/main.py 2 2 dp

python ./source/main.py 2 3 dijkstra
python ./source/main.py 2 3 astar_lv2_heuristic_1
python ./source/main.py 2 3 astar_lv2_heuristic_2
python ./source/main.py 2 3 dp

python ./source/main.py 3 1 genetic
python ./source/main.py 3 1 hill_climbing

python ./source/main.py 3 2 genetic
python ./source/main.py 3 2 hill_climbing

python ./source/main.py 3 3 genetic
python ./source/main.py 3 3 hill_climbing

python ./source/main.py advance 1 bfs_tele
python ./source/main.py advance 2 bfs_tele
python ./source/main.py advance 3 bfs_tele