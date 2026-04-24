from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    amcl_config = os.path.join(
        os.getenv('HOME'),
        'amr_ws/src/amr_navigation/config/amcl_params.yaml'
    )

    amcl_node = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',s
        output='screen',
        parameters=[amcl_config, {'use_sim_time': True}]
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'autostart': True,
            'node_names': ['amcl']
        }]
    )

    return LaunchDescription([
        amcl_node,
        lifecycle_manager
    ])
