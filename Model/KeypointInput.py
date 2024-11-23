from pydantic import BaseModel
from typing import List

class KeypointInput(BaseModel):
    # List of 30 frames, each containing flattened key points, each array contain 1662 elements
    # keypoint size: 30*1662
    keypoint: List[List[float]]