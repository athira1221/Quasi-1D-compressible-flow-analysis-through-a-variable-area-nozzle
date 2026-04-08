# 🚀 Quasi-1D Analysis of a Regeneratively Cooled Liquid Rocket Engine

## 📌 Overview

This project presents the **design and simulation of a student-scale liquid rocket engine thrust chamber**, integrating CAD-based geometry with a **quasi-one-dimensional (quasi-1D) compressible flow model** implemented in Python.

The objective is to bridge **mechanical design (CAD)** with **computational analysis**, enabling prediction of internal flow behavior and engine performance without relying on full CFD tools.

---

## 🎯 Objectives

* Model compressible flow through a **converging-diverging rocket nozzle**
* Compute flow properties such as **Mach number, pressure, and temperature**
* Estimate **mass flow rate and thrust**
* Integrate **CAD-derived geometry** into a physics-based simulation workflow
* Demonstrate a simplified approach to **rocket propulsion analysis**

---

## 🧩 Project Components

### 🔧 1. CAD Design

* Designed using CAD tools (SolidWorks / Fusion 360 / Inventor)
* Includes:

  * Combustion chamber
  * Converging-diverging nozzle
  * Cooling jacket and annular cooling gap

#### Key Dimensions (from design):

* Combustion chamber inner diameter: **80 mm**
* Combustion chamber length: **180 mm**
* Cooling jacket outer diameter: **100 mm**
* Cooling gap thickness: **5 mm**

---

### 🧮 2. Numerical Simulation (Python)

A quasi-1D compressible flow solver was developed using:

* Area–Mach number relation
* Isentropic flow equations
* Numerical root finding (`scipy.optimize.fsolve`)

---

## ⚙️ Methodology

1. Define geometry (from CAD or analytical approximation)
2. Compute cross-sectional area distribution:
   A(x) = π r(x)²
3. Identify throat (minimum area)
4. Solve Area–Mach relation numerically
5. Compute thermodynamic properties:

   * Temperature
   * Pressure
   * Density
6. Calculate velocity and mass flow rate
7. Estimate thrust using momentum equation

---

## 📊 Results

The simulation generates:

* 📈 Mach number distribution (subsonic → sonic → supersonic)
* 📉 Pressure variation along nozzle
* 🌡️ Temperature distribution
* 🚀 Exit velocity and thrust estimation

---

## 📁 Repository Structure

```
rocket-nozzle-analysis/
│
├── code/
│   └── rocket_nozzle_analysis.py
│
├── Assembly1.iam
├──Combustion chamber part1.SLDPRT
├── Jacket.SLDPRT
├── cooling channel system part 2 
├── results/
│   ├── mach_number_distrubution.png
│   ├── pressure_distribution.png
│   ├── temperature_distribution.png
│   ├── nozzel_geometery.png
|
├── images/
│   ├── cooling_channel_system.png
|   ├── jacket.png
|   ├── combustion_chamber.png
│   └── rokect_nozzel_isometric.png
│
└── README.md
```

---

## ▶️ How to Run

### 1. Install required libraries

```
pip install numpy scipy matplotlib pandas
```

### 2. Run the simulation

```
python rocket_nozzle_analysis.py
```

---

## 🧠 Key Concepts Used

* Quasi-1D compressible flow
* Isentropic flow relations
* Area–Mach number relationship
* Choked flow condition
* Rocket thrust equation

---

## 🚀 Key Features

* Combines **CAD design + physics-based simulation**
* Fully implemented in **Python (no CFD software required)**
* Beginner-friendly yet technically meaningful
* Extendable to advanced propulsion analysis

---

## 🚧 Future Work

* Incorporate real combustion gas properties (γ variation)
* Add **regenerative cooling heat transfer model**
* Perform validation with CFD tools (ANSYS / OpenFOAM)
* Implement GUI for interactive simulation
---

## 👤 Author

**ATHIRA S**

---

## 📢 Acknowledgment

This project was developed as part of a self-driven effort to explore **rocket propulsion, numerical methods, and simulation-based engineering design**.

