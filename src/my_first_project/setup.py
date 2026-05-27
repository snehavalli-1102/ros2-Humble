from setuptools import find_packages, setup

package_name = 'my_first_project'

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
    maintainer='snehavalli',
    maintainer_email='snehavalli@todo.todo',
    description='My first ROS 2 project package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_first_project.my_node:main',
            'draw_circle = my_first_project.draw_circle:main',
            "pose_subscriber = my_first_project.pose_subscriber:main",
            "turtle_controller=my_first_project.turtle_controller:main"
        ],
    },
)