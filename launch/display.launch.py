from launch import LaunchDescription #its a container for launch actions
from launch_ros.actions import Node #to launch ROS2 nodes
from ament_index_python.packages import get_package_share_directory #to get package paths
import os #to handle file paths

def generate_launch_description(): #hard boilerplate function  
    pkg_path = get_package_share_directory('amr_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'amr.urdf')
    robot_description = open(urdf_file).read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        )
    ])