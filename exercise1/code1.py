import matplotlib.pyplot as plt
import pandas as pd

def parse_data(file_path):
    lx = []
    pxx = []
    headers_found = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if "Lx" in line and "Pxx" in line:
                headers_found = True
                parts = line.split()
                lx_idx = parts.index("Lx")
                pxx_idx = parts.index("Pxx")
                continue
            if not headers_found:
                continue
            if "Loop time" in line:
                headers_found = False
                continue
            parts = line.split()
            lx.append(float(parts[lx_idx]))
            pxx.append(float(parts[pxx_idx]))
    return lx, pxx

import os
import glob

def batch_process(folder):
    # 1. get all log.* files
    files = glob.glob(os.path.join(folder, "log*.sec"))
    #print("Found files:", files)
    files.sort()
    results = {}

    for f in files:
        #print("Processing:", f)
        lx, pxx = parse_data(f)
        results[f] = (lx, pxx)

    return results

results = batch_process(".")
df = pd.DataFrame(data=results)
#df.to_csv("results.csv", index=False)
for filename, (lx, pxx) in results.items():
    key_filename = filename.split(".")[1].split("/")[-1]
    #print(f"Saving results for {filename} to file_{key_filename}_result.txt and plot_{key_filename}.png")
    with open(f"file_{key_filename}_result.txt", "w") as f:
        for x, y in zip(lx, pxx):
            f.write(f"{x} {y}\n")
    plt.figure(figsize=(10, 6))
    plt.plot(lx, pxx, marker='o', label=filename)
    plt.xlabel('Lx')
    plt.ylabel('Pxx')
    plt.title(f'Lx vs Pxx for {filename}')
    plt.legend()
    plt.grid() 
    plt.savefig(f"{key_filename}_plot.png")