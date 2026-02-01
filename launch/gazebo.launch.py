from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():

    pkg_path = get_package_share_directory("amr_description")

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        )
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-topic", "robot_description",
            "-entity", "amr"
        ],
        output="screen",
    )

    joint_state_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller"],
    #    remappings=[("/cmd_vel","/diff_drive_controller/cmd_vel_unstamped"),
    #                ("/diff_drive_controller/odom", "/odom")],
        output="screen",
    )
    ekf_node = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_node",
        output= "screen",
        parameters = [os.path.join(pkg_path, "config", "ekf.yaml")],
    )

    return LaunchDescription([
        gazebo,
        spawn_entity,
        joint_state_spawner,
        diff_drive_spawner,
        ekf_node,
    ])
