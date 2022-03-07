import os
from re import X

import sys
sys.path.append("/home/ros_tms/tms_db/tms_db_manager/scripts")
import rclpy
import json
import copy
from datetime import *

import pymongo
from rclpy.node import Node
from std_msgs.msg import String
from angel_msg_db.msg import Angeltest
from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import BatteryState
<<<<<<< HEAD
from sensor_msgs.msg import Temperature
from std_msgs.msg import Float64MultiArray
import socket
=======
>>>>>>> 4f8bc2d5becc86551e855e6e25a224176bfca53f
# import angel_db_manager.tms_db_util as db_util

# client = pymongo.MongoClient('localhost:27017')
# db = client.angeldb
MONGO_HOSTNAME = '192.168.0.243'
MONGO_PORT = '27017'
MONGO_DB = 'wasp'
class AngelDbcheck(Node):
    def __init__(self):
        super().__init__("angel_db_pub")
<<<<<<< HEAD

        # for Cloud
        # ID = input("ID :")
        # PW = input("Password :")
        # self.client = pymongo.MongoClient("mongodb+srv://"+ID+":"+PW+"@cluster0.rahyc.mongodb.net/angeldb?retryWrites=true&w=majority")
        # self.client = pymongo.MongoClient("mongodb+srv://angel1:angel1@cluster0.rahyc.mongodb.net/angeldb?retryWrites=true&w=majority")
        print("Host Name ",socket.gethostname())
        print("IP Address(Internal) : ",socket.gethostbyname(socket.gethostname()))
        print("IP Address(External) : ",socket.gethostbyname(socket.getfqdn()))

        self.client = pymongo.MongoClient('mongodb://'+MONGO_HOSTNAME+':'+MONGO_PORT)
        if not self.client:
            self.get_logger().error(" WASP Database server is not finded. please make sure your account and password")
        else :
            self.get_logger().info(" WASP Database server is successfully connected")
            print(self.client)

        
        self.substate = self.create_subscription(JointTrajectory, "/eth_bridge/joint_state_topic",  self.dbWriteCallback, 10)
        self.subcommand = self.create_subscription(JointTrajectory, "/eth_bridge/joint_target_topic",  self.dbCommandWriteCallback, 10)
        self.subcommand = self.create_subscription(BatteryState, "/eth_bridge/battery_state_topic", self.batterystateWrite, 10)
        self.publisher_batterystate = self.create_publisher(BatteryState, '/angel_db_data/battery', 10)
        self.sub_batterystate = self.create_subscription(BatteryState, '/angel_db_data/battery', self.mongodbbatteryWrite, 10)
        self.publisher_state = self.create_publisher(Angeltest, '/angel_db_data', 10)
        self.publisher_command = self.create_publisher(Angeltest, '/angel_db_data_command', 10)
        self.sub_state = self.create_subscription(Angeltest, "/angel_db_data",  self.mongodbstateWrite, 10)
        self.sub_command = self.create_subscription(Angeltest, "/angel_db_data_command",  self.mongodbcommandWrite, 10)
        self.sub_temp = self.create_subscription(Float64MultiArray, "/cpu_ram_info", self.temperaturewrite, 10)

    def mongodbbatteryWrite(self, mongomsg):
        db = self.client.wasp.robotpowers
        if mongomsg.percentage > 0 :
            id_mongo = {"id" : 1004}
            # post = {"$set" :{"percentage" : mongomsg.percentage, "current" : mongomsg.current, "voltage" : mongomsg.voltage }}
            post = {"id" : 1004, "percentage" : round(mongomsg.percentage,3), "current" : mongomsg.current, "voltage" : mongomsg.voltage }
            # post = {"percentage" : mongomsg.percentage, "current" : mongomsg.current, "voltage" : mongomsg.voltage }
            print(post)
            # db.insert(post)
            # print("11dddddddddddddddddddddddddddddddddddd")
            db.update(id_mongo, post)

    def temperaturewrite(self, msg):
        self.sensormsg = Float64MultiArray()
        self.sensormsg.data = msg.data
        db = self.client.wasp.sensors
        senser_db = {"robotModel":"M30","robotId":"robot-1","sensorType":"temp_cpuusage_ramusage","sensorId":"sensorId-1","header":{"seq":1,"stamp":{"sec":1645063385,"nanosec":123},"frame_id":""},"layout":{"dim":[{"label":"height","size":480,"stride":921600},{"label":"width","size":640,"stride":1920},{"label":"channel","size":3,"stride":3}],"data_offset":3},"data":[msg.data[0],msg.data[1],msg.data[2]]}
        db.insert(senser_db)
        print("insert sensor system data")

