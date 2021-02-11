import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from Particle import Particle
from SolarSystem import SolarSystem

def Plot():
    """Plots the positions of the bodies in 3D space at every time interval delta for the length of time supplied, 
    axes can be altered by changing the axis_xscale, axis_yscale and axis_zscale lists in the SolarSystem class"""
    ax = plt.axes(projection='3d')

    axes=plt.gca()
    axes.set_xlim(SolarSystem.axis_xscale)
    axes.set_ylim(SolarSystem.axis_yscale)
    axes.set_zlim(SolarSystem.axis_zscale)
 
    for w in SolarSystem.Bodies:
        ax.scatter3D(SolarSystem.xpoints[w], SolarSystem.ypoints[w], SolarSystem.zpoints[w], label=w)

    plt.legend()
    plt.show()
    

def Times():
    """Provides a list of the times for which the simulation is updated"""
    times=[]
    for i in SolarSystem.Data:
        times.append(i[0])
    return times

def E_k():
    """Returns a list of total Kinetic energies of the simulation as time progresses"""
    EK=[]
    for i in SolarSystem.Data:
        E=0
        for j in i[1].keys():
            E+=i[1][j].KineticEnergy()
        EK.append(E)
    return EK

def E_p():
    """Returns a list of total gravitational potential energies of the simulation as time progresses."""
    EP=[]
    for i in SolarSystem.Data:
        E=0
        for index, j in enumerate(i[1].keys()):
            for k in list(i[1].keys())[index:]:
                if j!=k:
                    E+=-Particle.G*i[1][j].mass*i[1][k].mass/(np.linalg.norm(i[1][j].position-i[1][k].position)) #could not be in particle class as the equuation for potential reqquires the masses of two bodies.
        EP.append(E)
    return EP

def E_k_plot():
    """Plots a graph of the total kinetic energy of the simulation as time progresses"""
    plt.plot(Times(),E_k(), label="Kinetic Energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Kinetic energy (J)")
    plt.legend()
    plt.show()
 
def E_p_plot():
    """Plots a graph of the total gravitaational potential energy of the simulation as time progresses"""
    plt.plot(Times(),E_p(), label="Gravitational potential energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Gravitational potential energy (J)")
    plt.legend()
    plt.show()

def Total_Energy():
    """Plots a graph showing how the total energy of the particles in the simulation changes as time progresses"""
    Etot=[]
    for i in range(len(Times())):
        Etot.append(E_k()[i]+E_p()[i])  #Calculates the total energy per time

    plt.plot(Times(),Etot, label="Total Energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Total Energy (J)")
    plt.legend()
    #plt.ylim(-3e35,0)
    plt.show()

def Momentum():
    """Plots a graph showing how te momentum of all the particles in the simulation varies as time progresses"""
    momentum=[]
    for i in SolarSystem.Data:
        m=np.array([0.,0.,0.])
        for j in i[1].keys():
            m+=i[1][j].Momentum()
        momentum.append(np.linalg.norm(np.array(m)))

    plt.plot(Times(), momentum, label="Momentum")
    plt.xlabel("Time (s)")
    plt.ylabel(r"Momentum $(\frac{kgm}{s})$")
    plt.legend()
    #plt.ylim(0,3e29)
    plt.show()

Plot()
#Momentum()
#E_k_plot()
#E_p_plot()
#Total_Energy()