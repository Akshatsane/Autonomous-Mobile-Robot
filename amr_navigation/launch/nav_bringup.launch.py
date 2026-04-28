from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():

    base_path = os.path.join(
        os.getenv('HOME'),
        'amr_ws/src/amr_navigation/launch'
    )

    map_loader = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(base_path, 'map_loader.launch.py')
        )
    )

    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(base_path, 'localization.launch.py')
        )
    )

    navigation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(base_path, 'navigation.launch.py')
        )
    )

    return LaunchDescription([
        map_loader,

        TimerAction(
            period=2.0,
            actions=[localization]
        ),
        TimerAction(
            period=5.0,
            actions=[navigation]
        ),


    ])
