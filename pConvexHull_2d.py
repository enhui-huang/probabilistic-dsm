#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:12:05 2019

@author: enhui
"""

import numpy as np

class ProbabilisticConvexHull_2D:
    """Convex hulls are widely applied in many real wrold problems, including but not limited to computer
    graphics, pattern recognition, image processing, robotics and statistics. For some of these applications,       
    such as sensor databases, location-based services or computer vision, the location and sometimes even the 
    existence of data is uncertain. This probabilistic version of convex hulls is thus proposed to
    characterize the probability distribution of uncertain data.
    
    
    References
    ----------
    [1] Convex Hulls under Uncertainty.Pankaj Agarwal, Sariel Har-Peled, Subhash Suri, Hakan Yildiz and 
    Wuzhou Zhang. Algorithmica 79(2), 340-367, 2017.
    """ 
    
    
    