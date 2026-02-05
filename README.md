# RA-HGSPSO Prototype  

**Renewable-Aware Hybrid Gravitational Search – Particle Swarm Optimization**  
for Sustainable Service Composition in Cloud-Based IoT Systems
## Project Overview

This repository contains a clean, modular, open-source Python prototype implementing **RA-HGSPSO** — a renewable-energy-aware extension of the Hybrid Gravitational Search-Particle Swarm Optimization (HGSPSO) algorithm for energy-sustainable service composition in cloud-IoT ecosystems.

The work is directly based on the research paper draft:

> "An energy-optimized service composition model for sustainable cloud-based IoT systems using a renewable-aware hybrid swarm intelligence algorithm"

**Current status (February 2026)**  
- Phase 1: Model classes, synthetic dataset, random/greedy baselines → **Complete**  
- Phase 2: Baseline HGSPSO optimizer → **Complete & validated**  
- Phase 3+: Renewable heterogeneity, green-aware extensions, lightweight simulator → **In progress**

The prototype uses **only open-source tools** and is designed to be lightweight, reproducible, and easy to extend.

### Key Features

- **Baseline HGSPSO** — faithful reproduction of Gong et al. (2025) hybrid GSA+PSO  
- Multi-objective fitness: cost, response time, availability, energy consumption  
- Particle-based representation for service-to-task mapping  
- Min-max QoS normalization across population  
- Synthetic 1000–5000 service dataset generation  
- NetworkX-based DAG workflows  
- Planned: Renewable energy profiles (solar/wind traces), green availability factor Gᵢ, sustainability term in fitness, dynamic energy manager, lightweight simulator

## Project Structure

```text
ra-hgspso-prototype/
├── src/
│   ├── __init__.py
│   ├── model.py          # Core entities: Service, Task, Workflow, ResourceNode, IoTDevice
│   ├── optimizer.py      # Baseline HGSPSO implementation
│   ├── energy.py         # (WIP) Renewable & battery models
│   ├── utils.py          # Data generation, normalization, config loading
│   └── config.yaml       # All tunable parameters
├── data/
│   └── synthetic_services.csv   # Generated QoS dataset
├── tests/
│   └── test_model.py     # Unit tests (pytest)
├── notebooks/
│   └── phase1_demo.ipynb       # Data exploration & baselines
│   └── phase2_demo.ipynb       # HGSPSO convergence & comparison
├── requirements.txt
└── README.md
```

## Setup Instructions

# 1. Clone the repository
git clone https://github.com/patbased/ra-hgspso-prototype.git
cd ra-hgspso-prototype

# 2. (Recommended) Create virtual environment
python -m venv venv
source venv/bin/activate    # Linux/macOS
# or
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt
   ```


## System Workflow
```
[User Input] --> [Streamlit UI]
                     |
                     v
[FastAPI Endpoint] --> [LlamaIndex: Data Processor]
                                  |
                                  v
[Mem0: Context Storage] <--> [LlamaIndex: Embedding Generator]
                                  |
                                  v
[Postgres VectorDB: Product Embeddings] --> [LlamaIndex: Query Engine]
                                  |
                                  v
[Recommendation Output] --> [Streamlit UI]
                                  |
                                  v
[User Feedback: Ratings/Selections] --> [Feedback Loop: Update Mem0 & Fine-Tune Embeddings]
                                  |
                                  v
[Back to LlamaIndex: Embedding Generator]
```

## Development Workflow
- **LlamaIndex Development**: Implement indexing and querying in `src/agents/`.
- **API Development**: Add endpoints in `src/api/main.py` using FastAPI.
- **Data Models**: Define Pydantic models in `src/models/`.
- **Testing**: Write tests in `tests/` using Pytest.
- **Database**: Use `scripts/setup_db.py` to initialize Postgres VectorDB.

## Future Enhancements
- Real-time analytics dashboard in Streamlit.
- Multimodal recommendations (e.g., image-based matching).
- A/B testing for recommendation algorithms.

## Contributing
- Follow Scrum methodology with daily stand-ups and weekly sprints.
- Use Git for version control and submit pull requests.
- Ensure code is tested with Pytest and adheres to security standards.

**License**: MIT  
**Repository**: https://github.com/victordeman/AI-Driven-Product-Recommendation-Platform.git
