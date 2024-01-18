#!/usr/bin/python3
############################################################################################################################
# ANLEITUNG
# Falls noch nicht vorhanden, installieren Sie Python auf Ihrem System.
# Es wird empfohlen mit einem sog. virtual environment zu arbeiten: https://docs.python.org/3/library/venv.html
# Wir verwenden im Folgenden das PM4Py python package (dieses muss installiert sein): https://pm4py.fit.fraunhofer.de/
############################################################################################################################

# Aufruf über command line: $ python3 blatt8_aufgabe3_loesungsvorschlag.py  --input_path="logs/" --filename="log1.xes"
# oder alternativ unter Linux 1) File ausführbar machen: $chmod +x blatt8_aufgabe3_loesungsvorschlag.py (dazu dient die erste Zeile), 2) $ ./blatt8_aufgabe3_loesungsvorschlag.py  --input_path="logs/" --filename="log1.xes"


# lädt die benötigten libraries; os und argparse nicht unbedingt notwendig, erlaubt aber die logs der Reihe nach bequem über command line arguments einzulesen
import os
import argparse

import pm4py

# Inputparameter um das XES File zu spezifizieren, das verwendet werden soll 
parser = argparse.ArgumentParser()
parser.add_argument('--input_path')
parser.add_argument('--filename')
args = parser.parse_args()
if not os.path.exists(args.input_path):
  print("input path does not exist")
if not os.path.exists(os.path.join(str(args.input_path), str(args.filename))):
  print("file does not exist")
if not os.path.exists("output/"):
  os.mkdir("output")

# Einlesen des XES Files
log = pm4py.read_xes(os.path.join(args.input_path, args.filename))

####
# Aufruf AlphaMiner
print("Call AlphaMiner")
petri_net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)

# Visualisierung Ergebnis AlphaMiner.
pm4py.save_vis_petri_net(petri_net, initial_marking, final_marking, os.path.join("output","pn_"+args.filename.replace('.xes','')+".pdf"))
####

####
# Aufruf HeuristicMiner mit default values und dependency threshold 0.1
print("Call HeuristicMiner with threshold 0.1")
heuristic_net = pm4py.discover_heuristics_net(log, dependency_threshold=0.1)

# Visualisierung Ergebnis HeuristicMiner.
pm4py.save_vis_heuristics_net(heuristic_net, os.path.join("output","hn_"+args.filename.replace('.xes','')+"_0_1.pdf"))
####

####
# Aufruf HeuristicMiner mit default values und dependency threshold 0.5
print("Call HeuristicMiner with threshold 0.5")
heuristic_net = pm4py.discover_heuristics_net(log, dependency_threshold=0.5)

# Visualisierung Ergebnis HeuristicMiner.
pm4py.save_vis_heuristics_net(heuristic_net, os.path.join("output","hn_"+args.filename.replace('.xes','')+"_0_5.pdf"))
####



