""" An example of the 'science' theme. """

import numpy as np 
import matplotlib.pyplot as plt 


shapes = ['X','o', 'd', 'v', '^', '<', '>', 'P', '8', 's', 'p', '*', 'h', 'H', 'D']

# Generate some data to be plotted
x = np.linspace(0,2*np.pi,20)
y = np.cos(x)

with plt.style.context(['science']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig1_science.pdf')
    fig.savefig('figures/fig1_science.png', dpi=600)

with plt.style.context(['science', 'ieee']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig2_science_ieee.pdf')
    fig.savefig('figures/fig2_science_ieee.png', dpi=600)

with plt.style.context(['science', 'scatter']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig3_science_scat.pdf')
    fig.savefig('figures/fig3_science_scat.png', dpi=600)

with plt.style.context(['science', 'high-vis']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig4_science_high_vis.pdf')
    fig.savefig('figures/fig4_science_high_vis.png', dpi=600)

with plt.style.context(['dark_background', 'science', 'high-vis']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig5_Dark_back_science_high_vis.pdf')
    fig.savefig('figures/fig5_Dark_back_science_high_vis.png', dpi=600)

with plt.style.context(['science', 'notebook']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig6_science_notebook.pdf')
    fig.savefig('figures/fig6_science_notebook.png', dpi=600)

# Plot different color cycles 

with plt.style.context(['science', 'bright']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig7_science_bright.pdf')
    fig.savefig('figures/fig7_science_bright.png', dpi=600)

with plt.style.context(['science', 'vibrant']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig8_science_vibrant.pdf')
    fig.savefig('figures/fig8_science_vibrant.png', dpi=600)

with plt.style.context(['science', 'muted']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig9_science_muted.pdf')
    fig.savefig('figures/fig9_science_muted.png', dpi=600)

with plt.style.context(['science', 'retro']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig10_science_retro.pdf')
    fig.savefig('figures/fig10_science_retro.png', dpi=600)

with plt.style.context(['science', 'grid']):
    fig, ax = plt.subplots(2,3,figsize = (12,8))
    for i, axes in enumerate(ax.flat):
        axes.plot(x,y, linestyle=':', marker = shapes[i],label='Data: ' + str(i))
        axes.plot(x,.5*y,linestyle=':', marker = shapes[i],label = 'Data: ' + str(i))
        axes.set_title('Figure')
        axes.set_xlabel('X-label')
        axes.set_ylabel('Y-label')
        axes.legend()
    plt.tight_layout()
    fig.savefig('figures/fig11_science_grid.pdf')
    fig.savefig('figures/fig11_science_grid.png', dpi=600)
