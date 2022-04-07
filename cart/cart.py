import pybullet as p 
from time import sleep
import pybullet_data
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)
planeId = p.loadURDF("plane.urdf")
car = p.loadURDF("simplecart.urdf",[0, 0, 1])
p.setGravity(0, 0, -10)
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
number_of_joints = p.getNumJoints(car)
# for joint_number in range(number_of_joints):
#     info = p.getJointInfo(car, joint_number)
#     print(info)
for i in range(10000000):
    p.stepSimulation()
    sleep(1 / 240)
p.disconnect()