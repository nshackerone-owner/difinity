import json
import requests
import subprocess

res= subprocess.run(["echo","123"],capture_output=True,)
result=res.stdout
print(result)
