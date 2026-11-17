import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
plt.rcParams.update({'font.family':['Liberation Sans','DejaVu Sans'],'mathtext.fontset':'dejavusans','svg.fonttype':'none','pdf.fonttype':42})
BLACK='#111111'; GREY='#555555'
BLUE='#d3e1f1'; BLUE2='#8fafd6'; GREEN='#dcefe2'; PEACH='#f7d9c4'; LIGHT='#f3f4f6'; WHITE='#ffffff'
def box(ax,x,y,w,h,fc=WHITE,ec=BLACK,lw=0.9,r=1.0,z=1,ls='-'):
    p=FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',fc=fc,ec=ec,lw=lw,zorder=z,ls=ls)
    ax.add_patch(p); return p
def arrow(ax,x0,y0,x1,y1,lw=1.0,ls='-',color=BLACK):
    ax.add_patch(FancyArrowPatch((x0,y0),(x1,y1),arrowstyle='-|>',mutation_scale=7,lw=lw,color=color,ls=ls,shrinkA=0,shrinkB=0,zorder=3))
def canvas(w_in,h_in,W,H):
    fig=plt.figure(figsize=(w_in,h_in)); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off'); return fig,ax
def save(fig,name):
    for ext in ('png','pdf','svg'): fig.savefig(f'{name}.{ext}',dpi=600 if ext=='png' else None)
