Team number: xohw23-172

Project name: Quantum Sensing: PYNQ-based Portable Nuclear Magnetic Resonance Spectrometer Powered by Deep Learning from AMD Xilinx

Link to YouTube Video: https://youtu.be/D55JbZ45ar8

Link to project repository: https://github.com/unizhibin/Xilinx_Open_Hardware_2023

University name: University of Stuttgart

Participants: Jianyu Zhao
Email:jianyu.zhao@iis.uni-stuttgart.de

Participants: Hima Mullamangalam
Email:st180551@stud.uni-stuttgart.de

Participants: Peng Yichao
Email: st175893@stud.uni-stuttgart.de

Participants: Pratyush Shukla
Email: st181601@stud.uni-stuttgart.de


Supervisor name: Zhibin Zhao

Supervisor e-mail:zhibin.zhao@iis.uni-stuttgart.de

Board used: PYNQ-Z2, PYNQ-ZU

Software version: Vivado 2020.2 

Project Description:

Due to the unsurpassed specificity and complete non-invasiveness, Nuclear Magnetic Resonance (NMR) is an immensely powerful analytical tool in the field of analytical chemistry, food analysis, oil-well exploration, medical imaging, as well early-period disease detection. For example, NMR spectroscopy exploits the magnetic characteristics of atomic nuclei to provide specific information about the molecular structure and composition of a sample. While NMR relaxometry measures relaxation variables of a sample and provides valuable information about e.g. molecular mobility and water distribution within food products, and/or molecular dynamics, porosity, and moisture content in material science.
Nevertheless, in order to compensate for the comparatively low sensitivity of NMR experiments, standard high-end NMR instruments utilize huge superconducting magnets to create a strong and homogeneous magnetic field since the field's strength boosts the NMR signal and the field's homogeneity is necessary to resolve the spectrum peaks. As a result, they are bulky and expensive, which remains a significant hurdle in making the powerful technology accessible to a wider range of applications.
In this project, with the strategy of substituting large superconducting magnets with small maintenance-free permanent magnets with sufficient field homogeneity and discrete sensor frontend electronics with custom-designed NMR-on-a-chip transceiver, we implement a portable, battery-powered, and low-cost FPGA-based NMR system that is capable of mobile relaxometry and spectroscopy. In addition, edge AI is deployed in our system. We demonstrate the possibilities of spectrum identification, which extends the usage of the system to non-NMR-professionals, and intelligent field compensation due to temperature drift, which allows us to get rid of the power-hungry temperature control unit.

Directories:

1. Documentation: contains all introduction files, details of overlay, and experiment results.
2. GUI: contains the code for GUI which can be run on PYNQ board together with .bit file.
3. PCB: contains all  the electronic circuit designs.
4. Video: contains a short introduction video of the architecture and application of the pNMR system.

Instructions On How To Run the Software System:

1. Download the GUI files as they are ordered originally, run Launch.ipynb file and GUI will pop up.

About This Project:

1. Technical Complexity: It's a complete instrument system consisting of high-performance hardware design, embedded system design, and user interface software.
2. Implementation: Portable NMR system has the potential to broaden the application scenarios in various industry and research areas.
3. Marketability: Low-cost, convenient and low power consumption. No complex installation process is needed. Easy to maintain.
4. Re-usability: All PCBs, Python codes, Overlay design available. Easy to reproduce.
