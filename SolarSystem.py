import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from Particle import Particle
import math
import copy

class SolarSystem:
 
    
 
    Bodies = {
    "Sun": Particle(np.array([-5.268391798044327E+08, 1.121961619492936E+09, 2.303527271642291E+06]), np.array([-1.458972541688275E+01, -2.832859102319356, 4.012008784973518E-01]), np.array([0,0,0]),'Sun', 1988500e24),  
    "Mercury": Particle(np.array([-5.669018162803669E+10, 7.008195061744226E+09, 5.635150439174352E+09]), np.array([-1.521806038600316E+04, -4.635893621771400E+04, -2.392854154766454E+03]), np.array([0,0,0]),'Mercury', 3.302e23), 
    "Venus": Particle(np.array([8.246543740774950E+10, -6.919156287526262E+10, -5.751914587944355E+09]), np.array([2.240047318813742E+04, 2.658488246369971E+04, -9.282854972459447E+02]), np.array([0,0,0]),'Venus', 48.685e23),
    "Earth": Particle(np.array([5.906912657111683E+10, 1.361364615947178E+11, -4.053347636044025E+06]), np.array([-2.776505428873560E+04, 1.191351144213665E+04, 1.049235001183924E-06]), np.array([0,0,0]),'Earth', 5.97237e24),
    "Mars": Particle(np.array([-2.269765923061599E+11, -8.439854451129478E+10, 3.766406579966728E+09]), np.array([9.450111587574932E+03, -2.059773509516776E+04, -6.633806333549366E+02]), np.array([0,0,0]),'Mars', 6.4171e23),
    "Jupiter": Particle(np.array([4.702337191946314E+10, -7.809871652380029E+11, 2.186985246720254E+09]), np.array([1.288248808230946E+04, 1.408096008552179E+03, -2.940330994804424E+02]), np.array([0,0,0]),'Jupiter', 1898.13e24),
    "Saturn": Particle(np.array([5.470899048658303E+11, -1.396979427977031E+12, 2.511176088232636E+09]), np.array([8.458315571985436E+03, 3.494319061589365E+03, -3.976061988801199E+02]), np.array([0,0,0]),'Saturn', 5.6834e26),
    "Uranus": Particle(np.array([2.436281384336293E+12, 1.690650542307573E+12, -2.528320960737050E+10]), np.array([-3.932436201328645E+03, 5.277484871220007E+03, 7.089560790105365E+01]), np.array([0,0,0]),'Uranus', 86.813e24),
    "Neptune": Particle(np.array([4.371367805850703E+12, -9.643277653361726E+11, -8.088408981320387E+10]), np.array([1.134049327787622E+03, 5.339872901957968E+03, -1.355977575275114E+02]), np.array([0,0,0]),'Neptune', 102.413e24),
    "Pluto": Particle(np.array([1.928267996633479E+12, -4.694008966102598E+12, -5.548298611397791E+10]), np.array([5.144539834778824E+03, 8.922443245187941E+02, -1.603509104441115E+03]), np.array([0,0,0]),'Pluto', 1.307e22)
    }
    #Bodies can be modified, added or removed

    delta=3600      #time step in seconds, can be changed
    time=31500000   #total time the simulation is run for in seconds, can be changed
    
    axis_xscale=[-5*10**12,5*10**12] #modifies the x axis of the graph plotted by the Plot() function
    axis_yscale=[-5*10**12,5*10**12] #modifies the y axis of the graph plotted by the Plot() function
    axis_zscale=[-5*10**12,5*10**12] #modifies the z axis of the graph plotted by the Plot() function

    xpoints={}
    ypoints={}
    zpoints={}

    Data=[]     #this will become a list of all the positions, velocities and accelerations of all particles for every value of delta
 
    for body in Bodies:     #creates a list of x, y and z co-ordinates for every body in SolarSystem.Bodies, allowing bodies to be added and removed without having to change the code
        xpoints[body]=[]
        ypoints[body]=[]
        zpoints[body]=[]
 
    acc=np.array([0,0,0], dtype=float)
    for i in range(time):
        if i % delta == 0:  #ensures the calculations are done for multiples of the time step delta supplied
            for j in Bodies:
                Bodies[j].acceleration=np.array([0,0,0], dtype=float)
                for k in Bodies:
                    if k==j:
                        continue    #so the body does not interact with itself
                    else:
                        r=np.linalg.norm(Bodies[k].position-Bodies[j].position)
                        Vector=(Bodies[k].position-Bodies[j].position)/r
                        acc=(Particle.G*Bodies[k].mass/(r**2))*Vector
                        Bodies[j].acceleration+=np.array(acc, dtype=float)
                
                Bodies[j].update(delta)
                xpoints[j].append(Bodies[j].position[0])
                ypoints[j].append(Bodies[j].position[1])
                zpoints[j].append(Bodies[j].position[2])

            item = [i, copy.deepcopy(Bodies)]
            Data.append(item)
