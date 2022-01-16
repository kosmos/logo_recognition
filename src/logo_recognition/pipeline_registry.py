"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from logo_recognition.pipelines import create_visual_embeddings

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "cve": create_visual_embeddings.create_pipeline(),
        "__default__": Pipeline([]),
    }
