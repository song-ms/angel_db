import psutil
import sys
import urllib.request #파이썬3에서
import threading
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
from std_msgs.msg import Float64MultiArray

# apiKey = 'thingSpeak api-key for reading'
# baseURL = 'https://api.thingspeak.com/update?api_key='+apiKey+'&field1='




class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Temperature, '/temperature', 10)
        self.publisher_2 = self.create_publisher(Float64MultiArray, '/cpu_ram_info', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
    # threading.Timer(60.0, updateit).start() #60초마다 실행
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        cpu_temp = psutil.sensors_temperatures()["k10temp"][0].current

        msg = Temperature()
        msg.temperature = cpu_temp
        print("CPU Usage :",cpu_usage)
        print("RAM Usage :",ram_usage)
        print("CPU Temp :",cpu_temp)
        print("--------")
        self.publisher_.publish(msg)

        cpu_ram_msg = Float64MultiArray()
        # cpu_ram_msg.layout[0] = ["cpu_usage", "ram_usage"]
        cpu_ram_msg.data = [cpu_temp, cpu_usage, ram_usage]
        
        self.publisher_2.publish(cpu_ram_msg)




def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()