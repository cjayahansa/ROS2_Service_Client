from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cjayahansa',
    maintainer_email='cjayahansa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'my_robot_controller = my_robot_controller.my_robot_controller:main',
            'draw_circle = my_robot_controller.draw_circle:main',
            'pose_subscribe = my_robot_controller.pose_subscribe:main',
            'turtle_controller = my_robot_controller.turtle_controller:main',
        ],
    },
)
