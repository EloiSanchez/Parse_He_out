import sys

def get_E(line):
    return line.split(":")[1].strip().split(" ")[0]

try:
    out_file = sys.argv[1]
except:
    print("You must call 'python parse_out output_file_path'")
    quit()

try:
    dt = sys.argv[2]
except:
    dt = 0.001  # Assume its in femtoseconds

try:
    with open(out_file, "r") as f:
        lines = f.readlines()
except:
    print(f"File {out_file = } does not exist")
    quit()

time, total_E, he_E, x_E, int_E, hekin_E, hecorr_E, heLJ_E, E_per_he = [], [], [], [], [], [], [], [], []
for line in lines:
    line = line.strip()
    if line.startswith("TOTAL ENERGY (He+X)"):
        total_E.append(get_E(line))
    elif line.startswith("TOTAL   energy (He)"):
        he_E.append(get_E(line))
    elif line.startswith("Kinetic energy (He)"):
        hekin_E.append(get_E(line))
    elif line.startswith("Lennard-Jones energy (He)"):
        heLJ_E.append(get_E(line))
    elif line.startswith("Correlation energy   (He)"):
        hecorr_E.append(get_E(line))
    elif line.startswith("Impurity energy (X-He)"):
        int_E.append(get_E(line))
    elif line.startswith("Rotational energy (X)"):
        x_E.append(get_E(line))
    elif line.startswith("Energy per particle (He)"):
        E_per_he.append(get_E(line)) 
    elif line.startswith("Iteration ="):
        time.append(line.split("=")[1].strip())

with open("parsed_out.dat", "w") as f:
    f.write(
        "#time\tTotal\tHe_tot\tImpurity\tInteraction\tHe_kin\tHe_LJ\tHe_corr\tE_per_he\n"
    )
    for i in range(len(time)):
        f.write(
           "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
           time[i],total_E[i],he_E[i],x_E[i],int_E[i],hekin_E[i],heLJ_E[i],hecorr_E[i],E_per_he[i]
           )
        )