=======
        # ID = input("ID :")
        # PW = input("Password :")
        # self.client = pymongo.MongoClient("mongodb+srv://"+ID+":"+PW+"@cluster0.rahyc.mongodb.net/angeldb?retryWrites=true&w=majority")
        # self.client = pymongo.MongoClient("mongodb+srv://angel1:angel1@cluster0.rahyc.mongodb.net/angeldb?retryWrites=true&w=majority")
        self.client = pymongo.MongoClient('mongodb://192.168.0.243:27017')
        if not self.client:
            self.get_logger().error(" WASP Database server is not finded. please make sure your account and password")
        else :
            self.get_logger().info(" WASP Database server is successfully connected")
            print(self.client)

        
        self.substate = self.create_subscription(JointTrajectory, "/eth_bridge/joint_state_topic",  self.dbWriteCallback, 10)
        self.subcommand = self.create_subscription(JointTrajectory, "/eth_bridge/joint_target_topic",  self.dbCommandWriteCallback, 10)
        self.subcommand = self.create_subscription(BatteryState, "/eth_bridge/battery_state_topic", self.batterystateWrite, 10)
        self.publisher_batterystate = self.create_publisher(BatteryState, '/angel_db_data/battery', 10)
        self.sub_batterystate = self.create_subscription(BatteryState, '/angel_db_data/battery', self.mongodbbatteryWrite, 10)
        self.publisher_state = self.create_publisher(Angeltest, '/angel_db_data', 10)
        self.publisher_command = self.create_publisher(Angeltest, '/angel_db_data_command', 10)
        self.sub_state = self.create_subscription(Angeltest, "/angel_db_data",  self.mongodbstateWrite, 10)
        self.sub_command = self.create_subscription(Angeltest, "/angel_db_data_command",  self.mongodbcommandWrite, 10)

    def mongodbbatteryWrite(self, mongomsg):
        db = self.client.wasp.robotpowers
        if mongomsg.percentage > 0 :
            id_mongo = {"id" : 1004}
            # post = {"$set" :{"percentage" : mongomsg.percentage, "current" : mongomsg.current, "voltage" : mongomsg.voltage }}
            post = {"id" : 1004, "percentage" : round(mongomsg.percentage,3), "current" : mongomsg.current, "voltage" : mongomsg.voltage }
            # post = {"percentage" : mongomsg.percentage, "current" : mongomsg.current, "voltage" : mongomsg.voltage }
            print(post)
            # db.insert(post)
            # print("11dddddddddddddddddddddddddddddddddddd")
            db.update(id_mongo, post)

>>>>>>> 4f8bc2d5becc86551e855e6e25a224176bfca53f
    def batterystateWrite(self, msg):
        self.batterymsg = BatteryState()
        self.batterymsg.voltage = msg.voltage
        self.batterymsg.current = msg.current
        self.batterymsg.percentage = msg.percentage
        
        msg_dict = {}

        slot_types = [None] * len(self.batterymsg.__slots__) 
        for (attr, type) in zip(self.batterymsg.__slots__, slot_types):
            result = zip(self.batterymsg.__slots__, slot_types)
            resultSet = set(result)
            # print(attr)
            # print(result)
            # print(resultSet)
            msg_dict[attr[1:]] = rearrange_value(getattr(self.batterymsg, attr))
            
        self.publisher_batterystate.publish(self.batterymsg)
        


    def mongodbstateWrite(self, mongomsg):
        # print(mongomsg)
        # print("11dddddddddddddddddddddddddddddddddddd")

        db = self.client.wasp.robotsjoints
        # db_command = self.client.wasp.robotscommands
        # print(db)
        post_insert = {}
        post_insert = {"id" : mongomsg.id, 'name': mongomsg.name, 'left_hip': mongomsg.positions[0], 'left_knee' : mongomsg.positions[1], 'right_hip': mongomsg.positions[2], 'right_knee': mongomsg.positions[3]}
        if mongomsg.name == "M30_command":
            id_mongo = {"name" : "M30_command"}
            post = {"$set" : {'left_hip': round(mongomsg.positions[0],3), 'left_knee' : round(mongomsg.positions[1],3), 'right_hip': round(mongomsg.positions[2],3), 'right_knee': round(mongomsg.positions[3],3)}}
            # db.insert(id_mongo, post)
            print("11dddddddddddddddddddddddddddddddddddd")
            db.update(id_mongo, post)
        # print(db)
        else :
            id_mongo = {"name" : "M30"}
            post = {"$set" : {'left_hip': round(mongomsg.positions[0],3), 'left_knee' : round(mongomsg.positions[1],3), 'right_hip': round(mongomsg.positions[2],3), 'right_knee': round(mongomsg.positions[3],3)}}
            # db.insert(post_insert)
            # db.insert(id_mongo, post)
            db.update(id_mongo, post)
        # db.insert(post_insert)

        # db_command.insert()
        # db.command.insert(post_insert)
        

    def mongodbcommandWrite(self, mongomsg):

        db = self.client.wasp.robotsjoints
        # db_command = self.client.wasp.robotscommands
        # print(mongomsg)
        post_insert = {}
        post_insert = {"id" : mongomsg.id, 'name': mongomsg.name, 'left_hip': mongomsg.positions[0], 'left_knee' : mongomsg.positions[1], 'right_hip': mongomsg.positions[2], 'right_knee': mongomsg.positions[3]}
        if mongomsg.name == "M30_command":
            id_mongo = {"name" : "M30_command"}
            post = {"$set" : {'left_hip': round(mongomsg.positions[0],3), 'left_knee' : round(mongomsg.positions[1],3), 'right_hip': round(mongomsg.positions[2],3), 'right_knee': round(mongomsg.positions[3],3)}}
            # db.insert(post_insert)
            db.update(id_mongo, post)
        # print(db)
        else :
            id_mongo = {"name" : "M30"}
            post = {"$set" : {'left_hip': round(mongomsg.positions[0],3), 'left_knee' : round(mongomsg.positions[1],3), 'right_hip': round(mongomsg.positions[2],3), 'right_knee': round(mongomsg.positions[3],3)}}
            # db.insert(post_insert)
            db.update(id_mongo, post)

    def dbWriteCallback(self, msg):
        # print("@@@@@@@@")
        self.dbmsg = Angeltest()
        self.dbmsg.id = 1004
        self.dbmsg.name = "M30"
        # print(msg)
        self.dbmsg.positions = msg.points[0].positions
        msg_dict = {}

        slot_types = [None] * len(self.dbmsg.__slots__) 
        for (attr, type) in zip(self.dbmsg.__slots__, slot_types):
            result = zip(self.dbmsg.__slots__, slot_types)
            resultSet = set(result)
            # print(attr)
