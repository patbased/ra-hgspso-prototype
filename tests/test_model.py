import pytest
from src.model import Service, Task, Workflow, ResourceNode, IoTDevice, ServiceRegistry, random_composition, greedy_composition

def test_service_init():
    s = Service(1, 10.0, 50.0, 0.95, 0.5)
    assert s.cost == 10.0
    assert repr(s) == "Service(id=1, cost=10.00, rt=50.00, avail=0.95, energy=0.50)"

def test_workflow_dag():
    tasks = [Task(1), Task(2), Task(3)]
    edges = [(1,2), (2,3)]
    wf = Workflow(tasks, edges)
    assert len(wf.get_tasks()) == 3
    assert list(wf.dag.edges) == [(1,2), (2,3)]

def test_registry_and_baselines():
    services = [Service(1, 10, 50, 0.95, 0.5), Service(2, 5, 60, 0.90, 0.6)]
    registry = ServiceRegistry(services)
    wf = Workflow([Task(1)], [])
    
    random_comp = random_composition(wf, registry)
    assert len(random_comp) == 1
    assert isinstance(random_comp[1], Service)
    
    greedy_comp = greedy_composition(wf, registry, key='cost')
    assert greedy_comp[1].id == 2  # Lowest cost
