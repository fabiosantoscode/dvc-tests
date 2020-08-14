from random import random
import json

metrics = json.dumps({
    "metric1": random(),
    "metric2": random(),
    "metric3": random(),
})

open('metrics.json', 'w').write(metrics)
