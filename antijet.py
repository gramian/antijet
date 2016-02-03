def antijet(n):
# antijet colormap
# by Stephan Rave 2016
# released under BSD 2-Clause License ( opensource.org/licenses/BSD-2-Clause )

    from numpy import *
    L = linspace(0,1,n)

    R = -0.5*sin( L*(1.37*pi)+0.13*pi )+0.5
    G = -0.4*cos( L*(1.5*pi) )+0.4
    B =  0.3*sin( L*(2.11*pi) )+0.3

    return array([L, R, G, B]).T


def antijet_paraview(n):
    # tested with ParaView 4.0.1

    lines = ['<Point x="{:.5}" o="1" r="{:.5}" g="{:.5}" b="{:.5}"/>'
             .format(l, r, g, b) for l, r, g, b in antijet(n)]

    return ('<ColorMap name="antijet" space="RGB">\n'
            + '\n'.join(lines) + '\n</ColorMap>')
