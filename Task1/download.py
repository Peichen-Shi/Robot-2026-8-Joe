from roboflow import Roboflow

rf = Roboflow(api_key="zJA3teiiD31YWA6naKT1")
project = rf.workspace("talov-9bcpd").project("computer-mouse-e1v2f")
version = project.version(1)
dataset = version.download("yolov8")
