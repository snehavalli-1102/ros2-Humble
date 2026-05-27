# ROS 2 Humble Workspace

Welcome to my ROS 2 Humble development workspace. This repository contains custom ROS 2 packages built using Python, focusing on node communications, publishers/subscribers, and turtle simulations.

## Workspace Structure
The workspace is organized to keep tracking clean by ignoring local build artifacts (`build/`, `install/`, `log/`) and focusing entirely on source packages:

```text
ros2_ws/
└── src/
    ├── my_first_project/    # Core package containing turtle simulation nodes
    └── my_robot_pkg/        # Secondary robot package setup
