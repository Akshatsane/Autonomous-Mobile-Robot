from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():

    pkg_path = get_package_share_directory("amr_description")

    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true'
    )

    # ---------------- Robot State Publisher ----------------
    urdf_file = os.path.join(pkg_path, 'urdf', 'amr.urdf')

    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {'robot_description': robot_description},
            {'use_sim_time': use_sim_time},
        ],
        output='screen'
    )

    # ---------------- Gazebo ----------------
    world_file = os.path.join(pkg_path, 'worlds', 'lidar_test.world')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        ),
        launch_arguments={
            'world': world_file,
            'use_sim_time': use_sim_time
        }.items()
    )

    # ---------------- Controllers ----------------
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
        output="screen",
    )

    # ---------------- EKF ----------------
    #ekf_node = Node(
    #    package="robot_localization",
    #    executable="ekf_node",
    #    name="ekf_node",
    #    output="screen",
    #    parameters=[
    #        os.path.join(pkg_path, "config", "ekf.yaml"),
    #        {'use_sim_time': use_sim_time}
    #    ],
    #)

    # ---------------- RViz ----------------
    rviz2 = Node(
        package="rviz2",
        executable="rviz2",
        parameters=[{'use_sim_time': use_sim_time}],
        output="screen"
    )

    # ================= FIXED STARTUP ORDER =================

    delay_joint_state = TimerAction(
        period=1.0,
        actions=[joint_state_spawner]
    )

    delay_diff_drive = TimerAction(
        period=2.0,
        actions=[diff_drive_spawner]
    )

    #delay_ekf = TimerAction(
    #    period=3.0,
    #    actions=[ekf_node]
    #)

    delay_rviz = TimerAction(
        period=6.0,
        actions=[rviz2]
    )

    return LaunchDescription([
        declare_use_sim_time,

        robot_state_publisher,
        gazebo,

        delay_joint_state,
        delay_diff_drive,
        #delay_ekf,
        delay_rviz,
    ])