+++
title = "MIMOSA: Multi-Modal SLAM for Resilient Autonomy"
description = "A Multi-Modal SLAM Framework for resilience against sensor degradation."
weight = 70
draft = false

[taxonomies]
tags = ["Autonomy", "Publications"]

[extra]
local_image = "img/projects/mimosa.png"
+++

{{ youtube(id="QDaqS7rL7kA") }}

**Authors**: N. Khedekar, M. Kulkarni and K. Alexis.

**Venue**: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2022.

### Abstract
This paper presents a framework for Multi-Modal SLAM (MIMOSA) that utilizes a nonlinear factor graph as the underlying representation to provide loosely-coupled fusion of any number of sensing modalities. Tailored to the goal of enabling resilient robotic autonomy in GPS-denied and perceptually-degraded environments, MIMOSA currently contains modules for pointcloud registration, fusion of multiple odometry estimates relying on visible-light and thermal vision, as well as inertial measurement propagation. A flexible back-end utilizes the sensing graph structure to provide optimized state estimates and detect sensor degradation, facilitating continued operation when sensing modalities fail or degrade.

#### [Paper Link](https://doi.org/10.1109/IROS47612.2022.9981108) • [Code](https://github.com/ntnu-arl/mimosa) {.centered-text}
