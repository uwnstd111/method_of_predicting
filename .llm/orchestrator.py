"""
Agent Orchestrator for method_of_predicting

This module provides a simple interface to spawn and manage Qwen3.5 agents
configured for the method_of_predicting project.

Usage:
    from orchestrator import AgentOrchestrator
    
    # Create orchestrator
    orchestrator = AgentOrchestrator(model="qwen-3.5-7b")
    
    # Run a forecasting workflow
    result = orchestrator.run_workflow("time_series_data", 
                                       {"source": "csv", "forecast_periods": 3})
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional
from zed.agent import spawn_agent


class AgentOrchestrator:
    """Simple orchestrator for Qwen3.5 agents."""
    
    # Skill name to model mapping
    DEFAULT_MODEL = "qwen-3.5-7b"
    
    # Agent categories
    CATEGORIES = {
        "forecasting": [
            "agent-linear-regression",
            "agent-brown-smoothing",
            "agent-holt-method",
            "agent-exponential-trend",
            "agent-power-function",
            "agent-logarithmic-trend",
            "agent-polynomial-trend",
            "agent-multi-regression"
        ],
        "utility": [
            "agent-data-import-validation",
            "agent-auto-model-selection",
            "agent-statistics-calculation",
            "agent-chart-visualization"
        ]
    }
    
    def __init__(self, model: Optional[str] = None):
        """Initialize with optional model override."""
        self.model = model or self.DEFAULT_MODEL
    
    def get_agent(self, skill_name: str, model: Optional[str] = None) -> spawn_agent:
        """
        Spawn an agent for a specific skill.
        
        Args:
            skill_name: Name of the skill (e.g., "agent-linear-regression")
            model: Optional model override (default: configured model)
        
        Returns:
            Spawned agent instance
        """
        agent_model = model or self.model
        label = skill_name.replace("agent-", "Agent: ")
        
        return spawn_agent(
            label=label,
            message=f"Execute skill: {skill_name}",
            model=agent_model
        )
    
    def run_workflow(
        self,
        data: Any,
        workflow: list,
        model: Optional[str] = None
    ) -> Dict:
        """
        Run a sequence of agents.
        
        Args:
            data: Initial data for the workflow
            workflow: List of skill names to execute
            model: Optional model override
        
        Returns:
            Final result from last agent
        """
        results = []
        current_data = data
        
        for step in workflow:
            skill_name = step if isinstance(step, str) else step["skill"]
            step_model = model if isinstance(step, dict) else model
            
            agent = self.get_agent(skill_name, step_model)
            
            # Pass data to agent
            agent_message = f"Input: {current_data}"
            if skill_name == "agent-data-import-validation":
                agent_message = f"Import source: {current_data.get('source', 'unknown')}"
            elif skill_name == "agent-auto-model-selection":
                agent_message = f"Analyze patterns in: {current_data}"
            
            agent = self.get_agent(skill_name, step_model)
            agent_message = f"Execute: {skill_name}\nInput: {json.dumps(current_data, indent=2)[:500]}"
            
            agent = self.get_agent(skill_name, step_model)
            agent.message = agent_message
            
            result = agent.wait()
            results.append(result)
            current_data = result
        
        return current_data
    
    def quick_forecast(
        self,
        time_series: list,
        model: Optional[str] = None
    ) -> Dict:
        """
        Quick forecasting workflow: Import → Select → Forecast → Stats
        
        Args:
            time_series: Raw time series data
            model: Optional model override
        
        Returns:
            Forecast result with statistics
        """
        workflow = [
            "agent-data-import-validation",
            "agent-auto-model-selection",
            "agent-holt-method",  # Default to Holt's
            "agent-statistics-calculation"
        ]
        
        return self.run_workflow(
            {"time_series": time_series},
            workflow,
            model
        )
    
    def smart_forecast(
        self,
        time_series: list,
        model: Optional[str] = None
    ) -> Dict:
        """
        Smart forecasting with auto-model selection and visualization.
        
        Args:
            time_series: Raw time series data
            model: Optional model override
        
        Returns:
            Complete forecast with charts
        """
        workflow = [
            "agent-data-import-validation",
            "agent-auto-model-selection",
            "agent-statistics-calculation",
            "agent-chart-visualization"
        ]
        
        return self.run_workflow(
            {"time_series": time_series},
            workflow,
            model
        )


# Predefined workflow templates
WORKFLOWS = {
    "simple": [
        "agent-auto-model-selection",
        "agent-holt-method",
        "agent-statistics-calculation"
    ],
    "comprehensive": [
        "agent-data-import-validation",
        "agent-auto-model-selection",
        "agent-holt-method",
        "agent-statistics-calculation",
        "agent-chart-visualization"
    ],
    "fast": [
        "agent-holt-method",
        "agent-statistics-calculation"
    ],
    "multi-factor": [
        "agent-multi-regression",
        "agent-statistics-calculation"
    ]
}


def quick_run(
    time_series: list,
    workflow: str = "simple",
    model: str = "qwen-3.5-7b"
) -> Dict:
    """
    Convenience function for quick forecasting.
    
    Args:
        time_series: Raw time series data
        workflow: Preset workflow name ("simple", "comprehensive", "fast", "multi-factor")
        model: Qwen3.5 model to use
    
    Returns:
        Forecast result
    """
    orchestrator = AgentOrchestrator(model=model)
    return orchestrator.run_workflow(
        {"time_series": time_series},
        WORKFLOWS[workflow]
    )


# Example usage
if __name__ == "__main__":
    # Sample time series
    sample_data = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    
    # Quick forecast with simple workflow
    print("Running simple forecast...")
    result = quick_run(sample_data, "simple", "qwen-3.5-7b")
    
    print(f"Forecast completed: {result}")
    
    # Comprehensive workflow
    print("\nRunning comprehensive workflow...")
    result = quick_run(sample_data, "comprehensive", "qwen-3.5-7b")
    
    print(f"Full analysis: {result}")
