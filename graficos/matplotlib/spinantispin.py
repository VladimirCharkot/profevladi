import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

PI = math.pi
PI2 = 2 * PI
def round5(v): 
    return round(v,5)

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def asTuple(self):
        return (self.x,self.y)
    

class routineDrawer(object):
    armLen = 0.6
    clubLen = 0.3
    tupr = 24   # Time units per revolution
    tail = 175
    dt = 1/(tupr*8)
    #ts = [dt*n for n in range(tslen)]
    fig = None
    
    def __init__(self):
        self.fig = plt.figure(num='Swing Simu')
        
    def sliceRail(self, start, end):
        if start < 0: 
            start = 200 + start
            rail = self.ts[start:] + self.ts[:end]
        else: 
            rail = self.ts[start:end]
        return rail

    def movie_factory(self, phase, routine):
        """r_conf = {'phase' : (move['hand']['phase'][0], move['objt']['phase'][0]),
                     'spin'  : (move['hand']['spin'][0],  move['objt']['spin'][0])}"""
        routine_len = max(routine, key=lambda f: f['t'])['t']
        revolutions = routine_len/self.tupr
        tslen = int(revolutions/self.dt)
        self.ts = [self.dt*n for n in range(tslen)]
        self.phase = phase
        ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
        #ax.set_title()
        #ax.text(-1.1,1.1,str(r_conf['s']) + ', ' + str(l_conf['s']))
        ax.axis('off')
        rh_trace, = ax.plot([], [], '-', color='mistyrose', lw=2)
        lh_trace, = ax.plot([], [], '-', color='powderblue', lw=2)
        #center_trace = ax.plot([], [], '-', color='gainsboro', lw=2)
        ro_line, = ax.plot([], [], '-', color='mistyrose', lw=1)
        lo_line, = ax.plot([], [], '-', color='powderblue', lw=1)
        rh_marker, = ax.plot([],[], 'o', color='mistyrose')
        lh_marker, = ax.plot([],[], 'o', color='powderblue')
        ro_marker, = ax.plot([],[], 'ro')
        lo_marker, = ax.plot([],[], 'bo')
        
        def movie(i):
            end_i = i % len(self.ts)
            start_i = end_i - self.tail
            rail = self.sliceRail(start_i,end_i)
            t = rail[-1]
            
            frame = next((f for f in routine if t < f['t']*(1/self.tupr)), routine[-1])
            """{'t' : 24,
                'l' : (2,-1),
                'r' : (2,-3)}"""
            
            rhs = frame['r'][0]
            rhp = self.phase['r'][0]
            lhs = frame['l'][0]
            lhp = self.phase['l'][0]
            
            ros = frame['r'][1]
            rop = self.phase['r'][1]
            los = frame['l'][1]
            lop = self.phase['l'][1]
            
            rh = self.handPos(rhs,rhp,t)
            lh = self.handPos(lhs,lhp,t)
            ro0 = self.objectPos(ros,rop,t)
            lo0 = self.objectPos(los,lop,t)
            ro = rh + ro0
            lo = lh + lo0
            
            # Right hand marker
            rh_marker.set_data([rh.x],[rh.y])
            
            # Left hand marker
            lh_marker.set_data([lh.x],[lh.y])
            
            # Right object marker
            ro_marker.set_data([ro.x],[ro.y])
            
            # Left object marker
            lo_marker.set_data([lo.x],[lo.y])
            
            # Right object line
            rl_points = [(rh.x,rh.y),(ro.x,ro.y)]
            ro_line.set_data(zip(*rl_points))
            
            # Left object line
            ll_points = [(lh.x,lh.y),(lo.x,lo.y)]
            lo_line.set_data(zip(*ll_points))
            
            # Right object trace
            ro_points = [self.handPos(rhs,rhp,t) + self.objectPos(ros,rop,t) for t in rail]
            r_trace = list(map(lambda p: p.asTuple(), ro_points))
            rh_trace.set_data(zip(*r_trace))
            
            # Left object trace
            lo_points = [self.handPos(lhs,lhp,t) + self.objectPos(los,lop,t) for t in rail]
            l_trace = list(map(lambda p: p.asTuple(), lo_points))
            lh_trace.set_data(zip(*l_trace))
            
            return (rh_trace, lh_trace, 
                   ro_marker, lo_marker, 
                   rh_marker, lh_marker,
                   ro_line, lo_line)
        
        return movie
    
    def handPos(self, hs, hp, t):
        """conf = {'spin'  : (1,-3),
                   'phase' : (1,0)}"""
        hx = self.armLen * math.cos(hs * PI2 * t + hp * PI)
        hy = self.armLen * math.sin(hs * PI2 * t + hp * PI)
        return Point(hx,hy)
    
    def objectPos(self, os, op, t):
        cx = self.clubLen * math.cos(os * PI2 * t + op * PI)
        cy = self.clubLen * math.sin(os * PI2 * t + op * PI)
        return Point(cx,cy)
    
    def frameToConfig(self, move):
        {'hand' : {'spin' : (1,1), 
                   'phase' : (0,0)},
         'objt' : {'spin' : (1,1), 
                   'phase' : (0,0)}
        }
        right_side = {'phase' : (move['hand']['phase'][0], move['objt']['phase'][0]),
                      'spin'  : (move['hand']['spin'][0],  move['objt']['spin'][0])}
        left_side =  {'phase' : (move['hand']['phase'][1], move['objt']['phase'][1]),
                      'spin'  : (move['hand']['spin'][1],  move['objt']['spin'][1])}
        return right_side, left_side
    
    def anim(self, initial, routine):
        #right_config, left_config = self.frameToConfig(routine[0])
        #right_config = {'spin'  : (1,3),
        #                'phase' : (1,0)}
        #left_config  = {'spin'  : (1,-3),
        #                'phase' : (0,0)}
        upd = self.movie_factory(initial, routine)
        ani = animation.FuncAnimation(self.fig, upd, frames=len(self.ts),  
                                      interval=15, blit=True)
        #o_writer = animation.FFMpegFileWriter()
        #print("Saving...")
        #ani.save('basic_animation.mp4',
        #         writer = o_writer)
        plt.show()
        return ani

