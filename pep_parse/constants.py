from pathlib import Path
from typing import List

BASE_DIR: Path = Path(__file__).parent.parent
DATETIME_FORMAT: str = '%Y-%m-%d_%H-%M-%S'
EXPECTED_STATUS: List[str] = ['Accepted', 'Active', 'Deferred', 'Draft',
                              'Final', 'Provisional', 'Rejected',
                              'Superseded', 'Withdrawn']