<<<<<<< HEAD
            # print(result)
            # print(resultSet)
            msg_dict[attr[1:]] = rearrange_value(getattr(self.dbmsg, attr))
            
        # print(msg_dict)
        self.publisher_state.publish(self.dbmsg)
        # self.get_logger().info("d")
        # x = db.robot.insert_one(post)
        # print(x.inserted_id)
    def dbCommandWriteCallback(self, commandmsg):
        self.dbmsg = Angeltest()
        self.dbmsg.id = 1004
        self.dbmsg.name = "M30_command"
        print(commandmsg)
        self.dbmsg.positions = commandmsg.points[0].effort
        print(self.dbmsg.positions)
        msg_dict = {}

        slot_types = [None] * len(self.dbmsg.__slots__) 
        for (attr, type) in zip(self.dbmsg.__slots__, slot_types):
            result = zip(self.dbmsg.__slots__, slot_types)
            resultSet = set(result)
            # print(attr)
=======
>>>>>>> 4f8bc2d5becc86551e855e6e25a224176bfca53f
            # print(result)
            # print(resultSet)
            msg_dict[attr[1:]] = rearrange_value(getattr(self.dbmsg, attr))
            
<<<<<<< HEAD
        print(msg_dict)
        self.publisher_command.publish(self.dbmsg)


=======
        # print(msg_dict)
        self.publisher_state.publish(self.dbmsg)
        # self.get_logger().info("d")
        # x = db.robot.insert_one(post)
        # print(x.inserted_id)
    def dbCommandWriteCallback(self, commandmsg):
        self.dbmsg = Angeltest()
        self.dbmsg.id = 1004
        self.dbmsg.name = "M30_command"
        print(commandmsg)
        self.dbmsg.positions = commandmsg.points[0].effort
        print(self.dbmsg.positions)
        msg_dict = {}

        slot_types = [None] * len(self.dbmsg.__slots__) 
        for (attr, type) in zip(self.dbmsg.__slots__, slot_types):
            result = zip(self.dbmsg.__slots__, slot_types)
            resultSet = set(result)
            # print(attr)
            # print(result)
            # print(resultSet)
            msg_dict[attr[1:]] = rearrange_value(getattr(self.dbmsg, attr))
            
        print(msg_dict)
        self.publisher_command.publish(self.dbmsg)


>>>>>>> 4f8bc2d5becc86551e855e6e25a224176bfca53f
def rearrange_value(v):
    if isinstance(v, list):
        result = []
        for t in v:
            if hasattr(t, 'type'):
                print(t)
                result.append(rearrange_value(None, t, t.type))
            else:
                result.append(rearrange_value(None, t, None))
                print(t)
        return result
    else:
        # print(v)
        return v

def main(args=None):
    if args is None:
        args = sys.argv

    rclpy.init(args=args)

    node = AngelDbcheck()
    rclpy.spin(node) 

if __name__ == '__main__':
    main()










# test topic message
# ros2 topic pub /angel_db_data angel_msg_db/TmsdbStamped 
# "header:
#   stamp:
#     secs: 0
#     nsecs: 0
#   frame_id: ''
# angelsdb:
# - {time: '', type: '', id: 0, name: '', x: 0.0, y: 0.0, z: 0.0, rr: 0.0, rp: 0.0,
#   ry: 0.0, offset_x: 0.0, offset_y: 0.0, offset_z: 0.0, joint: '', weight: 0.0, rfid: '',
#   etcdata: '', place: 0, extfile: '', sensor: 0, probability: 0.0, state: 0, task: '',
#   note: '', tag: ''}"
