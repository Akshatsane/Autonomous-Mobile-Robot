# 🤖 AMR ROS2 Navigation Stack

A complete ROS2-based Autonomous Mobile Robot (AMR) stack including:

- Robot description (URDF + Gazebo simulation)
- Localization (AMCL / SLAM)
- Navigation (Nav2)
- Sensor fusion (EKF)

---

# 🛠️ Requirements

## 🖥️ System

- Ubuntu 22.04 LTS
- ROS2 Humble Hawksbill
- Python 3.10+

---

# 📦 Packages

| Package | Description |
|--------|------------|
| `amr_description` | Robot model, URDF, Gazebo simulation |
| `amr_navigation`  | Localization, mapping, and navigation stack |

---

## 🚀 Quick Start

### 1. Clone workspace

bash
```
mkdir -p ~/amr_ws
cd ~/amr_ws
git clone git@github.com:Akshatsane/Autonomous-Mobile-Robot.git
```

### 2. Build

```bash
cd ~/amr_ws
colcon build
source ~/amr_ws/install/setup.bash
```
Instead of sourcing different bash files, open the bashrc file with the first command  and paste the second command in it. And then source all the bash files simultaneously in the terminal using the third command. 

```bash
gedit ~/.bashrc
source ~/amr_ws/install/setup.bash
source ~/.bashrc
```

Also source the ros or add directly to bashrc file using the command above:

```bash
source /opt/ros/humble/setup.bash
```


### 3. Launch Simulation

```bash
ros2 launch amr_description gazebo.launch.py
```

### 4. Run Navigation 

```bash
ros2 launch amr_navigation combined.launch.py
```



## 📬 Contact / Support

If you encounter any issues while setting up or running the project, feel free to reach out:

- 👨‍💻 Author: Akshat Sane
- 📧 Email: akshatsane.as@gmail.com 
- 💼 GitHub: https://github.com/Akshatsane 

---

## 🐛 Reporting Issues

If you find a bug or face a problem:

1. Check existing issues in the repository 
2. Provide:
   - Error logs 
   - Steps to reproduce 
   - Screenshots (if applicable) 
3. Open a new issue 

---

## 🤝 Contributions

Contributions are welcome!  
Feel free to fork the repo and submit a pull request.
