# Lab 4 Context — Week 4: GUI & Problem-Solving Agent

**CLO-2:** Apply classical AI techniques, including uninformed and informed search algorithms, minimax, and neural networks, to solve structured problems.

---

## Submission Guidelines

1. Attach the link of the deployed Streamlit application.
2. Download the `.ipynb` file from Jupyter Notebook.
3. Submit the `.ipynb` and application link to GCR.
4. Failure to follow submission guidelines → **50% deduction** of total marks.

---

## Task 1: Streamlit-Based Exploratory Data Analysis Interface

**Goal:** Build an interactive EDA GUI with Streamlit. Deploy it.

### Requirements

1. **Dataset Ingestion & Metadata Inspection**
   - File upload module (CSV only), with format validation.
   - Dataset overview panel showing:
     - Row & column count
     - Column data types
     - Missing values per column
     - Statistical summary for numerical columns (mean, median, min, max)

2. **Attribute Selection & Classification**
   - Dropdown to select a single column.
   - Auto-detect if column is numerical or categorical → update visuals accordingly.

3. **Visualization Module**
   - **Numerical:** Histogram with axis labels + title.
   - **Categorical:** Bar chart with frequency counts + optional percentage display.
   - Visuals update dynamically on column selection.

4. **Interface Layout**
   - **Sidebar:** All interactive controls (file upload, column selector).
   - **Main area (top):** Dataset preview (first 5 rows) + metadata.
   - **Main area (bottom):** Conditional visualization canvas.

### Deliverables
- Fully deployed Streamlit EDA app.
- Screenshots with at least one numerical and one categorical plot.

### Dataset: Titanic (`Titanic-Dataset.csv`)
- **891 rows**, **12 columns** (plus header)
- Columns: `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, `Embarked`
- Numerical columns: `PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`
- Categorical columns: `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked`
- Has missing values (e.g., `Age`, `Cabin`, `Embarked`)

---

## Task 2: Smart Airport Check-in Planning Agent

**Goal:** Build a Problem-Solving Agent that plans a sequence of actions from arrival → boarding.

### Problem Formulation

| Element          | Definition                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Initial State    | Passenger arrives at the airport entrance                         |
| Goal State       | Passenger successfully boards the flight (state = `Boarded`)      |
| Actions          | Verify Identity, Check-in Baggage, Pass Security, Complete Immigration, Reach Boarding Gate |
| Transition Model | Executing an action updates the passenger's current state         |
| Goal Test        | Passenger state equals `Boarded`                                  |
| Path Cost        | Each checkpoint has an associated processing time                 |

### Implementation Requirements
- Represent checkpoints with an **adjacency-list graph**.
- Define: initial state, actions, transition model, goal test, path cost.
- Generate the reachable **state space**.
- Display: planned checkpoint sequence + total processing time.
- **Minimum 6 checkpoints.**
- Static environment; don't revisit completed checkpoints; store visited states to avoid cycles.

### Expected Output
- Initial State, Goal State, State-space graph, Planned checkpoint sequence, Total processing time.

---

## Task 3: University Course Registration Planning Agent

**Goal:** Build a Problem-Solving Agent for university course registration.

### Problem Formulation

| Element          | Definition                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Initial State    | Student Login                                                     |
| Goal State       | Student successfully enrolled (status = `Completed`)              |
| Actions          | Authenticate Student, Verify Prerequisites, Select Courses, Verify Fee Status, Confirm Enrollment |
| Transition Model | Each completed task updates the registration state                |
| Goal Test        | Registration status equals `Completed`                            |
| Path Cost        | Each step has a cost of **1 unit**                                |

### Implementation Requirements
- Represent the registration workflow as a **graph**.
- Generate all reachable states.
- Prevent revisiting completed steps.
- Display the execution sequence + total path cost.

---

## Task 4 (Ungraded): Cloud Resource Deployment Planning Agent

**Goal:** Plan deployment of an AI application onto cloud infrastructure.

### Problem Formulation

| Element          | Definition                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Initial State    | Deployment request received                                       |
| Goal State       | AI application deployed successfully (status = `Completed`)       |
| Actions          | Allocate Resources, Create Virtual Machine, Install Dependencies, Deploy AI Model, Verify Deployment |
| Transition Model | Each completed action updates the deployment state                |
| Goal Test        | Deployment status equals `Completed`                              |
| Path Cost        | Each operation has an associated execution time                   |

### Implementation Requirements
- Represent deployment states programmatically.
- Generate complete deployment state space.
- Display execution sequence + total deployment cost.

---

## Task 5 (Ungraded): Smart Warehouse Inventory Retrieval Agent

**Goal:** Generate a sequence of warehouse movements to retrieve an inventory item.

### Problem Formulation

| Element          | Definition                                                        |
| ---------------- | ----------------------------------------------------------------- |
| Initial State    | Warehouse Entrance                                                |
| Goal State       | Target Storage Rack                                               |
| Actions          | Move North, Move South, Move East, Move West                      |
| Transition Model | Movement changes robot's current warehouse location               |
| Goal Test        | Current location equals target rack                               |
| Path Cost        | Distance travelled between connected locations                    |

### Implementation Requirements
- Represent warehouse locations using a **graph**.
- Generate reachable warehouse states.
- Prevent revisiting explored locations.
- Display movement sequence + total travel cost.

---

## General Notes for All Planning Agents

All planning agents (Tasks 2–5) share a common pattern:
1. Define states, actions, transition model, goal test, path cost.
2. Represent the problem as a graph (adjacency list or similar).
3. Generate the reachable state space (BFS/DFS or similar search).
4. Track visited states to prevent cycles.
5. Output the action sequence and total path cost.

For Task 1, the focus is purely on Streamlit GUI + EDA with the Titanic dataset.
