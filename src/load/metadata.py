# run_id, timestamps
from datetime import datetime
import uuid

def generate_run_metadata():
    return {
        'run_id': str(uuid.uuid4()),
        'timestamp': datetime.utcnow().isoformat()
    }