"""
'o' == 'origin'
'a' == 'alternative'
moves = {'PS' : {'o' : {'spin' : (1,1), 
                        'phase' : (0,0)}, 
                 'a' : {'spin' : (-1,-1), 
                        'phase' : (0,0)}},
         'PA' : {'o' : {'spin' : (1,1),
                        'phase' : (1,0)},
                 'a' : {'spin' : (-1,-1),
                        'phase' : (1,0)}},
         'CS' : {'o' : {'spin' : (1,-1), 
                        'phase' : (0,0)}, 
                 'a' : {'spin' : (-1,1), 
                        'phase' : (0,0)}},
         'CA' : {'o' : {'spin' : (1,-1), 
                        'phase' : (1,0)}, 
                 'a' : {'spin' : (1,-1), 
                        'phase' : (1,0)}}
         }
        
routine = [{'hand' : moves['PA']['o'],
            'objt' : moves['PA']['o']}]
"""

initial = {'r' : (1,0),
           'l' : (0,0)}

routine = [{'t' : 24,
            'l' : (2,5),
            'r' : (2,-4)},
            {'t' : 48,
             'l' : (2,2),
             'r' : (2,-2)}]
"""
right_config = {'s' : (2,-1),   #spin
                'p' : (1,0),    #phase
                't' : 24}        #time
left_config  = {'s' : (2,-3),
                'p' : (0,0),
                't' : 24}

rd = routineDrawer()
a = rd.anim([left_config, right_config)]"""

rd = routineDrawer()
a = rd.anim(initial, routine)
#plt.close()