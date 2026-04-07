from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='mypkg',
            executable='nodo1',
            name='sensor1_node',
            output='screen'
        ),

        Node(
            package='mypkg',
            executable='nodo2',
            name='sensor2_node',
            output='screen'
        ),

        Node(
            package='mypkg',
            executable='nodo3',
            name='sensor3_node',
            output='screen'
        ),

        Node(
            package='mypkg',
            executable='nodo4',
            name='aggregator_node',
            output='screen'
        ),

        Node(
            package='mypkg',
            executable='nodo5',
            name='final_node',
            output='screen'
        ),
    ])