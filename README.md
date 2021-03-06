# Format Nutanix Cluster Details

If you are using Nutanix Sizer, you might have wanted to reformat the following block of text into something more text-friendly:

![Screenshot of Nutanix Sizer](/images/sizer_screenshot.png)

If you copy this text into your clipboard, you will end up with something like this:
```
NX-1065-G7
Model TypeHybrid
CPU Type2 x Intel Xeon Silver 4214R 12C 100W 2.4GHz Processor (24 Cores)
RAM16 x 32GB Memory Module (3200MHz DDR4 RDIMM)
SSD1 x 3.84TB 3.5"-A5-A SSD
HDD2 x 4TB 3.5"-A5-A HDD
NIC1 x 4-port 10GbE SFP+ Network Adapter
GPUNone
```

This script will take the previous example of a cluster specs, and reformat it into a nicer text that is copied to your clipboard so you can use it in your technical proposal or other documentation easily.

## Usage Steps

### 1. Have this in your clipboard:

```
NX-1065-G7
Model TypeHybrid
CPU Type2 x Intel Xeon Silver 4214R 12C 100W 2.4GHz Processor (24 Cores)
RAM16 x 32GB Memory Module (3200MHz DDR4 RDIMM)
SSD1 x 3.84TB 3.5"-A5-A SSD
HDD2 x 4TB 3.5"-A5-A HDD
NIC1 x 4-port 10GbE SFP+ Network Adapter
GPUNone
```

### 2. Run the script...

```bash
git clone https://github.com/obay/nutanix-sizer-cluster-specs.git
cd nutanix-sizer-cluster-specs
./run.sh
```
You will need Python to be installed to run the script.

### 3. You will have this in your clipboard instead

```
Cluster:		
Model Type:	NX-1065-G7 (Hybrid)
Nodes:		
CPU Type:	2 x Intel Xeon Silver 4214R 12C 100W 2.4GHz Processor (24 Cores)
RAM:		16 x 32GB Memory Module (3200MHz DDR4 RDIMM)
SSD:		1 x 3.84TB 3.5"-A5-A SSD
HDD:		2 x 4TB 3.5"-A5-A HDD
NIC:		1 x 4-port 10GbE SFP+ Network Adapter
GPU:		None
```

Fill the Cluster line with the cluster name and the Nodes line with the number of nodes in the cluster.
