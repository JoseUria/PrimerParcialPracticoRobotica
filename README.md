# Primer Parcial Práctico - Robótica

Integrantes:
- José Manuel Uría Fernandez
  
Este repositorio contiene la implementación de:

● Control cinemático inverso del **Robot A** 

● Control cinemático inverso del **Robot Bio-Inspirado**

● Sistema de sensores con agregación y filtrado de datos en ROS 2

---

## Requisitos

Antes de ejecutar los paquetes, asegúrate de haber compilado el workspace:

```bash
colcon build
source install/setup.bash
```

---

## Robot A

### Ejecución

```bash
ros2 launch robot_description RobotA.launch.py
```

### Control del efector final

En otra terminal:

```bash
ros2 topic pub /target_position geometry_msgs/Point "{x: 1.0, y: 2.0, z: -3.0}"
```

Esto permite modificar en tiempo real la posición deseada del efector final.

---

## Robot Bio-Inspirado

### Ejecución

```bash
ros2 launch robot_description Robotbioinspirado.launch.py
```

### Control del efector final

En otra terminal:

```bash
ros2 topic pub /target_position geometry_msgs/Point "{x: 1.0, y: 2.0, z: -3.0}"
```

---

##  Sistema de Sensores

Este sistema simula tres sensores y un nodo agregador que calcula el promedio y publica un valor filtrado.

### Ejecución

```bash
ros2 launch mypkg sensores.launch.py
```

---

## Visualización de nodos

Para verificar la arquitectura del sistema:

```bash
rqt_graph
```


