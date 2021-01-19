import clipboard


def main():
    text = clipboard.paste()
    if not text.startswith("NX"):
        return
    text_lines = text.splitlines()

    for text_line in text_lines:
        if text_line.startswith("NX"):
            model_line = text_line
        if text_line.startswith("Model Type"):
            model_type = text_line[len("Model Type"):len(text_line)]
        if text_line.startswith("CPU Type"):
            cpu_line = text_line[len("CPU Type"):len(text_line)]
        if text_line.startswith("RAM"):
            ram_line = text_line[len("RAM"):len(text_line)]
        if text_line.startswith("SSD"):
            ssd_line = text_line[len("SSD"):len(text_line)]
        if text_line.startswith("HDD"):
            hdd_line = text_line[len("HDD"):len(text_line)]
        if text_line.startswith("NIC"):
            nic_line = text_line[len("NIC"):len(text_line)]
        if text_line.startswith("GPU"):
            gpu_line = text_line[len("GPU"):len(text_line)]

    cluster_specs = ""
    cluster_specs = cluster_specs + "Cluster:\t\t" + "\n"
    cluster_specs = cluster_specs + "Model Type:\t" + model_line + " (" + model_type + ")" + "\n"
    cluster_specs = cluster_specs + "Nodes:\t\t" + "\n"
    cluster_specs = cluster_specs + "CPU Type:\t" + cpu_line + "\n"
    cluster_specs = cluster_specs + "RAM:\t\t" + ram_line + "\n"
    cluster_specs = cluster_specs + "SSD:\t\t" + ssd_line + "\n"
    cluster_specs = cluster_specs + "HDD:\t\t" + hdd_line + "\n"
    cluster_specs = cluster_specs + "NIC:\t\t" + nic_line + "\n"
    cluster_specs = cluster_specs + "GPU:\t\t" + gpu_line
    clipboard.copy(cluster_specs)
    print("Copied to clibpoard!")


if __name__ == "__main__":
    main()
