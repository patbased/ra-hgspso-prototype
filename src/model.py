import networkx as nx
import pandas as pd
from typing import List, Dict

class Service:
    """Represents an atomic service with QoS attributes."""
    def __init__(self, id: int, cost: float, response_time: float, availability: float, base_energy_kwh: float, hosting_node: 'ResourceNode' = None):
        """
        Initialize a Service.
        
        :param id: Unique identifier.
        :param cost: Monetary cost.
        :param response_time: Execution time in ms.
        :param availability: Probability [0,1].
        :param base_energy_kwh: Base energy consumption.
        :param hosting_node: Optional ResourceNode hosting this service.
        """
        self.id = id
        self.cost = cost
        self.response_time = response_time
        self.availability = availability
        self.base_energy_kwh = base_energy_kwh
        self.hosting_node = hosting_node

    def __repr__(self):
        return f"Service(id={self.id}, cost={self.cost:.2f}, rt={self.response_time:.2f}, avail={self.availability:.2f}, energy={self.base_energy_kwh:.2f})"

class Task:
    """Represents a task in a workflow."""
    def __init__(self, id: int, required_services: List[int] = None):
        """
        Initialize a Task.
        
        :param id: Unique identifier.
        :param required_services: List of compatible service IDs (optional, for simplicity assume all compatible initially).
        """
        self.id = id
        self.required_services = required_services or []

    def __repr__(self):
        return f"Task(id={self.id})"

class Workflow:
    """Represents a composite workflow as a DAG of tasks."""
    def __init__(self, tasks: List[Task], edges: List[tuple]):
        """
        Initialize a Workflow.
        
        :param tasks: List of Task objects.
        :param edges: List of (source_task_id, target_task_id) for dependencies.
        """
        self.dag = nx.DiGraph()
        for task in tasks:
            self.dag.add_node(task.id, task=task)
        self.dag.add_edges_from(edges)

    def get_tasks(self) -> List[Task]:
        """Return list of tasks in topological order."""
        return [self.dag.nodes[n]['task'] for n in nx.topological_sort(self.dag)]

    def __repr__(self):
        return f"Workflow with {len(self.dag.nodes)} tasks"

class ResourceNode:
    """Represents an edge or cloud node."""
    def __init__(self, id: int, location: str, capacity: float):
        """
        Initialize a ResourceNode.
        
        :param id: Unique identifier.
        :param location: Geographical location (e.g., 'us-west').
        :param capacity: Computational capacity (abstract units).
        """
        self.id = id
        self.location = location
        self.capacity = capacity
        self.services = []  # List of hosted Services

    def add_service(self, service: Service):
        """Host a service on this node."""
        self.services.append(service)
        service.hosting_node = self

    def __repr__(self):
        return f"ResourceNode(id={self.id}, location={self.location}, capacity={self.capacity:.2f})"

class IoTDevice:
    """Represents an IoT device with energy constraints."""
    def __init__(self, id: int, battery_level: float = 1.0, local_renewable: bool = False):
        """
        Initialize an IoTDevice.
        
        :param id: Unique identifier.
        :param battery_level: Current battery [0,1].
        :param local_renewable: If device has local renewable source.
        """
        self.id = id
        self.battery_level = battery_level
        self.local_renewable = local_renewable

    def __repr__(self):
        return f"IoTDevice(id={self.id}, battery={self.battery_level:.2f}, renewable={self.local_renewable})"

class ServiceRegistry:
    """Manages a catalog of services."""
    def __init__(self, services: List[Service]):
        self.services = {s.id: s for s in services}

    def get_service(self, id: int) -> Service:
        return self.services.get(id)

    def find_candidates_for_task(self, task: Task) -> List[Service]:
        """For now, return all services (simplified; later filter by compatibility)."""
        return list(self.services.values())

# Baselines for sanity checking
def random_composition(workflow: Workflow, registry: ServiceRegistry) -> Dict[int, Service]:
    """Randomly assign a service to each task."""
    composition = {}
    for task in workflow.get_tasks():
        candidates = registry.find_candidates_for_task(task)
        if candidates:
            composition[task.id] = candidates[int(len(candidates) * hash(task.id) % len(candidates))]  # Deterministic random
    return composition

def greedy_composition(workflow: Workflow, registry: ServiceRegistry, key: str = 'cost') -> Dict[int, Service]:
    """Greedily assign the 'best' service per task (e.g., min cost)."""
    composition = {}
    for task in workflow.get_tasks():
        candidates = registry.find_candidates_for_task(task)
        if candidates:
            composition[task.id] = min(candidates, key=lambda s: getattr(s, key))
    return composition
