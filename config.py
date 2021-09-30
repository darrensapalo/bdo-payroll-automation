
import yaml

def GetConfig() -> any:
  with open("config.yaml", "r") as stream:
    try:
      output = yaml.safe_load(stream)
      return output
    except yaml.YAMLError as exc:
      print(exc)
  return None