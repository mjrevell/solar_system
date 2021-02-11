import numpy as np

class Particle:
    
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):
        self.position=np.array(Position, dtype=float)
        self.velocity=np.array(Velocity, dtype=float)
        self.acceleration=np.array(Acceleration, dtype=float)
        self.Name=Name
        self.mass=Mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    n=1     #sets method, n=0 for Euler method, n=1 for Euler-Cromer

    def update(self, deltaT):
        """Updates the positions of all particles"""         
        if self.n==0:    #Euler Method
            self.position=self.position+self.velocity*deltaT
            self.velocity=self.velocity+self.acceleration*deltaT
        elif self.n==1:  #Euler-Cromer Method
            self.velocity=self.velocity+self.acceleration*deltaT
            self.position=self.position+self.velocity*deltaT

    G=G=6.67408E-11

    def KineticEnergy(self):
        """Returns the kinetic energy of a particle"""
        E_k=0.5*self.mass*(np.linalg.norm(self.velocity))**2
        return E_k

    def Momentum(self):
        """returns the momentum of a particle"""
        p=self.mass*self.velocity
        return p
