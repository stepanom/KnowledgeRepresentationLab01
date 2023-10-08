import search as sr
import notebook as np

romania_map = sr.UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

romania_locations = romania_map.locations

node_colors = {node: 'white' for node in romania_map.locations.keys()}
node_positions = romania_map.locations
node_label_pos = {k: [v[0], v[1] - 10] for k, v in romania_map.locations.items()}
edge_weights = {(k, k2): v2 for k, v in romania_map.graph_dict.items() for k2, v2 in v.items()}

romania_graph_data = {'graph_dict': romania_map.graph_dict,
                      'node_colors': node_colors,
                      'node_positions': node_positions,
                      'node_label_positions': node_label_pos,
                      'edge_weights': edge_weights
                      }
np.show_map(romania_graph_data)

call_node_colors = []
romania_problem = sr.GraphProblem('Arad', 'Bucharest', romania_map)
a = sr.breadth_first_tree_search(romania_problem)
np.display_visual(romania_graph_data, user_input=False,
                  algorithm=sr.breadth_first_tree_search,
                  problem=romania_problem)
