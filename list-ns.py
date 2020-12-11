import os
from kubernetes import client, config

config.load_kube_config(os.path.join(os.environ["HOME"], '.kube/config'))

api = client.CoreV1Api()
for ns in api.list_namespace().items:
    print(ns.metadata.name)
