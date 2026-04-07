from ament_index_python.packages import get_package_share_path
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch import LaunchDescription
from launch.substitutions import Command


def generate_launch_description():

    # Ruta del URDF (puedes cambiar si tienes otro archivo)
    urdf_path = get_package_share_path('robot_description') / 'urdf/bioinspirado.urdf'
    rviz_path = get_package_share_path('robot_description') / 'rviz/urdf.rviz'

    robot_description = ParameterValue(
        Command(['xacro ', str(urdf_path)]),
        value_type=str
    )

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package='visual_pubsub',
            executable='inverse2',
            name='inverse_kinematics_bio',
            output='screen'
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', str(rviz_path)],
            output='screen'
        ),
    ])